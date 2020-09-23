import configparser

# Raw config parser is a class and config is an object of that class. Main use of this class is to read data fron config file.
config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        URL = config.get('common info', 'baseURL')
        return URL

    @staticmethod
    def getUserEmail():
        useremail = config.get('common info', 'useremail')
        return useremail

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password