import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.realpath(__file__), '/home/ali/PycharmProjects/EmailBot')))
from Email.dependencies.Locators import Locators
class Login():
    @staticmethod
    def login(driver):
        driver.maximize_window()
        driver.get("https://webmail.iinet.net.au")
        time.sleep(3)
        email = driver.find_element_by_id(Locators.login_email_id)
        email.send_keys('janb1@iinet.net.au')
        time.sleep(1)
        password = driver.find_element_by_id(Locators.login_password_id)
        password.send_keys('9a9il9pty')
        time.sleep(1)
        print('email password inserted')
        driver.find_element_by_class_name(Locators.login_btn_class_name).click()
        print('button clicked')
        time.sleep(10)
