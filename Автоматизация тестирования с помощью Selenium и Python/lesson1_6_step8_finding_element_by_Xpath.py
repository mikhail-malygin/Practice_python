from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element_by_xpath("//input")
    input_first_name.send_keys("Mikhail")
    input_last_name = browser.find_element_by_xpath("//input[@name='last_name']")
    input_last_name.send_keys("Malygin")
    input_city = browser.find_element_by_xpath("//form/div[3]//input")
    input_city.send_keys("Ekaterinburg")
    input_country = browser.find_element_by_xpath("//input[@id='country']")
    input_country.send_keys("Russia")
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()