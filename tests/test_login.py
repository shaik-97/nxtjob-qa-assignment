import pytest

pytestmark = pytest.mark.no_auth


@pytest.mark.smoke
def test_valid_login(login_page, users):
    login_page.open()
    login_page.login(users["valid_user"]["email"], users["valid_user"]["password"])
    login_page.verify_logged_in()


def test_invalid_password(login_page, users):
    login_page.open()
    login_page.login(users["invalid_user"]["email"], users["invalid_user"]["password"])
    login_page.verify_error("Invalid")
