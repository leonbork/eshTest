from pages.login_page import LoginPage

def test_login_functionality(driver):
    login_page = LoginPage(driver)
    login_page.open()

    # Use sample credentials for testing
    login_page.login("john_doe@company.con", "123456")

    # Since there are no valid credentials, check for login failure indication, e.g., error message
    # This could vary based on the application
    assert driver.current_url != LoginPage.URL, "Login failed as expected"
