import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IeService

def get_driver(browser):
    if browser == "chrome":
        chrome_service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # Start maximized for consistency
        return webdriver.Chrome(service=chrome_service, options=options)
    elif browser == "firefox":
        firefox_service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        return webdriver.Firefox(service=firefox_service, options=options)
    elif browser == "ie":
        ie_service = IeService(IEDriverManager().install())
        options = webdriver.IeOptions()
        return webdriver.Ie(service=ie_service, options=options)
    else:
        raise ValueError("Unsupported browser!")

@pytest.fixture(params=["chrome", "firefox", "ie"])
def driver(request):
    driver = get_driver(request.param)
    driver.maximize_window()
    yield driver
    driver.quit()
