import sys

from behave import fixture, use_fixture
import os
from dotenv import load_dotenv
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import pages.login_page.login_page as lp
import pages.products_page.products_page as prod_page
from core_framework.driver.browser import Browser
import core_framework.driver.browser_methods as browser_methods
import utils.yaml_utils as yaml_utils


@fixture
def load_helper_classes(context):
    context.browser_methods = browser_methods.BrowserMethods(context)
    context.yaml_utils = yaml_utils.YamlUtils()


@fixture
def config_test_browser(context):
    load_dotenv()
    browser_name = os.getenv('BROWSER')
    headless = os.getenv('HEADLESS')
    match browser_name:
        case 'chrome':
            context.browser = Browser(headless).chrome_browser()
        case 'firefox':
            context.browser = Browser(headless).firefox_browser()
        case 'brave':
            context.browser = Browser(headless).brave_browser()
    context.browser.maximize_window()
    yield context.browser
    context.browser.quit()


@fixture
def load_page_classes(context):
    context.login_page = lp.LoginPage(context)
    context.products_page = prod_page.ProductsPage(context)


def before_all(context):
    use_fixture(config_test_browser, context)
    use_fixture(load_helper_classes, context)
    use_fixture(load_page_classes, context)


def after_scenario(context, scenario):
    if 'logout' in scenario.tags:
        context.login_page.logout()
