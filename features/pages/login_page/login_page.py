from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, context):
        self.context = context
        self.username_locator = 'user-name'
        self.password_locator = 'password'
        self.login_btn_locator = 'login-button'
        self.error_text_locator = 'h3[data-test="error"]'
        self.lock_error_string = 'Epic sadface: Sorry, this user has been locked out.'
        self.menu_btn_locator = 'react-burger-menu-btn'
        self.logout_btn_locator = 'logout_sidebar_link'
        self.username_error_string = 'Epic sadface: Username is required'
        self.password_error_string = 'Epic sadface: Password is required'
        self.invalid_cred_string = 'Epic sadface: Username and password do not match any user in this service'
        self.clear_error_btn_locator = 'error-button'

    def set_login_vals(self, user_type):
        user = self.context.yaml_utils.get_user_info(user_type)
        self.context.browser.find_element(By.ID, self.username_locator).send_keys(user['username'])
        self.context.browser.find_element(By.ID, self.password_locator).send_keys(user['password'])

    def submit_login(self):
        self.context.browser.find_element(By.ID, self.login_btn_locator).click()

    def match_error_text(self, error_type):
        text = self.context.browser.find_element(By.CSS_SELECTOR, self.error_text_locator).text
        return text == self.get_error_string(error_type)

    def clear_error_msg(self, error_type):
        self.context.browser.find_element(By.CLASS_NAME, self.clear_error_btn_locator).click()
        return self.get_error_string(error_type) in self.context.browser.page_source

    def logout(self):
        WebDriverWait(self.context.browser, 9).until(EC.element_to_be_clickable((By.ID, self.menu_btn_locator))).click()
        WebDriverWait(self.context.browser, 10).until(EC.element_to_be_clickable(
            (By.ID, self.logout_btn_locator))).click()

    def get_error_string(self, error_type):
        expected_string = ''
        match error_type:
            case 'locked_out':
                expected_string = self.lock_error_string
            case 'empty_login':
                expected_string = self.username_error_string
            case 'empty_username':
                expected_string = self.username_error_string
            case 'empty_password':
                expected_string = self.password_error_string
            case 'invalid_username':
                expected_string = self.invalid_cred_string
            case 'invalid_password':
                expected_string = self.invalid_cred_string

        return expected_string
