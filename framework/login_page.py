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

        button_log_in = self.find_elements("//*[@text = 'Log In']")
        if button_log_in is None:
            return "ERROR at log_in(): starting button_log_in not found"
        self.tap_element(button_log_in[0])

        credents_boxes = self.find_elements('android.widget.EditText', "class name")
        if credents_boxes is None:
            return "ERROR at log_in(): credents_boxes not found"
        self.tap_element(credents_boxes[0])
        self.enter_text(email, credents_boxes[0])
        self.tap_element(credents_boxes[1])
        self.enter_text(password, credents_boxes[1])

        view_elements = self.find_elements("android.view.View", "class name")
        if view_elements is None:
            return "ERROR at log_in(): view_elements not found"
        eye_icon = None
        for element in view_elements:
            if element.get_attribute("resource-id") == "iconPassword":
                eye_icon = element
        if eye_icon is not None:
            self.tap_element(eye_icon)
        else:
            return "ERROR at log_in(): eye_icon not found"
        if not credents_boxes[0].text == email and credents_boxes[1].text == password:
            return "ERROR at log_in(): credents_boxes test values do not equal desired ones"

        button_log_in = self.find_elements("//*[@text = 'Log In']")
        if button_log_in is None:
            return "ERROR at log_in(): ending button_log_in not found"
        self.tap_element(button_log_in[0])

        textview_elements = self.find_elements("android.widget.TextView", "class name")
        if textview_elements is not None:
            for element in textview_elements:
                if element.get_attribute("resource-id") == "com.ajaxsystems:id/snackbar_text":
                    return "ERROR at log_in(): " + element.text

        return None
