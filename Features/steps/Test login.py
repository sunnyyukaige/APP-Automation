from behave import *
from PageModel.LoginPage import LoginPage
from PageModel.HomePage import HomePage

use_step_matcher("re")


@given("I click login on EFP app login page")
def step_impl(context):
    context.loginPage.GotoLogin(context.platform)



@when("I input (?P<Username>.+) and (?P<Password>.+) with login")
def step_impl(context, Username, Password):
    context.loginPage.SwitchToWeb()
    context.loginPage.Login(Username, Password, context.platform)
    context.loginPage.SwitchBack()

@then("I can go to Home page")
def step_impl(context):
    assert (context.homePage.HomeTitle(context.platform).text=='Home')


@when("I input (?P<Username>.+) and (?P<Password>.+) with login android app")
def step_impl(context, Username, Password):
    #context.loginPage.SwitchToWeb()
    context.loginPage.Login(Username, Password, context.platform)
    #context.loginPage.SwitchBack()


@then("I logout")
def step_impl(context):
    context.homePage.logout()