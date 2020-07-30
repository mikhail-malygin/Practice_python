import math
from selenium import webdriver
import time

link_website = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link_website)

    number = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link_number = browser.find_element_by_link_text(number)
    link_number.click()

    input_first_name = browser.find_element_by_tag_name("input")
    input_first_name.send_keys("Mikhail")
    input_last_name = browser.find_element_by_name("last_name")
    input_last_name.send_keys("Malygin")
    input_city = browser.find_element_by_class_name("city")
    input_city.send_keys("Ekaterinburg")
    input_country = browser.find_element_by_id("country")
    input_country.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

