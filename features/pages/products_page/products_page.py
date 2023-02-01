from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.utils.product import Product


class ProductsPage:
    def __init__(self, context):
        self.context = context
        self.item_name_locator = 'inventory_item_name'
        self.item_desc_locator = 'inventory_item_desc'
        self.item_price_locator = 'inventory_item_price'

    def get_all_item_titles_on_page(self):
        WebDriverWait(self.context.browser, 10).until(EC.visibility_of_all_elements_located(
            (By.CLASS_NAME, self.item_name_locator)))
        title_elements = self.context.browser.find_elements(By.CLASS_NAME, self.item_name_locator)
        title_strings = []
        for title in title_elements:
            title_strings.append(title.text)
        return title_strings

    def get_all_item_desc_on_page(self):
        WebDriverWait(self.context.browser, 10).until(EC.visibility_of_all_elements_located(
            (By.CLASS_NAME, self.item_name_locator)))
        desc_elements = self.context.browser.find_elements(By.CLASS_NAME, self.item_desc_locator)
        desc_strings = []
        for desc in desc_elements:
            desc_strings.append(desc.text)
        return desc_strings

    def get_all_item_prices_on_page(self):
        WebDriverWait(self.context.browser, 10).until(EC.visibility_of_all_elements_located(
            (By.CLASS_NAME, self.item_name_locator)))
        price_elements = self.context.browser.find_elements(By.CLASS_NAME, self.item_price_locator)
        price_strings = []
        for price in price_elements:
            price_strings.append(price.text)
        return price_strings

    def validate_product_titles_on_page(self, product):
        titles_list = self.get_all_item_titles_on_page()
        product = Product(self.context, product)
        return product.get_product_title() in titles_list

    def validate_product_desc_on_page(self, product):
        desc_list = self.get_all_item_desc_on_page()
        product = Product(self.context, product)
        return product.get_product_desc() in desc_list

    def validate_product_prices_on_page(self, product):
        price_list = self.get_all_item_prices_on_page()
        product = Product(self.context, product)
        return product.get_product_price() in price_list

    def validate_product_cart_btn_on_page(self, product):
        product = Product(self.context, product)
        add_to_cart_btn = self.context.browser.find_elements(By.ID, product.cart_btn_id)
        return len(add_to_cart_btn) == 1
