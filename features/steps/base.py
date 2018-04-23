__author__ = 'sunny.yu2'
from behave import *
from features.accountManage import AccountManage


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


@then("i can open omni")
def step_impl(context):
    context.basePage.navigate_to(AccountManage.url)


@then("I can switch-to-lightning module")
def step_impl(context):
    context.homePage.switch_to_lightning()


@when("I go to classical model")
def step_impl(context):
    context.homePage.switch_to_classical()


@when("I create opp")
def step_impl(context):
    context.homePage.gotoOpp()
    context.oppPage.creat_new_button()
    context.oppPage.fill_oppName()
    context.oppPage.fillBU()
    context.oppPage.fillCenter()
    context.oppPage.search_by_icon('Account Name')

