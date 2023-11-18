import json
import time
from locators.base_locators import BaseLocators
from pages.base_page import BasePage
from pages.admin_page import AdminPage

def test_test1(page):
    page.goto("localhost:8000")
    page.locator("xpath=//*[@id='search']/input").type("Iphone10", delay=0.3)

    element = page.locator(BaseLocators.CURRENCY)
    assert element
    element.click()
    elem_list = page.locator(BaseLocators.CURRENCY_LIST).count()
    assert elem_list == 3


def test_test2(page):
    base_page = BasePage(page)
    base_page.open_page("localhost:8000")
    logo = base_page.is_desired_page()
    assert logo


def test_test3(page):
    admin_page = AdminPage(page)
    admin_page.open_admin_page()
    admin_page.submit_credantions()
    time.sleep(10)

def test_get_cookies(context):
    new_page = context.new_page()
    admin_page = AdminPage(new_page)
    admin_page.open_admin_page()
    admin_page.submit_credantions()
    cookies = context.cookies()
    with open("cookies.json", "w") as file:
        json.dump(cookies, file, indent=4)

def test_go_to_admin_page_without_fillin_cred(context):
    admin_page = AdminPage(context, cookies=True)
    admin_page.open_admin_page()
    time.sleep(10)
