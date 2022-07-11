import os 
from datetime import datetime

ROOT_DIR = os.getcwd() # to get current directory

CONFIG_DIR ="config"   # CONFIG floder is config_dir
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)# ROOT DIR IS LOCATE ML PROJECT CONFIG_DIR IS THE FOLDER OF CONFIG AND CONFIG IS FILE NAME 

 CURRENT_TIME_STAMP =  f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


 #TRAINING PIPELINE RELATED VARIABLE  we want to read the information in config.yaml file  we want to key , we declare it constant variable as key 
 TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
 TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
 TRAINING_PIPELINE_NAME_KEY = "pipeline_name"



# Data Ingestion related variable  WE PRODUCE THE KEY THAT ARE Aviable in yaml file  this mdouleos prupose sand we can see it small letter type we can we see the pop up 

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"



# Data Validation related variables
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"   # config.yaml data validation key ia present two only is there 
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY = "schema_file_name"   #scheme file name key 
DATA_VALIDATION_SCHEMA_DIR_KEY = "schema_dir"
DATA_VALIDATION_ARTIFACT_DIR_NAME="data_validation"                   # when we run the pipleine it generate the output (artifact)   we want to store in that directory 
DATA_VALIDATION_REPORT_FILE_NAME_KEY = "report_file_name"              #  report file path is jso file about the data drify
DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY = "report_page_file_name"     #we wan t to visization the graphy in html page  ,#toi check the validatiobn report 