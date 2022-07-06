# machine_learning_project

from xml.dom import pulldom


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























 question 
        1.'docker' is not recognized as an internal or external command,   docker image    docker run -p 5000:5000 -e PORT=5000 docker key 
         operable program or batch file.
         2. explaination of main.yml
         3.heroku open app is not working
         4.interpretor path is not found
         5. list is using the setup.py files y not truples
         6.log cannot be catch in the file