__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from WebElement.By import By
import time


class LoginPage(BasePage):

  # def __init__(self):
  #     super(self).__init__()

    def InputUserName(self,value,plateform=None):
        if(plateform=='ios'):
            element=self.browser.find_element(By.ID,'MobileNumberOrUsername')
            element.click()
            element.send_keys(value)
        else:
            element=self.browser.find_element(By.ID, 'MobileNumberOrUsername')
            element.send_keys(value)



    def InputPassWord(self,value,plateform=None):
        if(plateform=='ios'):

            element=self.browser.find_element(By.NAME,'Password')
            element.click()
            element.send_keys(value)
        else:
            element=self.browser.find_element(By.ID, 'Password')
            element.send_keys(value)



    def Submit(self,plateform=None):
        if(plateform=='ios'):
            elements=self.browser.find_elements(By.TAG_NAME,'Button')
            elements[1].click()
        else:
            elements=self.browser.find_elements(By.CLASS_NAME, 'android.widget.Button')
            elements[1].click()


    def Login(self,name,psw,plateform=None):
        self.InputUserName(name,plateform)
        self.InputPassWord(psw,plateform)
        self.Submit(plateform)

    def GotoLogin(self,plateform=None):
        if(plateform=='ios'):
            self.NotificationAcc()
            self.browser.find_element(By.NAME,'Login').click()
            self.NotificationAcc()
        else:
            self.browser.find_element(By.ID, 'com.ef.efp:id/btn_login').click()

    def NotificationAcc(self):
        time.sleep(1)
        self.browser.wait_for_alert_present()
        self.browser.get_alert().accept()


    def SwitchToWeb(self):
        time.sleep(2)
        self.browser.switch_to_web()

    def SwitchBack(self):
        self.browser.switch_back()

