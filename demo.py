# from src.logger import logging

# logging.debug("This is debug message")
# logging.critical("lun t vjooo")
import logging

logging.getLogger("pymongo").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)


# below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e


from src.pipeline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()

