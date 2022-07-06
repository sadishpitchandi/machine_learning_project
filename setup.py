from setuptools import setup ,find_packages
from typing import List



    

#create the variable
PROJECT_NAME="hosuing-predictor"
VERSION="0.0.3"
AUTHOR="sadish"
DESRCIPTION=" this my first project in ML"
PACKAGES=["housing"] #folder name
REQUIREMENTS_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]: #we weant read the requirement.txt files and return in list which is string value 
    with open(REQUIREMENTS_FILE_NAME) as requirements_files:
        return requirements_files.readlines().remove("-e .") # return this function is going to return a list whcihcontain main of libraies mentioned in requirements files.txt files
    #-e . to check the local packages you created all the python files where the init files is install has libriy is accessable
    # find packages all doing the ssame action so we remove the -e . from requirements.txt
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=find_packages(), # packages is also install in folder and  check the n no of folder where find the init.py filesit will use those folder has packages
    install_requires=get_requirements_list() #extermalrequirement also install


)

   #to check  get_requirements_lists() is working r not 

  # if __name__=="__main__":
   # print(get_requirements_lists())
