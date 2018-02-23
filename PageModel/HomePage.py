__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from WebElement.By import By
import time

class HomePage(BasePage):

  # def __init__(self):
  #     super(self).__init__()

    def HomeTitle(self,plateform=None):
        if(plateform=='ios'):
           element= self.browser.find_element(By.XPATH,'//XCUIElementTypeOther[@name="Home"]')
           return element
        else:
            element=self.browser.find_element(By.ID,'com.android.packageinstaller:id/permission_allow_button')
            element.click()
            element.click()
            element.click()
            element = self.browser.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Home"]/android.widget.ImageView')
            return element


    def GoToMessage(self,plateform=None):
        if (plateform == 'ios'):
            self.browser.find_element(By.XPATH,'//XCUIElementTypeButton[@name="Messages"]').click()
        else:
            self.browser.find_element(By.XPATH,'//android.widget.FrameLayout[@content-desc="Messages"]/android.widget.ImageView').click()

    def logout(self,plateform=None):
        if(plateform=='ios'):
            self.browser.find_element(By.NAME,'Logout')
        else:
            self.browser.find_element(By.ID,'com.ef.efp:id/btn_logout').click()