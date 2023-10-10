from behave import *
from hamcrest import assert_that, equal_to


@step('the {name} is visible on page {locator}')
def step_impl(context, name, locator):
    is_visible = context.home_page.home_element_displayed(name, locator)
    assert is_visible is True


@step('the user clicks on the {btn} button')
def step_impl(context, btn):
    context.home_page.click_home_btn(btn)

