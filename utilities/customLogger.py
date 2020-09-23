# import logging
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename="/home/appventurez/PycharmProjects/NopCommerce/Logs/automation.log",
#                             format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger=logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger
import logging
from datetime import datetime
class LogGen:
    # LOG_FILENAME = "logfile.log"
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename="./Logs/automation.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger("test_login")
        logger.setLevel(logging.INFO)
        # logging.info('Forecastiong Job Started...')
        # logging.debug('abc method started...')
       # LOG_FILENAME = datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log')
        return logger

