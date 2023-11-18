import json
from pathlib import Path

from pages.base_page import BasePage
from locators.admin_locators import AdminLocators

class AdminPage(BasePage):
    def __init__(self, context, cookies: bool = None):
        if cookies:
            self.context = context.add_cookies(json.loads(Path("cookies.json").read_text()))
            self.page = context.new_page()
        else:
            self.context = context
            self.page = context.new_page()

    def open_admin_page(self):
        self.page.goto("http://localhost:8000/administration/index.php")

    def fill_user_name(self):
        self.page.get_by_placeholder("Username").fill("user")


    def fill_password(self):
        self.page.get_by_placeholder("Password").fill("bitnami")

    def submit_credantions(self):
        self.fill_user_name()
        self.fill_password()
        self.page.locator(AdminLocators.SUBMIT).click()

    def get_cookies(self):
        self.submit_credantions()
        with open("cookies.json", "w") as file:
            json.dump(self.context, file, indent=4)