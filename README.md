# machine_learning_project

from asyncore import file_dispatcher
from ctypes import Structure
from importlib.metadata import files
from importlib.resources import path
from msilib.schema import Component
from tkinter.tix import COLUMN
from typing import KeysView
from xml.dom import pulldom

from sklearn import pipeline


my first ML project 4/7/2022

git account : https://github.com/sadishpitchandi/machine_learning_project



 first we create the github respo make that name has  machine learning project 
 install the  git  https://git-scm.com/download/win  
 open one folder like machince project 
 open the git bash  and use command like  " git clone and paste the repo link (https://github.com/sadishpitchandi/machine_learning_project.git) " and enter and cancel
 use : we work in local system what ever change is happen we can commit the change in the github account multplie person can be work in sigle respo

 ""  conda --version""

 creating the conda environment 

 ""
  conda create -p venv python==3.7 -y
  ""
  y =yes venv = virutal environment  p= virtual env is create in current folfer 


  enivornemt variable in system search we get the enivornemt variable click on and chosse path either 

  " C:\sadish\annaconda\files
  C:\sadish\annaconda\files\Scripts "


  " conda create -p venv python==3.7 -y "

  detect the termionate and restart 
  conda init use when you face issue and restart and the detect the terminate

" conda activate venv/"

add the filoe  requirements.txt 
 add the flask we need the api connector


 pip install -r  requirements.txt 

 create the file   app.py to write the flask code


 whatever we write the we push into github

 first we need not rthe venv is enviornment that is not required so we can igone it 
 we ignore the file uswing the  GITIGNORE  that should want toit github

we can DD THE FILE "venv enviorement " in gitigonre


" git status 
  git add.
  git add app.py
   git status "


   commit is create the version 
   "git log " to see previous version 

   "git pull" pull the files

   to create version?commit all changes by git 
   "
   git commit -m "message"


   to see  version /changes to github 

   "
   git push origin main 
   "
   origin is URL   remote the url  use4 code git remote -v



   to create the heruko app

   1. heruko key=c2047bba-ff21-46d3-a071-f7dd811ed1fa   profile  scroll down key is avaible 
   2. app name =pulldomgh


   create the Docker file 

   gunicorn  is reuirement for dockeer 

   to crearte the doc igonore   venv/ is remove


  '   docker build -t ml-project:latest .    '''

    to see load image we use 
    ''''   docker image'''

    to run the docker image 

    """   docker run -p 5000:5000 -e PORT=5000 docker key """

e port =enivorment vartiable  


to stop the image 
 " docker stop image id "
to check the running container 

" docker ps




git init
git pull 
git add .
git commit -m "first ml prpoject"
git push origin main 

create the folder '.github' in right click create thwe folder workflow create the one filesd  'main.yaml'


add the secret  
create the duplicate of github 
go to setting ad click the secret and go to actions and click new respo
name : 'HEROKU_EMAIL'
value : apjsadish2706@gmail.com
 add the new respo
 name " HEROKU_API_KEY
 vvalue : c2047bba-ff21-46d3-a071-f7dd811ed1fa 
 add bew repo
 name :HEROKU_APP_NAME
 value ; mlfirstproject123


create the folder has  "housing"
creat the file 'setup.py'  outside from the housing floder  steup file is like requirements.txt file we use 
pip install -r requirements.txt instead of we use donot isuse that we want to wwrite the code in setup we use python setup.py install


to set the interpretor  use the command  'ctrl+shift+x' tp add the python microsoft
down python base conda envirment 
add the interpretor


first housing folder crete the filres '__init__.py' its python module or python packeges 
hosing is libraues


requirements.txt
sklearn
pandas
numpy

write the code in saetup.py files

terimanal  "python steup.py install"


this not work properly in window use lumius

use "pip install -r requirements.txt" when you -e . is put in the requiremets.txt files.


"pip install -e ."

-e . =   we install the particular folder HOUSING  alos   dot me3ans the current directory search the current directory

first create folder inside the housing 
1.exception
2.logger
3.pipeline      create file in  folder inside the
4.component       __init__.py file
5.config
6.entity


