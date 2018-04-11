__author__ = 'sunny.yu2'
from behave import *
from features.accountManage import AccountManage

@given('I am a admin')
def step_impl(context):
	context.loginPage.userName(AccountManage.userName)
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
	context.basePage.Navigate_To(AccountManage.url)


@then("I can switch-to-lightning module")
def step_impl(context):
	context.homePage.switch_to_lightning()