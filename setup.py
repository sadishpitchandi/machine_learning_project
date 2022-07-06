from setuptools import setup
from typing import List



    

#create the variable
PROJECT_NAME="hosuing-predictor"
VERSION="0.0.1"
AUTHOR="sadish"
DESRCIPTION=" this my first project in ML"
PACKAGES=["housing"] #folder name
REQUIREMENTS_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]: #we weant read the requirement.txt files and return in list which is string value 
    with open(REQUIREMENTS_FILE_NAME) as requirements_files:
        return requirements_files.readlines() # return this function is going to return a list whcihcontain main of libraies mentioned in requirements files.txt files

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=PACKAGES, # packages is a;l0os install in folder and requirement also install
    install_requires=get_requirements_list()


)

   #to check  get_requirements_lists() is working r not 

  # if __name__=="__main__":
   # print(get_requirements_lists())
