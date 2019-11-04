import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
from selenium.webdriver.support.wait import WebDriverWait
sys.path.insert(0, os.path.abspath(os.path.join(os.path.realpath(__file__), '/home/ali/PycharmProjects/EmailBot')))
from Email.dependencies.Locators import Locators

class Reply():
    @staticmethod
    def Replies(driver, values, subject):
        length = len(values)
        print(length)
        r = length/5
        mod = length%5
        if mod > 0:
            r = r+1
        rng = int(r)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//*[@id="folder_sent"]/a'))).click()
        element = driver.find_element_by_xpath('//*[@id="folder_sent"]/a').click()
        # element.click()
        time.sleep(3)
        y=0
        print(rng)
        for x in range(rng):
            table_body = driver.find_element_by_xpath('//*[@id="messageListTable"]/tbody')
            tag_name = table_body.find_element_by_tag_name("tr")
            idtr = (tag_name.get_attribute('id'))
            print('id is ' + idtr)
            tag_name.click()
            time.sleep(3)
            messageIframe = driver.find_element_by_class_name('messageIframe')
            driver.switch_to.frame(messageIframe)
            body = driver.find_element_by_xpath('/html/body')
            body.click()
            time.sleep(2)
            body.send_keys(Keys.CONTROL + "a")
            body.send_keys(Keys.CONTROL + "c")
            time.sleep(2)
            driver.switch_to.default_content()
            driver.find_element_by_xpath('//*[@id="action_reply_all"]/a').click()
            time.sleep(3)
            driver.switch_to.frame(1)
            body = driver.find_element_by_xpath('/html/body')
            body.send_keys(Keys.TAB)
            body.send_keys(Keys.ENTER * 2)
            body.send_keys(Keys.CONTROL + "v")
            time.sleep(3)
            driver.switch_to.default_content()
            add_bcc = driver.find_element_by_id('addBcc')
            add_bcc.click()
            time.sleep(1)
            bcc_email = driver.find_element_by_xpath('//*[@id="form_bcc"]/div/ul/li/input')
            y=0
            print('yello')
            while values:
                y=y+1
                print(y)
                if y == 6:
                    break
                else:
                    bcc_email.send_keys(values.pop(-1) + Keys.ENTER)
            edit_subject = driver.find_element_by_id('editSubject')
            edit_subject.click()
            subject_input = driver.find_element_by_id('emailSubject')
            subject_input.send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE)
            subject_input.send_keys(subject)
            driver.find_element_by_partial_link_text('Send my').click()
            time.sleep(3)