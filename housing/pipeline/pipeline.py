from collections import namedtuple
from datetime import datetime
from tkinter import E
import uuid
from housing.config.configuration import Configuartion   # importing the  classs from configuration 
from housing.logger import logging, get_log_file_name
from housing.exception import HousingException
from threading import Thread
from typing import List
import sys,os 


class pipeline:

    def __init__(self,config: configuartion = configuartion())-> None:
        try:
            self.config=config

        except Exception as e:
            raise Exception as e:
            raise HousingException(e,sys) from e 
    
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()

        except Exception as e:
            raise HousingException(e,sys) from e 


    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) \
            -> DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),  #ITS GIVBE THE  all the scheme file and  report file report path 
                                             data_ingestion_artifact=data_ingestion_artifact                               #data inginition artifact is the inpuyt of the data validatiobn and it has the test and train data 
                                             )
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise HousingException(e, sys) from e



   
    def start_data_tranformation(self):
        pass
    def start_model_trainer(self):
        pass
    def start_model_evalution(self):
        pass
    def start_model_pusher(self):
        pass





        def run_pipeline(self):
            try:
                #dataingestion

                data_ingestion_artifact = self.start_data_ingestion()
                data_validation_artifact = self.start_data_validation(data_ingestion_artifact = data_ingestion_artifact)

            except Exception as e:
                raise HousingException(e,sys) from e