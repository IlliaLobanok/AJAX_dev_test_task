from .page import Page


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.email = "qa.ajax.app.automation@gmail.com"
        self.password = "qa_automation_password"

    def log_in(self):
        pass