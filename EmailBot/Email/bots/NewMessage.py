import time
from selenium.webdriver.common.keys import Keys
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.realpath(__file__), '/home/ali/PycharmProjects/EmailBot')))


class NewMessage():
    @staticmethod
    def newMessage(driver):
        driver.find_element_by_class_name('arrow').click()
        print('arrow click')
        time.sleep(5)
        driver.find_element_by_id('newEmailButton').click()
        print('new email button clicked')
        time.sleep(6)
        email = driver.find_element_by_class_name('textboxlist-bit-editable-input')
        time.sleep(2)
        email.send_keys('ali8934120@gmail.com')
        print('email filled')
        time.sleep(3)
        subject = driver.find_element_by_id('emailSubject')
        subject.send_keys('Automated robot')
        print('subject filled')
        time.sleep(3)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        body = driver.find_element_by_xpath('/html/body')
        body.send_keys('Email for test Automated Robot ')
        driver.switch_to.default_content()
        print('body filled')
        time.sleep(3)
        send_email = driver.find_element_by_id('topRightSendButton')
        send_email.click()
        print('email sent')
        time.sleep(4)

