
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from Homework_22.homework22.pages.header_block import HeaderBlock
import pytest


@pytest.fixture(scope="session")
def driver():
    driver = Chrome("Homework_22/driver/chromedriver.exe")
    driver.get("https://www.epicgames.com/site/en-US/home")
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture
def header_block(driver):
    yield HeaderBlock(driver)


