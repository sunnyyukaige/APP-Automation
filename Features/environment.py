from Features.steps.BaseCaseIOS import BaseCaseIOS
from Features.steps.BaseCase import BaseCase
from PageModel.MessagePage import MessagePage
from PageModel.HomePage import HomePage
from PageModel.LoginPage import LoginPage


def before_scenario(context,scenario):
    context.tag=scenario.tags[0]
    init_Pages(context)

def after_scenario(context,scenario):
    context.base.tearDown()

def init_Pages(context):
    if(context.tag=='ios'):
        context.base = BaseCaseIOS()
        context.base.setUp()
        context.platform='ios'
    else:
        context.base = BaseCase()
        context.base.setUp()
        context.platform='android'
    context.messagePage=MessagePage()
    context.homePage=HomePage()
    context.loginPage=LoginPage()
