import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying Home page title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****** Home page Title is passed *******")

        else:
            self.driver.save_screenshot("./Screenshots/test1_homePageTitle.png")
            self.driver.close()
            self.logger.info("****** Home page Title is failed *******")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******* Verifying Login Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("****** Login Test is passed *******")
        else:

            self.driver.save_screenshot("./Screenshots/test1_login.png")
            self.driver.close()
            assert False
            self.logger.info("****** Login Test is failed *******")