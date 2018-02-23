__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from WebElement.By import By
import time

class MessagePage(BasePage):

  # def __init__(self):
  #     super(self).__init__()

    def GotoGroup(self,plateform='ios'):
        if(plateform=='ios'):
            self.browser.find_element(By.XPATH,'//XCUIElementTypeCell').click()
        else:
            self.browser.find_element(By.ID,'com.ef.efp:id/rl_content').click()

    def SendMessage(self,plateform=None):
        if (plateform == 'ios'):
            el1 = self.browser.find_element(By.NAME,"icon toolview emotion normal")
            el1.click()
            el2 = self.browser.find_element(By.NAME,"emoji 02")
            el2.click()
            el3 = self.browser.find_element(By.NAME,"发送")
            el3.click()
            time.sleep(5)
        else:
            el1 = self.browser.find_element(By.ID, "com.ef.efp:id/emoji_button")
            el1.click()
            el2 = self.browser.find_element(By.ID, "com.ef.efp:id/imgEmoji")
            el2.click()
            el3 = self.browser.find_element(By.ID, "com.ef.efp:id/buttonSendMessage")
            el3.click()
            time.sleep(5)

    def Scroll_down(self):
        self.browser.scroll_down()

    def Alert(self,plateform=None):
       if(plateform=='ios'):
            self.browser.find_element(By.XPATH,'//UIAWindow[1]/UIAButton[2]').click()
       else:
            self.browser.is_alert_present()
            self.browser.find_element(By.ID,'android:id/button1').click()
