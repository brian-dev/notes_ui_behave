from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, context):
        self.context = context

    def set_login_vals(self, user_type):
        user = self.context.yaml_utils.get_user_info(user_type)
        username_input = self.context.browser.find_element(By.ID, 'user-name')
        password_input = self.context.browser.find_element(By.ID, 'password')

        username_input.send_keys(user['username'])
        password_input.send_keys(user['password'])

    def submit_login(self):
        login_btn = self.context.browser.find_element(By.ID, 'login-button')
        self.context.browser_methods.click(login_btn)