from selenium.webdriver.common.by import By
from features.utils.product import Product


class ProductsPage:
    def __init__(self, context):
        self.context = context
        self.item_name_locator = 'inventory_item_name'
        self.item_desc_locator = 'inventory_item_desc'
        self.item_price_locator = 'inventory_item_price'

    def get_all_item_titles_on_page(self):
        self.context.browser_methods.wait_until_visible('class', self.item_name_locator)

        title_elements = self.context.browser.find_elements(By.CLASS_NAME, self.item_name_locator)
        title_strings = []
        for title in title_elements:
            title_strings.append(title.text)
        return title_strings

    def get_all_item_desc_on_page(self):
        self.context.browser_methods.wait_until_visible('class', self.item_name_locator)

        desc_elements = self.context.browser.find_elements(By.CLASS_NAME, self.item_desc_locator)
        desc_strings = []
        for desc in desc_elements:
            desc_strings.append(desc.text)
        return desc_strings

    def get_all_item_prices_on_page(self):
        self.context.browser_methods.wait_until_visible('class', self.item_name_locator)

        price_elements = self.context.browser.find_elements(By.CLASS_NAME, self.item_price_locator)
        price_strings = []
        for price in price_elements:
            price_strings.append(price.text)
        return price_strings

    def validate_product_elements(self, product, elements):
        product = Product(self.context, product)

        match elements:
            case 'title':
                titles_list = self.get_all_item_titles_on_page()
                return product.get_product_title() in titles_list
            case 'description':
                desc_list = self.get_all_item_desc_on_page()
                return product.get_product_desc() in desc_list
            case 'price':
                price_list = self.get_all_item_prices_on_page()
                return product.get_product_price() in price_list
            case 'add_to_cart_btn':
                add_to_cart_btn = self.context.browser.find_elements(By.ID, product.cart_btn_id)
                return len(add_to_cart_btn) == 1

