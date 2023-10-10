import sys

from behave import fixture, use_fixture
import os
from dotenv import load_dotenv

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.abspath(os.path.join(current, '../..'))
sys.path.append(parent)

import pages.home_page.home_page as hp
import pages.login_page.login_page as lp
import pages.notes_page.notes_page as np
from core_framework.core import Core
from core_framework.api.api import Api
import core_framework.driver.browser_methods as bm
import utils.yaml_utils as yaml_utils
import notes_api.utils.user_api as user_api
import notes_api.utils.data_utils as api_utils


@fixture
def load_helper_classes(context):
    context.base_api = Api()
    context.user_api = user_api.UserApi()
    context.browser_methods = bm.BrowserMethods(context)
    context.yaml_utils = yaml_utils.YamlUtils()
    context.api_utils = api_utils


@fixture
def config_test_browser(context):
    load_dotenv()
    browser_name = os.getenv('BROWSER')
    headless = os.getenv('HEADLESS')
    context.browser = Core().initialize_core(browser_name=browser_name, headless=headless)
    context.browser.maximize_window()
    yield context.browser
    context.browser.quit()


@fixture
def load_page_classes(context):
    context.home_page = hp.HomePage(context)
    context.login_page = lp.LoginPage(context)
    context.notes_page = np.NotesPage(context)


def before_all(context):
    use_fixture(config_test_browser, context)
    use_fixture(load_helper_classes, context)
    use_fixture(load_page_classes, context)


def after_scenario(context, scenario):
    # if 'ui' in scenario.tags:
    #     token = context.yaml_utils.get_user_token('ui')
    # else:
    token = context.yaml_utils.get_user_token()
    if 'delete_user' in scenario.tags:
        context.user_api.delete_user('delete', token, context.base_api)
    elif 'logout' in scenario.tags:
        resp = context.user_api.logout_user('logout', token, context.base_api)
    elif 'manual_logout' in scenario.tags:
        context.notes_page.click_logout_btn()

