from housing.pipeline.pipeline import pipeline
from housing.exception import HousingException
from housing.logger import logging

def main():

    try:

        pipeline=pipeline
        pipeline=run_pieline()

    
        logging.info("main function execution completed.")
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=='__main__':
    main()