from distutils.log import INFO
import logging 
from datetime import datetime
import os
              # we nned the one folder inside one files  LOG  files in in the log_dir folder folder name is ;housingh_logs
LOG_DIR="housing_logs"
             # when we trace the piepline that time stamp the files is created
CURRENT_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
             # WE WAnt create the file name
LOG_FILE_NAME=F"log_{CURRENT_TIME_STAMP}.log"
             #to create the directoruy use import os ,exist_ok=True it for create the  folder which is not exist tpo check the folder is not aavaible and then create new
os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)
                                         #pressF12 we more information
logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
#format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
format='%(asctime)s %(message)s',
level=logging.INFO

)