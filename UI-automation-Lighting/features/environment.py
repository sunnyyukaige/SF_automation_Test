__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from PageModel.HomePage import HomePage
from features.accountManage import AccountManage
from PageModel.LoginPage import LoginPage
from PageModel.BUPage import BUPage
from Browser.Browser import Browser
from Browser.Browser import BrowserType
from Browser.BrowserManage import BrowserManage
from PageModel.ContentMapPage import ContenMapPage
from PageModel.OppPage import OppPage
from PageModel.QuotePage import QuotePage
from PageModel.CatalogPage import CatalogPage
import time


def before_scenario(context,scenario):
    #env_tag = context.config.userdata['env']
    #browser_tag=context.config.userdata['browser']
    # if you want to debug just uncomment below 2 lines and comment above 2 lines
    env_tag = 'qa'
    browser_tag='chrome'
    if "skip" in scenario.tags:
        scenario.skip("Marked with @skip, may be developing in progress or some reason")
        return
    if env_tag == 'qa':
        AccountManage()
    else:
        AccountManage('staging')
    context.browserManager = BrowserManage()
    if browser_tag=='appium':
        browser_setting = BrowserType.APPIUM
        context.browserManager.add_browser_queue( Browser(browser_setting, command_executor='http://127.0.0.1:4723/wd/hub',
                                         desired_capabilities={
                                             'platformName': 'iOS',
                                             'platformVersion': '11.2',
                                             'deviceName': 'iPad Air',
                                             'browserName': "Safari"
                                         }))
    else:
        browser_setting = BrowserType.CHROME
        context.browserManager.add_browser_queue(Browser(browser_type=browser_setting))
    context.browser = context.browserManager.get_browser()
    #context.browser.maximize_window()
    context.browser.open(AccountManage.url)
    _init_page(context)


def after_scenario(context, scenario):
    if "skip" in scenario.tags:
        return
    if scenario.status == "failed":
        logtime =scenario.name+ time.strftime('_%y%m%d%H%M', time.localtime(time.time())) + ".png"
        path = "./Result/"
        context.browser.get_screenshot_as_file(path + logtime)
    context.browser.quit()
    context.browserManager.clear_browsers()


def _init_page(context):
    context.basePage = BasePage(context.browser)
    context.homePage = HomePage(context.browser)
    context.loginPage = LoginPage(context.browser)
    context.buPage = BUPage(context.browser)
    context.contentmapPage = ContenMapPage(context.browser)
    context.oppPage = OppPage(context.browser)
    context.quotePage = QuotePage(context.browser)
    context.catalogPage = CatalogPage(context.browser)


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    pass
