from behave import *
from PageModel.HomePage import HomePage
from PageModel.MessagePage import MessagePage

use_step_matcher("re")


@step("I can go to Message page")
def step_impl(context):
   context.homePage=HomePage()
   context.homePage.GoToMessage(context.platform)
   context.messagePage=MessagePage()
   context.messagePage.GotoGroup(context.platform)


@then("I can chat in group")
def step_impl(context):
   context.messagePage.SendMessage(context.platform)