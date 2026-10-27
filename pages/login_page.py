import dotenv

loaded = dotenv.load_dotenv(".env.logincredentials")

def test_login(page):
    page.goto("/sign-in")
    page.get_by_test_id("add-email-address").fill(loaded["VALID_USER_EMAIL"])
    page.get_by_test_id("login-password").fill("Test@1234")
    page.get_by_test_id("login-submit").click()
    expect(page.get_by_test_id("user-menu")).to_be_visible()