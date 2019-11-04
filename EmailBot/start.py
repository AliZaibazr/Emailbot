import os
import sys
import datetime
from selenium import webdriver
sys.path.insert(0, os.path.abspath(os.path.join(os.path.realpath(__file__), '/home/ali/PycharmProjects/EmailBot')))
from Email.bots.Login import Login
from Email.bots.Replys import Reply
from Email.bots.NewMessage import NewMessage

class Start():
    @staticmethod
    def start(values,subject,host,port,end,msg):
        now = datetime.datetime.now()
        # values = ['ali8934120@gmail.com', 'alizaib.azr@gmail.com']
        if str(now) < end:
            print(msg)
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--proxy-server=socks://" + host + ":" + port)
            options.add_argument('--ignore-certificate-errors')
            options.add_argument("--test-type")
            options.add_argument("--start-maximized")
            options.add_argument("--auto-open-devtools-for-tabs")
            driver = webdriver.Chrome(executable_path="/home/ali/PycharmProjects/EmailBot/Email/drivers/chromedriver_linux64/chromedriver")
            Login.login(driver)
            Reply.Replies(driver, values,subject)

    # NewMessage.newMessage(driver)
