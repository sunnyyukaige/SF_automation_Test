from behave import *

use_step_matcher("re")


@when("I goto learning module")
def step_impl(context):
    context.homePage.goto_module("Omni | Production | Learning")
    context.homePage.goto_tab_lighting("Content Maps")

@then("I can edit contentmap")
def step_impl(context):
    context.contentmapPage.addNew()
    context.contentmapPage.inputContentName('sunnytest')
    context.contentmapPage.selectContentMapVersion('001')
