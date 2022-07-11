from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig  # config entity file importing the data validation hasw (scheme file and )
from housing.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact  # artifact is the output of data ingectyion and its input of data validation oso it mention 
import os,sys
import pandas  as pd
from evidently.model_profile import Profile                              #evidently is libeary use to for data drift
from evidently.model_profile.sections import DataDriftProfileSection #this provide the json kind od report    # data drift is the data have statistica has been changed whewn compare to old data set  run the statistical test and  to compare the input feature distribution and visability of the drift

from evidently.dashboard import Dashboard   # report page  to show the graph in this dashboard module 
from evidently.dashboard.tabs import DataDriftTab
import json                                        # to convert into jsonfiacation  to covert into the dict

class DataValidation:
    

    def __init__(self, data_validation_config:DataValidationConfig,   #DATA_VALIDATION_CONFIG_KEY = "data_validation_config"    its the whole folder like scheme file and resport file and path so it alway metion the  "data_validation_config"  has initial has data type is datvalidationconfig
        data_ingestion_artifact:DataIngestionArtifact):               #data ingewestion artifact  these two information we can validate the data validation 
        try:
            logging.info(f"{'>>'*30}Data Valdaition log started.{'<<'*30} \n\n")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e


    def get_train_and_test_df(self):            #WE GET THE TRAIN AND TEST DATA WE CREATE THE FUNCTION ITS LAST FUNCTION
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)   #USE PANDS TO READ THE FILE  DATA  ingeition artifact used and the file path mention 
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df,test_df
        except Exception as e:
            raise HousingException(e,sys) from e


    def is_train_test_file_exists(self)->bool:  # validating the file first file is aviable are not this is mention here train aand test file is exist and it represnt the boolean type of it 
 
        try:
            logging.info("Checking if training and test file is available")
            is_train_file_exist = False      #both are false is exist we metion ture or false but both will be ture 
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path          # # is train  file is exist at the  praticular directory is the output of data ingestion and mention its train path 
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)     
            is_test_file_exist = os.path.exists(test_file_path)

            is_available =  is_train_file_exist and is_test_file_exist  # both are false its weill return has is avaible the file 

            logging.info(f"Is train and test file exists?-> {is_available}")
            
            if not is_available:
                training_file = self.data_ingestion_artifact.train_file_path  # train file path  and 3 t3st file path
                testing_file = self.data_ingestion_artifact.test_file_path         
                message=f"Training file: {training_file} or Testing file: {testing_file}" \    #message is prinbted and  raise the exception 
                    "is not present"
                raise Exception(message)

            return is_available
        except Exception as e:
            raise HousingException(e,sys) from e

    
    def validate_dataset_schema(self)->bool:
        try:
            validation_status = False
            
            #Assigment validate training and testing dataset using schema file
            #1. Number of Column
            #2. Check the value of ocean proximity 
            # acceptable values     <1H OCEAN
            # INLAND
            # ISLAND
            # NEAR BAY
            # NEAR OCEAN
            #3. Check column names


            validation_status = True
            return validation_status 
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_and_save_data_drift_report(self):
        try:
            profile = Profile(sections=[DataDriftProfileSection()])    # evidenty packge is used profit is object and another profile is classs and section is mention and its inside the data drif profile section is mention it haqs classs it give comapre two data give siginifact different bertween 

            train_df,test_df = self.get_train_and_test_df()    # this fucion get train and test dir give the3 test and train function 

            profile.calculate(train_df,test_df)    #through which provide data drift report abd calculte with profile is class 
                                                     # all the data drift is calculte and in profile  that are convert to the json file 
            report = json.loads(profile.json())       #profile.json() is in json object to convert intro dict wqe use thye json.load 

            report_file_path = self.data_validation_config.report_file_path
            report_dir = os.path.dirname(report_file_path)
            os.makedirs(report_dir,exist_ok=True)

            with open(report_file_path,"w") as report_file:   # to save this json  and W is Written this file ass report file 
                json.dump(report, report_file, indent=6)        #json is dump fuction it give object has report andf report files and indent is  format the datasaet its more readable 
            return report
        except Exception as e:
            raise HousingException(e,sys) from e

    def save_data_drift_report_page(self):
        try:
            dashboard = Dashboard(tabs=[DataDriftTab()])                     # dashbaord is object and classs is another dashboard and in tab must be mention 
            train_df,test_df = self.get_train_and_test_df() # it  give the train df and test df data 
            dashboard.calculate(train_df,test_df)                  # and calulate these data with help of above test amnd tarin the test and represent the graphy there are siugificantly different or not 

            report_page_file_path = self.data_validation_config.report_page_file_path   # to create the folder directory  first we extract it 
            report_page_dir = os.path.dirname(report_page_file_path)                   # mention it directory has os.path 
            os.makedirs(report_page_dir,exist_ok=True)                                #make the directory is ture create the folder 

            dashboard.save(report_page_file_path)                      #save the path in respresentive path 
        except Exception as e:
            raise HousingException(e,sys) from e

    def is_data_drift_found(self)->bool:   # 3 function is data drift is avaible its bool true or flase 
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()
            return True
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_data_validation(self)->DataValidationArtifact :
        try:
            self.is_train_test_file_exists()   # first function is mentioned its tewst and train data is avaible or not.
            self.validate_dataset_schema()      # validating the data(test and train data set)
            self.is_data_drift_found()

            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path,   # artifwact  mention the path scheme and report file and page file path 
                report_file_path=self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated=True,
                message="Data Validation performed successully."
            )
            logging.info(f"Data validation artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e


    def __del__(self):
        logging.info(f"{'>>'*30}Data Valdaition log completed.{'<<'*30} \n\n")
        