#from housing.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig
#from ast import Str
from housing.entity.config_entity import DataIngestionConfig, DataTransformationConfig,DataValidationConfig,   \
ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig 
from housing.util.util import read_yaml_file
from housing.constant import *
import sys,os
from housing.logger import logging 
from housing.exception import HousingException


class Configuartion:
    def __init__(self
        config_file_path:Str = CONFIG_FILE_PATH ,   # READ THE  config path and go that config folder and read the config fdile
        current_time_stamp:str = CURRENT_TIME_STAMP
     )->None:
     self.config_info = read_yaml_file(file_path=CONFIG_FILE_PATH)
     self.training_pipeline_config = self.get_training_pipeline_config()   
     self.time_stamp = current_time_stamp



    def get_data_ingestion_config(self)-> DataIngestionConfig:
        pass
    def get_data_validation_config(self)-> DataValidationConfig:
        pass
    def get_data_transformation_config(self)-> DataTransformationConfig:
        pass
    def get_data_trainer_config(self)->ModelTrainerConfig:
        pass
    def get_data_evaluation_config(self)->ModelEvaluationConfig:
        pass
    def get_data_model_pusher_config(self)->ModelPusherConfig:
        pass
    def get_training_pipeline_config(self) ->TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]  # TRAINING_PIPELINE_CONFIG_KEYgive this infomration training_pipeline_config  .....config_info[TRAINING_PIPELINE_CONFIG_KEY] give the {pip[leine name: housing ,,artifact_dir=artyifact]}
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )  #IT CAN CHOOSE THE PATH IN ARTIFACT DIR .. ROOT DIR(mlproject) ---HOUSING IS PIPEL NAME------ ARTIFACT IS PIPLELINE ARTIFACT KEY
            training_pipleine_config = TrainingPipelineConfig(artifact_dir=artifact_dir) #ouput it show like trainingpiplineconfig(artifact_dir= path)
            logging.info(f"Training pipeline config :{training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e
