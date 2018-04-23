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


def before_scenario(context, scenario):
    tag = context.config.userdata['env']
    # if you want to debug just uncomment below line and comment above line
    # tag = 'staging'
    if tag == 'qa':
        AccountManage()
    else:
        AccountManage('staging')
    context.browserManager = BrowserManage()
    browser_setting = BrowserType.CHROME
    context.browserManager.add_browser_queue(Browser(browser_type=browser_setting))
    context.browser = context.browserManager.get_browser()
    context.browser.maximize_window()
    context.browser.open(AccountManage.url)
    _init_page(context)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        logtime = str(time.time()) + ".png"
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
