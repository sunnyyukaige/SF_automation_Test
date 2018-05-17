__author__ = 'sunny.yu2'
from behave import *
from features.accountManage import AccountManage
import time


@given('I am a admin')
def step_impl(context):
    context.loginPage.username(AccountManage.username)
    context.loginPage.password(AccountManage.password)
    context.loginPage.signIn()


@when('load some "{text}" arguments')
def step_impl(context, text):
    if (text == 'qa'):
        AccountManage()
    else:
        AccountManage('staging')

@then("I can go to Group tab")
def step_impl(context):
    context.homePage.selectTab('Groups')
    time.sleep(20)


@then('I can go to "{Opportunities}" tab')
def step_impl(context,Opportunities):
    context.homePage.selectTab(Opportunities)
    time.sleep(20)