first we work with  
1.logger  =  when we write the code we get the error, to tracke all the progress to check the status ,progess, what is happen we check in logger

once complete the loging go to app.py and 'from housing.loggerimport logging'
logging.info(" we are testing the logging moudle ")
and it will catch the log in housing folder its new created
more files avaible we tracke what is happening 

next we go with excepation

2. exception= we may get the error, excepaional events is occuring how we handling 

once completed  app.py

from housing.exception import HousingException
import sys

try:
          raise Exception(" we are testing custom Exception")
     except Exception as e:
          housing=HousingException(e,sys)
          logging.info(housing.error_message)

and terminate  "python app.py"


3. entity =  we defoine the mutple Structure  like configuration of pipeline amd output this pipeline will produce thouse output we call it has artifact/
             output of machience learning Component  first we define the variable like url it help to read the .yaml filr(stoage file)

  in entity folfer we creae the new file  "config_entity"-> configuration information
     ( some want to know the datainGEITIONCONFIG info that time we go to config_entity )
   ( we give all the information for data ingestion,valition,transformatiom,... ) satyructure of asll the components
and sepecify the all configuration information in that above file

create the notebook floder  and create the example files (example1.ipynb)
pip install ipykernel


datainGEITIONCONFIG= INFORMATION OF SOURCE DATA
nametuples= (a=34,v=6,r=67) we metion sny name in tuples is called named turples. ITr take two parameters  names and list/ it should be permanent cvan not change in between and we want to change we go with dict
dataIngetionconfig is named turples(turples is store the info) to sotrage the info

data download url is source of data 
tgz-DOWNLOAD_DIR is location where the data is tto be located. tgz is compressed file 
raw_data_dir= extract the file (tgz)
ingested_train_dir= train data set folder
ingested_test_dir=test dataset folder


DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path"])
schemafilepath is no of COLUMN Aand datatypes it want create one file that contain (no of COLUMN Aand datatypes) and path is mention in above 


DataTransformationConfig = namedtuple(" DataTransformationConfig",["add_bedroom_per_room",
                                                        "treansformed_train_dir",
                                                        "transformed_test_dir",
                                                        "preprocessed_object_file_path"])
add_bedroom_per_room= new COLUMN
preprocessed_object_file_path= we want to create the pickle file(we do all the feasture engennering steps) ,this file located location is file_path
treansformed_train_dir=when we data set we apply the preprocessed  we can tranformat the dfataset and we store that path in treansformed_train_dir


ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])

onece model is trained we want to expose or ssave in pickle file that path is trauined model file path
base accxuary is we train the model it give best better the older one we except it not not give in that base accacury we reject 
hyposis coming in picture

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path","time_stamp"])
we test data for  model evalution 
we keeq the infor for our model  of all exisdt model has we train a new model 
and we comapre the best model all ready in production  that model is trained  and compare with these two model in model evalution 
alrewady in production model older data set = model_evaluation file path 


ModelPusherConfig = namedtuple("ModelPusherConfig",["export_dir_path "])
wqe campre the above model is gicveuing the best accuracvy we want push in production replached with older model 
to export thee new data in export file path 
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
we want to read the information like url....

we can storage these information in file or database (file.yaml file)
creqate the .yml file and storage all the information in yaml amd read those info and create the objective of all the components

  

  create the folder config
to create the yaml file  and storage that config yaml file in config folder 
and create the file config.yaml file

we give the location of data and we directoruy of that path

we can read these inforamtion(config.yaml file)  througgh CODE AND WE ACCESS THESE FILE IN ENTITYS

*** config folder we can utilise this (config_entity) and this (config.yaml file) and finally we give the configuraion through the piepleine
***confiraution means above = housing folder inside the config we write code for config entity and config.yaml file congiuration
create the file in hosuing folder inside config inside the neww file like configuration.py

