import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = "./TestData/testdata.xlsx"


    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************ Test_002_DDT_Login")
        self.logger.info("******* Verifying Login Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'login_data')
        print("No of rows in an excel:-", self.rows)

        lst_status=[]   # Empty list variable


        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'login_data', r, 1)
            self.password = XLUtils.readData(self.path, 'login_data', r, 2)
            self.exp = XLUtils.readData(self.path, 'login_data', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="pass":
                    self.logger.info("**passed**")
                    self.lp.clickLogout()
                    lst_status.append("pass")
                elif self.exp=="Fail":
                    self.logger.info("**Failed**")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp=="pass":
                    self.logger.info("**failed**")

                    lst_status.append("fail")
                elif self.exp=="Fail":
                    self.logger.info("**passed**")
                    # self.lp.clickLogout()
                    lst_status.append("pass")

        if "Fail" not in lst_status:
            self.logger.info("*********Login DDT test passed*********")
            self.driver.close()
            assert True


        else:
            self.logger.info("*********Login DDT test failed*********")
            self.driver.close()
            assert False

        self.logger.info("******* End of login test *****")
        self.logger.info("******* Completed TC_002_LoginTestDDT *********")



