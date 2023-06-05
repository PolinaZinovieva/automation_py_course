from selenium.webdriver import Chrome, Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

def test_01():
    # test 1
    driver = Chrome("Homework_22/chromedriver.exe")
    driver.get("https://www.google.com/maps/")
    # driver.implicitly_wait(5)
    web_driver_wait = WebDriverWait(driver, 10)
    search_input_field_locator = '//*[@id="searchboxinput"]'
    search_input_field= web_driver_wait.until(EC.presence_of_element_located(('xpath', search_input_field_locator)))
    # search_input_field = driver.find_element(
    #     by="xpath", value=search_input_field_locator
    search_input_field.click()
    search_input_field.send_keys("Glinki street 2, Dnipro")
    search_input_field.send_keys(Keys.ENTER)