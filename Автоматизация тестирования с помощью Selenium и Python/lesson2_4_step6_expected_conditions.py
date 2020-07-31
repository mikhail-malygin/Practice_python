from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return math.log(abs(12 * math.sin(int(x))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    time_to_buy = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button_book = browser.find_element_by_id("book")
    button_book.click()


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = str(calc(x))

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)
    button_submit = browser.find_element_by_id("solve")
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()