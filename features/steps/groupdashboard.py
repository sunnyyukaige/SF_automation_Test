from behave import *
import time

@then("I can go to home page")
def step_impl(context):
    context.homePage.checkThisisHomePage()


@then("I can go to BU page")
def step_impl(context):
    context.homePage.gotoBU()


@then('I can view the "China Franchise" BU')
def step_impl(context):
    context.buPage.checkBUname('China Franchise')


@step('I can search and view "China Franchise" BU')
def step_impl(context):
    context.buPage.searchBU()
    context.buPage.selectBU()


@then("I can go to home page and {tab} tab")
def step_impl(context, tab):
    context.homePage.checkThisisHomePage()
    context.homePage.gotoTab(tab)


@step('I can edit the "China Franchise" BU')
def step_impl(context):
    context.buPage.clickEdit()
    context.buPage.selectMarketName("Indonesia")
    context.buPage.selectBusinessLineName("Own")
    context.buPage.setBusinessUnitName("sunny")
    context.buPage.setBusinessUnitCode("MCN.EFP")

    time.sleep(30)
