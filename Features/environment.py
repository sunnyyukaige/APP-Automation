import behave
from Features.steps.BaseCaseIOS import BaseCaseIOS
from Features.steps.BaseCase import BaseCase

def before_scenario(context,scenario):
    if(scenario.tags[0]=='ios'):
        context.base = BaseCaseIOS()
        context.base.setUp()
        context.platform='ios'
    else:
        context.base = BaseCase()
        context.base.setUp()
        context.platform='android'

def after_scenario(context,scenario):
    context.base.tearDown()