import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


@pytest.fixture(autouse=True)
def setup():
    chrome_service = Service(
        ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()
    )

    chrome_options = Options()
    options = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
    ]
    for option in options:
        chrome_options.add_argument(option)

    return options
