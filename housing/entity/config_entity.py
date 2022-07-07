from collections import namedtuple



DataIngestionconfig=namedtuple("DataIngestionconfig",
["dataset_download_url","tgz_dowmloads","raw_data_dir","ingested_train_dir","ingested_test_dir"])

""" this namedtuples we can give the name and url=....."""

DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path"])


DataTransformationConfig = namedtuple(" DataTransformationConfig",["add_bedroom_per_room",
                                                        "treansformed_train_dir",
                                                        "transformed_test_dir",
                                                        "preprocessed_object_file_path"])
            

ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])


ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path","time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig",["export_dir_path "])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",["artifact_dir"])