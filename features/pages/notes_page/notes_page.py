from notes_ui_behave.features.pages.base_page import BasePage


class NotesPage(BasePage):
    def __init__(self, context):
        self.context = context
        self.logout_btn_css_loc = 'button[data-testid="logout"]'

    def click_logout_btn(self):
        logout_btn = self.find_by_css(self.logout_btn_css_loc)
        self.click(logout_btn)
