#from housing.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig
#from ast import Str
from housing import constant
from housing.entity.config_entity import DataIngestionConfig, DataTransformationConfig,DataValidationConfig,   \
ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig 
from housing.util.util import read_yaml_file
from housing.constant import *
import sys,os
from housing.logger import logging 
from housing.exception import HousingException


class Configuartion:
     ''' when we insitise the new obvject ( Like configuration().get_data-validation)
        first it call the init fuction as first '''




    def __init__(self
        config_file_path:Str = CONFIG_FILE_PATH ,   # READ THE  config path and go that config folder and read the config fdile
        current_time_stamp:str = CURRENT_TIME_STAMP
     )->None:
     try:
        self.config_info = read_yaml_file(file_path=CONFIG_FILE_PATH)    # CONFIG INFO IS  totsal file util.py (its contain .yaml file in dict format) if we call the config info=it show the dict of all the .yaml files loades  (.yaml file conatin the information (xconfig.yaml files))
        self.training_pipeline_config = self.get_training_pipeline_config()   
        self.time_stamp = current_time_stamp
    except Exceptionas e:
        raise HousingException(e,sys) from e



    def get_data_ingestion_config(self) ->DataIngestionConfig:    # wecall get data ingestion config we can get the all thee folder path its creayte only the path not a folfer
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir  #we want the data ignition artifact dir (for tgz _download_url) and put self.training_pipeline_config = self.get_training_pipeline_config()  thuis we get the c:sadish:project:mlproject  and put artifact dir  we get c:sadish:project:mlproject:artificatdir
            data_ingestion_artifact_dir=os.path.join(                 #dqata ignition artifact dir is ouput we want to store in specfic folder 
                artifact_dir,                                         #we mention path of artifict dir in above 
                DATA_INGESTION_ARTIFACT_DIR,                          #DATA_INGESTION_ARTIFACT_DIR it the constant  and give data ingition (it give all the url,test train dir of 2 path)
                self.time_stamp                                       # we the time stamp
            )
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]   # we give all infomatipon of data ingestion like url root dir test train file... we get it from the .yaml mile and we use config info we can get the dict and extract it 
  # declare valure to the varible           
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]   # weput the variable as data ingestioninfo and declare constant(it may pop up) we extract the url
            tgz_download_dir = os.path.join(                                               # when we put dir we want to put path so os.path.join  
                data_ingestion_artifact_dir,                                       #mention artifact dir 
                data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]            #  3use the constant
            )
            raw_data_dir = os.path.join(data_ingestion_artifact_dir,                # we mention path of artificat dir and constant of raw darta
            data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )

            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,                        # we mention tha aritfact and const
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY]
            )
            ingested_train_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]    #in ingested_data_dir folder there is two fiolder is train dir and test dir 
            )                                                        #so it mention ingested_data_dir this dir and use constant file of train dir and te3st dir consatnt
            ingested_test_dir =os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
            )


            data_ingestion_config=DataIngestionConfig(                  # data ingetion cofig pass all the parament url,dir,test... abd create the cvarible i above 
                dataset_download_url=dataset_download_url, 
                tgz_download_dir=tgz_download_dir, 
                raw_data_dir=raw_data_dir, 
                ingested_train_dir=ingested_train_dir, 
                ingested_test_dir=ingested_test_dir
            )
            logging.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys) from e
