from selenium.webdriver.common.by import By


class BasePage:
    def __init(self, context):
        self.context = context

    def find_by_id(self, locator):
        element = self.context.browser.find_element(By.ID, locator)
        return element

    def find_by_css(self, locator):
        element = self.context.browser.find_element(By.CSS_SELECTOR, locator)
        return element

    def find_by_class(self, locator):
        element = self.context.browser.find_element(By.CLASS_NAME, locator)
        return element

    def element_is_displayed(self, name, locator, instance_vars):
        print(f"Fetching {name}")
        locator_val = self.fetch_element_def(locator, instance_vars)

        if 'css' in locator:
            return self.find_by_css(locator_val).is_displayed()
        elif 'class' in locator:
            return self.find_by_class(locator_val).is_displayed()
        else:
            return self.find_by_id(locator_val).is_displayed()

    def fetch_element_def(self, locator, instance_vars):
        for var in instance_vars:
            if locator == var:
                return vars(self)[var]

    def click(self, btn):
        btn.click()

    def input_text(self, locator, text):
        locator.send_keys(text)
