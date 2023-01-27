from behave import *


@step('the user logs in as the "{user_type}"')
def step_impl(context, user_type):
    context.login_page.set_login_vals(user_type)
    context.login_page.submit_login()