#data validatio         
    def get_data_validation_config(self)-> DataValidationConfig:   #DataValidationConfig it go the entity folder 
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir  # it give the root directory like housing??artifact 

            data_validation_artifact_dir=os.path.join(   # we create the validatgion artifaact dir is the folder how it create with help of
                artifact_dir,             # root dir 
                DATA_VALIDATION_ARTIFACT_DIR_NAME,   #its key inside  data validation is there so  we call the key it produce the data validation folder in artifacte folder 
                self.time_stamp                       #it produce the time stamp of it 
            )
            data_validation_config = self.config_info[DATA_VALIDATION_CONFIG_KEY]  # first we do the scheme file path so we want extract the information on "enity.yaml "   self.config_info[DATA_VALIDATION_CONFIG_KEY] when call this we can get the all the scheme dir:config,scheme file name : scheme.yaml file



            schema_file_path = os.path.join(ROOT_DIR,                        #we want the schem,e file path so we want to root dir , config and scheme .yaml file path 
            data_validation_config[DATA_VALIDATION_SCHEMA_DIR_KEY],         #WE EXTRACT IT FROM THE ABoVE DICT and it mentioned and we extract with key of the dict  .(DATA_VALIDATION_CONFIG_KEY]) with help of constant file we use the wscheme kleys and get config folder 
            data_validation_config[DATA_VALIDATION_SCHEMA_FILE_NAME_KEY]      # with help of the constant file the key and we the scheme file  has scheme.yaml 
            )

            report_file_path = os.path.join(data_validation_artifact_dir,     #we want to find the record path so  final report path is used in  that artificat dir inside data validation inside the report file its show json   
            data_validation_config[DATA_VALIDATION_REPORT_FILE_NAME_KEY]     # datavalidation config(confiog.yaml) we can call it file name has key used in the constant 
            )

            report_page_file_path = os.path.join(data_validation_artifact_dir,
            data_validation_config[DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY]    #same approch 

            )

            data_validation_config = DataValidationConfig(     # finaal of the3 data validation   we get scheme file path 
                schema_file_path=schema_file_path,                    # above the variable mention in valkidation config the fianl function 
                report_file_path=report_file_path,
                report_page_file_path=report_page_file_path,
            )
            return data_validation_config
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir

            data_transformation_artifact_dir=os.path.join(
                artifact_dir,
                DATA_TRANSFORMATION_ARTIFACT_DIR,
                self.time_stamp
            )

            data_transformation_config_info=self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]

            add_bedroom_per_room=data_transformation_config_info[DATA_TRANSFORMATION_ADD_BEDROOM_PER_ROOM_KEY]


            preprocessed_object_file_path = os.path.join(
                data_transformation_artifact_dir,
                data_transformation_config_info[DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY],
                data_transformation_config_info[DATA_TRANSFORMATION_PREPROCESSED_FILE_NAME_KEY]
            )

            
            transformed_train_dir=os.path.join(
            data_transformation_artifact_dir,
            data_transformation_config_info[DATA_TRANSFORMATION_DIR_NAME_KEY],
            data_transformation_config_info[DATA_TRANSFORMATION_TRAIN_DIR_NAME_KEY]
            )


            transformed_test_dir = os.path.join(
            data_transformation_artifact_dir,
            data_transformation_config_info[DATA_TRANSFORMATION_DIR_NAME_KEY],
            data_transformation_config_info[DATA_TRANSFORMATION_TEST_DIR_NAME_KEY]

            )
            

            data_transformation_config=DataTransformationConfig(
                add_bedroom_per_room=add_bedroom_per_room,
                preprocessed_object_file_path=preprocessed_object_file_path,
                transformed_train_dir=transformed_train_dir,
                transformed_test_dir=transformed_test_dir
            )

            logging.info(f"Data transformation config: {data_transformation_config}")
            return data_transformation_config
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir

            model_trainer_artifact_dir=os.path.join(
                artifact_dir,
                MODEL_TRAINER_ARTIFACT_DIR,
                self.time_stamp
            )
            model_trainer_config_info = self.config_info[MODEL_TRAINER_CONFIG_KEY]
            trained_model_file_path = os.path.join(model_trainer_artifact_dir,
            model_trainer_config_info[MODEL_TRAINER_TRAINED_MODEL_DIR_KEY],
            model_trainer_config_info[MODEL_TRAINER_TRAINED_MODEL_FILE_NAME_KEY]
            )

            model_config_file_path = os.path.join(model_trainer_config_info[MODEL_TRAINER_MODEL_CONFIG_DIR_KEY],
            model_trainer_config_info[MODEL_TRAINER_MODEL_CONFIG_FILE_NAME_KEY]
            )

            base_accuracy = model_trainer_config_info[MODEL_TRAINER_BASE_ACCURACY_KEY]

            model_trainer_config = ModelTrainerConfig(
                trained_model_file_path=trained_model_file_path,
                base_accuracy=base_accuracy,
                model_config_file_path=model_config_file_path
            )
            logging.info(f"Model trainer config: {model_trainer_config}")
            return model_trainer_config
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_model_evaluation_config(self) ->ModelEvaluationConfig:
        try:
            model_evaluation_config = self.config_info[MODEL_EVALUATION_CONFIG_KEY]
            artifact_dir = os.path.join(self.training_pipeline_config.artifact_dir,
                                        MODEL_EVALUATION_ARTIFACT_DIR, )

            model_evaluation_file_path = os.path.join(artifact_dir,
                                                    model_evaluation_config[MODEL_EVALUATION_FILE_NAME_KEY])
            response = ModelEvaluationConfig(model_evaluation_file_path=model_evaluation_file_path,
                                            time_stamp=self.time_stamp)
            
            
            logging.info(f"Model Evaluation Config: {response}.")
            return response
        except Exception as e:
            raise HousingException(e,sys) from e


    def get_model_pusher_config(self) -> ModelPusherConfig:
        try:
            time_stamp = f"{datetime.now().strftime('%Y%m%d%H%M%S')}"
            model_pusher_config_info = self.config_info[MODEL_PUSHER_CONFIG_KEY]
            export_dir_path = os.path.join(ROOT_DIR, model_pusher_config_info[MODEL_PUSHER_MODEL_EXPORT_DIR_KEY],
                                           time_stamp)

            model_pusher_config = ModelPusherConfig(export_dir_path=export_dir_path)
            logging.info(f"Model pusher config {model_pusher_config}")
            return model_pusher_config

        except Exception as e:
            raise HousingException(e,sys) from e
    def get_training_pipeline_config(self) ->TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]  # TRAINING_PIPELINE_CONFIG_KEYgive this infomration training_pipeline_config  .....config_info[TRAINING_PIPELINE_CONFIG_KEY] give the {pip[leine name: housing ,,artifact_dir=artyifact]}
            artifact_dir = os.path.join(ROOT_DIR,               #root dir  d:project: machi8en leARNING
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],                   # IT CONFIG.YAML FILE PIPLEINE NAME =HPOUSING 
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )  #IT CAN CHOOSE THE PATH IN ARTIFACT DIR .. ROOT DIR(mlproject) ---HOUSING IS PIPEL NAME------ ARTIFACT IS PIPLELINE ARTIFACT KEY
            training_pipleine_config = TrainingPipelineConfig(artifact_dir=artifact_dir) #ouput it show like trainingpiplineconfig(artifact_dir= path)
            logging.info(f"Training pipeline config :{training_pipeline_config}")        #CONFIG ITS CARE ONLY ONE DIR ITS PIPLEINE OUTPUT 
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e
