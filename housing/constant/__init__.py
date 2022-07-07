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
