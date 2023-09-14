import logging

from .page import Page
from typing import Optional


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.email = "qa.ajax.app.automation@gmail.com"
        self.password = "qa_automation_password"

    def log_in(self, email: Optional[str] = None, password: Optional[str] = None):
        if email is None:
            email = self.email
        if password is None:
            password = self.password

        logger = logging.getLogger(__name__)
        logger.info(f"Started log_in function with {email}, {password}")

        button_log_in = self.find_elements(value="android.widget.FrameLayout", attr_value="com.ajaxsystems:id/authHelloLogin")
        if button_log_in is None:
            logger.error("Starting button_log_in not found.")
            return False
        self.tap_element(button_log_in)

        credents_boxes = self.find_elements('android.widget.EditText')
        if credents_boxes is None:
            logger.error("Credentials boxes not found.")
            return False
        self.tap_element(credents_boxes[0])
        self.enter_text(email, credents_boxes[0])
        self.tap_element(credents_boxes[1])
        self.enter_text(password, credents_boxes[1])

        eye_icon = self.find_elements(value="android.view.View", attr_value="iconPassword")
        if eye_icon is not None:
            self.tap_element(eye_icon)
        else:
            logger.error("Eye_icon not found.")
            return False
        if not credents_boxes[0].text == email and credents_boxes[1].text == password:
            logger.error("Credentials boxes values do not equal the desired ones.")
            return False

        button_log_in = self.find_elements(value="androidx.compose.ui.platform.ComposeView", attr_value="com.ajaxsystems:id/compose_view")
        if button_log_in is None:
            logger.error("Ending button_log_in not found.")
            return False
        self.tap_element(button_log_in)

        snackbar_text = self.catch_snackbar()
        if snackbar_text is None:
            return None
        else:
            return snackbar_text

