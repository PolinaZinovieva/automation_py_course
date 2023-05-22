from selenium.webdriver import Chrome, Keys


def test_01():
    # test 1
    driver = Chrome("Package2/lesson_sel/drivers/chromedriver.exe")
    driver.get("https://www.google.com/maps/")

    search_input_field_locator = '//*[@id="searchboxinput"]'
    search_input_field = driver.find_element(
        by="xpath", value=search_input_field_locator
    )
    search_input_field.click()
    search_input_field.send_keys("Glinki street 2, Dnipro")
    search_input_field.send_keys(Keys.ENTER)

    # test 2
    search_input_field = driver.find_element(
        by="xpath", value=search_input_field_locator
    )
    search_input_field.click()
    search_locator = '//*[@id="searchbox-searchbutton"]'
    search_button = driver.find_element(by="xpath", value=search_locator)
    search_button.click()
    driver.implicitly_wait(10)

    # test 3
    article_button_selector = '//*[@role="article" ]'
    artcl = driver.find_element(by="xpath", value=article_button_selector)
    artcl.click()

    # test 4
    directions_selector = '//*[@aria-label="Directions to Dnipro"]'
    dir_button = driver.find_element(by="xpath", value=directions_selector)
    dir_button.click()

    # test 5
    start_input_selector = '//*[@aria-label="Starting point Your location"]'
    start_direction_button = driver.find_element(by="xpath", value=start_input_selector)
    start_direction_button.click()
    start_direction_button.send_keys("Kyiv")
    start_direction_button.send_keys(Keys.ENTER)

    # search_input_field.send_keys(Keys.DELETE)
    # time.sleep(60)

    #
    # driver.maximize_window()
    # # time.sleep(60)
    # # first_non_ad_link = driver.find_element(by='xpath', value=first_non_ad_link_locator)
    # # first_non_ad_link.click()
    # # driver.quit()
    # item_locator = '//*[@href="/sale/ona"]'
    # click_item = driver.find_element(by ='xpath', value=item_locator)
    # click_item.click()
    # driver.back()
    # search_input_field = driver.find_element(by='xpath', value=search_input_field_locator)
    # search_input_field.send_keys(Keys.DELETE)
    # time.sleep(10)
