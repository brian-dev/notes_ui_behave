from behave import *
from hamcrest import assert_that, is_


@step('all "{product}" titles are listed on the page')
def step_impl(context, product):
    title_present = context.products_page.validate_product_elements(product, 'title')
    assert_that(title_present, is_(True))


@step('all "{product}" descriptions are listed on the page')
def step_impl(context, product):
    desc_present = context.products_page.validate_product_elements(product, 'description')
    assert_that(desc_present, is_(True))


@step('all "{product}" prices are listed on the page')
def step_impl(context, product):
    price_present = context.products_page.validate_product_elements(product, 'price')
    assert_that(price_present, is_(True))


@step('all "{product}" add to cart buttons are listed on the page')
def step_impl(context, product):
    btn_present = context.products_page.validate_product_elements(product, 'add_to_cart_btn')
    assert_that(btn_present, is_(True))
