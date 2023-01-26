from behave import fixture, use_fixture
import os
from dotenv import load_dotenv
from features.pages.login_page.login_page import LoginPage
from features.pages.products_page.products_page import ProductsPage
from features.utils.browser import Browser
from features.utils.browser_methods import BrowserMethods
from features.utils.yaml_utils import YamlUtils


@fixture
def load_helper_classes(context):
    context.browser_methods = BrowserMethods(context)
    context.yaml_utils = YamlUtils()


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
    yield context.browser
    context.browser.maximize_window()
    context.browser.quit()


@fixture
def load_page_classes(context):
    context.login_page = LoginPage(context)
    context.products_page = ProductsPage(context)


def before_all(context):
    use_fixture(config_test_browser, context)
    use_fixture(load_helper_classes, context)
    use_fixture(load_page_classes, context)
