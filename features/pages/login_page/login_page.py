from notes_ui_behave.features.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, context):
        self.context = context
        self.email_input_id_loc = 'email'
        self.password_input_id_loc = 'password'
        self.login_btn_css_loc = 'button[data-testid="login-submit"]'
        self.email_error_class_loc = 'invalid-feedback'
        self.email_required_str = 'Email address is required'
        self.invalid_address_str = 'Email address is invalid'

    def set_login_vals(self, user_type):
        if user_type == 'active_user':
            user = self.context.yaml_utils.get_user_info()
            email_str = user['data']['email']
            pass_str = 'password'
        else:
            user = self.context.yaml_utils.get_test_creds(user_type)
            email_str = user['email']
            pass_str = user['pass']

        self.input_text(self.find_by_id(self.email_input_id_loc), email_str)
        self.input_text(self.find_by_id(self.password_input_id_loc), pass_str)

    def submit_login(self):
        self.click(self.find_by_css(self.login_btn_css_loc))

    def match_error_text(self, error_type):
        text = self.find_by_class(self.email_error_class_loc).text
        return text == self.get_error_string(error_type)

    def get_error_string(self, error_type):
        expected_string = ''
        match error_type:
            case 'email_required':
                expected_string = self.email_required_str
            case 'invalid_address':
                expected_string = self.invalid_address_str

        return expected_string
