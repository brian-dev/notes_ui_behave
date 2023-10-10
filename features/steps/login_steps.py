import time

from behave import *
from hamcrest import assert_that, is_


@step('the user logs in as the "{user_type}" user')
def step_impl(context, user_type):
    # Set hard wait of 0.5 sec due to variable load times
    time.sleep(0.5)
    context.login_page.set_login_vals(user_type)
    context.login_page.submit_login()


@step('the user is is given a "{error_type}" error')
def step_impl(context, error_type):
    compare_val = context.login_page.match_error_text(error_type)
    assert_that(compare_val, is_(True))


@step('the user can clear the "{error_type}" error')
def step_impl(context, error_type):
    msg_present = context.login_page.clear_error_msg(error_type)
    assert_that(msg_present, is_(False))
