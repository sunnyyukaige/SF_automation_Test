from behave import *

use_step_matcher("re")
import time


@step("I goto opp and quote")
def step_impl(context):
    context.basePage.goto_url('https://english1--dev.cs57.my.salesforce.com/0060k000005vGWIAA2')
    context.oppPage.goto_quote()
    context.quotePage.gotoProduction()


@step("I can finish a quote")
def step_impl(context):
    context.quotePage.selectPrograme("Small Stars SSV2")
    context.quotePage.gotoConfig(0)
    context.quotePage.goValidate()
    context.quotePage.goPricing()
    context.quotePage.goFinialise()
    time.sleep(8)


@step("Check and delete quote")
def step_impl(context):
    context.basePage.goto_url('https://english1--dev.cs57.my.salesforce.com/0060k000005vGWIAA2')
    time.sleep(12)


