from housing.entity.config_entity import DataIngestionconfig
import sys,os
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.artifact_entity import DataIngestionArtifact  # we give artifact entity
import tarfile   #to extract the file in tar format(compreesed file)
from six.moves import urllib # this module is use to download  


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
            pass
        except Exception as e:
            raise HousingException(e,sys) from e 
    def split_data_as_train_test(self):     # read the csv file split the 80% and 20% data 
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e





    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            tgz_file_path = self.download_housing_data()  # we dowlaond the file and its location




        except Exception as e:
            raise HousingException(e,sys) from e