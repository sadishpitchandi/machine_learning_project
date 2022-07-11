from housing.entity.config_entity import DataIngestionconfig
import sys,os
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.artifact_entity import DataIngestionArtifact  # we give artifact entity
import tarfile   #to extract the file in tar format(compreesed file)
from six.moves import urllib # this module is use to download  
import pandas as pd 
import numpy as np
from sklearn.model_selection import stratifiedshufflesplit  # use to split the train and test even  stratifiedshufflesplitused to split the same disribution (when pkot in some graph like pie chart you can see the same daigram )

class DataIngestion:


    def __init__(self,data_ingestion_config:DataIngestionconfig):
        try:
            logging.info(f"{'='*20}Data Ingestion log started. {'='*20}")
        except Exception as e:
            raise HousingException(e,sys)
      
    def  download_housing_data(self)->str:    #dowloand the data from the source 
        try:
            #extraction remote url to download datasets
            download_url = self.data_ingestion_config.dataset_download_url # constant we using we get the info.

            #folder location to download file
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir 

            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)
            os.makedirs(tgz_download_dir,exist_ok = True ) # this use to create the new folder 


            housing_file_name = os.path.basename(download_url)  # dowloand url is url is present we want to extract the housing.tgz file name we use os.basename
            logging.info(f"downloading file from :[{download_url}]into : [{tgz_file_path}]")
            tgz_file_path = os.path.join(tgz_download_dir , housing_file_name) # give the complete path of extracted file
            urllib.request.urlretrieve(download_url,tgz_file_path)  #urllib is use to download the dataset and we reuqest it and url retieve command is mention ad dowload url we specifed that path 
            logging.ifo(f"File:[{tgz_file_path}] has been downloaded successfully.")
            return tgz_file_path
        except Exception as e:
            raise HousingException(e,sys) from e 




    def extract_tgz_file(self):          #extract the dowloand file raw datsa is converted into csv file
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir  # extract file  dir is raw data dir 

            if os.path.exists(raw_data_dir):   # we create the new folder 
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir,exist_ok=True)

            logging.info(f"Extracting tgz file: [{tgz_file_path}] into dir: [{raw_data_dir}]")
            with tarfile.open(tgz_file_path) as housing_tgz_file_obj:  # open in tarfile  housing_tgz_file_obj variable 
                housing_tgz_file_obj.extractall(path=raw_data_dir)      #extract in tar file 
            logging.info(f"Extraction completed")

        except Exception as e:
            raise HousingException(e,sys) from e



    def split_data_as_train_test(self) -> DataIngestionArtifact:     # read the csv file split the 80% and 20% data 
         try:
             raw_data_dir = self.data_ingestion_config.raw_data_dir  #raw dir path 

            file_name = os.listdir(raw_data_dir)[0]   # extract the particular  file name 

            housing_file_path = os.path.join(raw_data_dir,file_name)  #folder and file name complete csv file 

            
            logging.info(f"Reading csv file: [{housing_file_path}]")
            housing_data_frame = pd.read_csv(housing_file_path)  # folder and file is there we read the that spefic file using csv we in read mode in csv file3 
            #to split the data  # we want to predictor the median income 

            housing_data_frame["income_cat"] = pd.cut(   #income cat is the catogy  new col use to spilt the data and we detect once the split is completed  # create new colun and catgory is 1,2,3,4,5 
                housing_data_frame["median_income"],         #median income is new columns 
                bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],     #bins is use to draw the histogram  its show the bar 0 to1.5 like it scale 
                labels=[1,2,3,4,5] )                         #level means the data is spi;lted in 5 even data set  # 5 catgory is created .high income fall in the 4 th cateorgy
   
            logging.info(f"Splitting data into train and test")
            strat_train_set = None  # declare the variable 
            strat_test_set = None

            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42) # startfied is use to split the varible evely same percenatge of test and train dataset
                                                                                            n_splits=1 is split is one. test size is 20% ,randow we choose 42 dta set numberf.

            for train_index,test_index in split.split(housing_data_frame, housing_data_frame["income_cat"]): # that whole folder and the specvify the group
                strat_train_set = housing_data_frame.loc[train_index].drop(["income_cat"],axis=1)   #loc = extract the raw by index location  drop the catogry colnum axis =12 is drop the coln 
                strat_test_set = housing_data_frame.loc[test_index].drop(["income_cat"],axis=1)

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,  #save the file of train and path use self.data ingestion config in constant file and use the train-dir path  file name at read tghe pands 
                                            file_name)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                        file_name)
            
            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)  # make the new dir 
                logging.info(f"Exporting training datset to file: [{train_file_path}]")
                strat_train_set.to_csv(train_file_path,index=False)                                 # to sotre it conver into the csv make index has flase 

            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok= True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                strat_test_set.to_csv(test_file_path,index=False)


             data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,  #output of artifact of data ingintion 
                                test_file_path=test_file_path,                                 #both file path is mention 
                                is_ingested=True,                                               # and its mention it true of it 
                                message=f"Data ingestion completed successfully."
                                )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact                      # retun the output 




       except Exception as e:
            
            raise HousingException(e,sys) from e





    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
              # we dowlaond the file and its location
            tgz_file_path =  self.download_housing_data()
            self.extract_tgz_file(tgz_file_path=tgz_file_path)   # extracted file 
            return self.split_data_as_train_test()  # return the split the file 


    def __del__(self):
        logging.info(f"{'>>'*20}Data Ingestion log completed.{'<<'*20} \n\n")



        except Exception as e:
            raise HousingException(e,sys) from e