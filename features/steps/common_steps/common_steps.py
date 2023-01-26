from behave import *
from hamcrest import assert_that, equal_to


@step('the user is on the "{page}" page')
def step_impl(context, page):
    url = context.yaml_utils.get_env_urls()
    context.browser_methods.goto(url[page])


@step('the user is directed to the "{page}" url')
def step_impl(context, page):
    urls = context.browser_methods.validate_url(page)
    assert_that(urls[0], equal_to(urls[1]))
