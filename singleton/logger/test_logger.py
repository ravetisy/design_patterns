# import logger
# try:
#     a = 1 / 0
# except:
#     logger.error("something went wrong")
import os

from logger_class import Logger
logger_object = Logger(
    file_name=
    '/Users/rob/pycharm_projects/design_patterns/singleton/logger/filename'
)
logger_object.info('This is an info message')
logger_object.error('Critical error, exiting the application')