in config ionside configuation.oy 
create one class like configuration 
def the function as init and define all compoent like 
   def get_data_transformation_config(self):
        pass

  get_data_transformation_config return we want to mention 
  return is from get_data_transformation_config is function output i/return the enity 

  from housing.entity.config_entity import DataIngestionConfig
  we want to extract this prativcular (config_entity.py )

  def get_data_ingestion_config(self)->DataIngestionConfig:
        pass

      get_data_ingestion_config this particvular function .. return this DataIngestionConfig entity its present in config_entity 
 

 how can i read the file from the config.yaml files and i can cxreate of objectiuve or i can create the nameturple of DataIngestionConfig and return information #dopubt    


 we want to use the yml so we want to install the pyYAML in requirements

 import yaml  
 import os 
 os.getcwd() we can check the directory of current folder 
 'd:\\Project\\machine_learning_project\\notebook' we setect the partichalur 'd:\\Project\\machine_learning_projec\
  os.chdir("d:\\Project\\machine_learning_project")  we want to change the directory
   check again the path 
   os.getcwd()
   os.list(". ") that point to cuurent  directory
   os.list("config")

   config_file_path=os.path.join("config","config.yaml")  we join the path 


   to read the yml file 
    
    config_info=None                # variable emty 
    with open(config_file_path,"rb") as yaml_file:    # we open the yaml_file we mention path and we put the read mode 
    config_info=yaml.safe_load(yaml_file)             #we can save the file in save_load means saving the file in ymlfile
            yaml is libarry   safeload is function and yaml_file is object 

    config_info  is the dict format 

    # we define the function as readyaml files 

    def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise e

    config =read_yaml_file(config_file_path)   
    its variable   function       config file path we that we use to yml file aviab;e at current directory 


    in housing folder 

    ** create the folder  util (helping file  to function to read the yaml files) in util folder create the file as util.py in that create the file as __init__.py

    in hoiusling folder confighuration.py files  we want to mention the 
      
      from housing.util.util import read_yaml_file  we want to read the yaml file in configuration.py file 

      we waNt to create the folder in housing 
      as constant and in that create the file has __init__.py
      constant  we declare the hard conded    we new one folder and declare all the constant its shpould be modelisaed.

      we mention it root dir 
      time stamp 
       we the all the compoent key 
       using config.yaml right we take it and put all the Keys

TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
 TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
 TRAINING_PIPELINE_NAME_KEY = "pipeline_name"

 go congiuration folder 

 def get traing puiepline 
   1.extract the specific value in the dict (confic.info)
   2.use the path its the output(artifact) and mergeing those path like ROOT DIR(mlproject) ---HOUSING IS PIPEL NAME------ ARTIFACT IS PIPLELINE ARTIFACT KEY
   3.call the trainingpipleine=artifict(pand its path)  we get ouput 

   next we go with get data igination config function 

   we write code l;ike  use the dict.path and url ,dir,test,train all the emements 


   same we declre all the function that avaiavble in compoents

  ===================================================================================================

  now we goo for component folder 

  data ingection.py file data_validation.py file ,data_transformation,model_evaluation.py,model_pusher.py,model_trainer.py

  go with data ingection .py file and tyope the code.


  in hosuimg ->entity ->new file as artifact_entity.py

  its oouput of compoents

  input is config_entuity


  and write the code in compoent has            dataingestion.py file 
  give the function as dowloand the dataset,extraxt the dataset,split the datase4t


  url="............"
  import os 
  os.path.basename(url)  we can extract the base url hosuing.tgz

  housing the comp[omenyt and data ingenition ]
  write the code 
  defiune the fucntion of tgz file and split the file

  and go to hpousing the pipeline.py 


  and write the code 
  ===============================================================================
  
create the file demo.py in outer file  (read the pipeline )

run the python demo.py in the terminate we get the new foldeer that are crearte  path is housing artyifact fdir inm that time stampis cxreate and 3 type of folder is the ouput 

================================================================================

#data validation.



firsdt create the outside  "scheme.yaml" file on it it repont the col and its dataypes

create schem file 
next go to constant do the keys that are in config.yaml 

decalre the key 

next go configuration.py file 

====================================================================================
                                housing 
  1. root directory            2. constant              3. config             4. compound                5. pipeline     
     folder 



     config.yaml               constant file           configuration.py          data                     pipeline
                                                                               validation
                                                                               data_tranforamation

                                                     entity.py 
                                                     use in the configuration file.
===============================================================================================


data validation 
