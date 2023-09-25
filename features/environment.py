import sys

from behave import fixture, use_fixture
import os
from dotenv import load_dotenv

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.abspath(os.path.join(current, '../..'))
print(f"************{current}")
print(f"*************{parent}")
sys.path.append(parent)

import pages.login_page.login_page as lp
import pages.products_page.products_page as prod_page
from core_framework.core import Core
import core_framework.driver.browser_methods as bm
import utils.yaml_utils as yaml_utils


@fixture
def load_helper_classes(context):
    context.browser_methods = bm.BrowserMethods(context)
    context.yaml_utils = yaml_utils.YamlUtils()


@fixture
def config_test_browser(context):
    load_dotenv()
    browser_name = os.getenv('BROWSER')
    headless = os.getenv('HEADLESS')
    context.browser = Core().initialize_core(browser_name=browser_name, headless=headless)
    print(context.browser)
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
