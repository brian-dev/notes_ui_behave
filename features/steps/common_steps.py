import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.abspath(os.path.join(current, '../..'))
sys.path.append(parent)
import time

from behave import *
from hamcrest import assert_that, equal_to


@step('the user is on the {page} page')
def step_impl(context, page):
    url = context.yaml_utils.get_env_urls()
    if page == 'base_url' or page == 'home':
        context.browser_methods.goto(url['base_url'])
    else:
        context.browser_methods.goto(url['base_url'] + url[page])

@step('the user is directed to the "{page}" url')
def step_impl(context, page):
    # Add static wait to give time for URL to update
    time.sleep(1)
    urls = context.browser_methods.validate_url(page)
    assert_that(urls[0], equal_to(urls[1]))


@step('a user has been created')
def step_impl(context):
    payload = context.api_utils.generate_user_payload()
    user_info = context.user_api.register_new_user('register', payload, context.base_api)
    context.yaml_utils.write_to_json('users.json', user_info)


@step('the user is logged in')
def step_impl(context):
    user_data = context.yaml_utils.get_user_info()
    user_creds = {
        'email': user_data['data']['email'],
        'password': 'password'
    }
    resp = context.user_api.login_user('login', user_creds, context.base_api)
    context.yaml_utils.write_to_json('active_user.json', resp['data'])
