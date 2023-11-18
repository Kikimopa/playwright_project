from locators.base_locators import BaseLocators

class BasePage():
    def __init__(self, page):
        self.page = page

    def open_page(self, url):
        self.page.goto(url)


    def is_desired_page(self):
        logo = self.page.locator(BaseLocators.LOGO)
        if logo:
            return True
        else: return False
