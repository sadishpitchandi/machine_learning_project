# machine_learning_project

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
   2. app name =mlfirstproject123


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