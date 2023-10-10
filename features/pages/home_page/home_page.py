from notes_ui_behave.features.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, context):
        self.context = context
        self.login_btn_css_loc = 'a[href="/notes/app/login"]'
        self.create_acct_btn_css_loc = 'a[data-testid="open-register-view"]'
        self.google_acct_btn_css_loc = 'a[data-testid="use-google-account"]'
        self.forgot_pass_btn_css_loc = 'a[data-testid="forgot-password-view"]'
        self.home_title_class_loc = 'lh-1'
        self.home_title_str = 'Welcome to Notes App'
        self.practice_breadcrumb_css_loc = 'a[href="/"]'
        self.practice_breadcrumb_str = 'Practice'
        self.home_breadcrumb_css_loc = 'a[href="/notes/app/"]'
        self.home_breadcrumb_str = 'Home - My Notes'

    def home_element_displayed(self, name, locator):
        return self.element_is_displayed(name, locator, vars(self))

    def click_home_btn(self, btn):
        match btn:
            case 'login':
                btn = self.find_by_css(self.login_btn_css_loc)
            case 'create_account':
                btn = self.find_by_css(self.create_acct_btn_css_loc)

        self.click(btn)

