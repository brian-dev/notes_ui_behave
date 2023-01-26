from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, context):
        self.context = context.browser
        self.find_element = self.context.find_element

    # def find_by_name(self, name):
    #     WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.NAME, name)))
    #     return self.find_element(By.NAME, name)

    # def find_by_css(self, css_val):
    #     WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_val)))
    #     return self.context.browser.find_element(By.CSS_SELECTOR, css_val)

    def find_by_id(self, id_val):
        WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.ID, id_val)))
        return self.find_element(By.ID, id_val)

    # def find_by_xpath(self, xpath):
    #     WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    #     return self.context.browser.find_element(By.XPATH, xpath)
    #
    # def find_elements_by_name(self, name):
    #     WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.NAME, name)))
    #     return self.context.browser.find_elements(By.NAME, name)
    #
    # def find_elements_by_css(self, css_val):
    #     WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_val)))
    #     return self.context.browser.find_elements(By.CSS_SELECTOR, css_val)
    #
    # def find_elements_by_id(self, id_val):
    #     WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.ID, id_val)))
    #     return self.context.browser.find_elements(By.ID, id_val)
