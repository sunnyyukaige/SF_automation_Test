from behave import *
import time

use_step_matcher("re")


@when("I goto learning module")
def step_impl(context):
    context.homePage.gotoModule("Omni | Production | Learning")
    context.homePage.gotoLightTab("Content Maps")

@then("I can edit contentmap")
def step_impl(context):
    context.contentmapPage.addNew()
    context.contentmapPage.inputContentName('sunnytest')
    context.contentmapPage.selectContentMapVersion('001')
