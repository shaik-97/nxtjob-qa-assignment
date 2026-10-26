import re
from playwright.sync_api import expect
from playwright.sync_api import sync_playwright

def test_search_google_title(page):
    page.wait_for_timeout = 10000
    page.goto("https://google.com")
    try:
        page.get_by_role("button", name="Accept All").click(timeout=3000)
    except:
        print("No cookie banner found")
    page.get_by_role("combobox",name="search").fill("Playwright Python")
    page.keyboard.press("Enter")
    page.wait_for_timeout = 3000
    expect(page).to_have_title(re.compile("Playwright Python", re.IGNORECASE))