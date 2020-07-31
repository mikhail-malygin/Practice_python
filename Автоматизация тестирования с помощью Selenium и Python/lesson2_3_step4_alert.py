from selenium import webdriver
import time
import math

def calc(x):
    return math.log(abs(12 * math.sin(int(x))))

try:
    link = " http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_journey = browser.find_element_by_tag_name("button")
    button_journey.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = str(calc(x))

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)
    button_submit = browser.find_element_by_tag_name("button")
    button_submit.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()