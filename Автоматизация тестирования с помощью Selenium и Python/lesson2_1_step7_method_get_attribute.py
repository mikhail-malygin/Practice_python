from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    box = browser.find_element_by_tag_name("img")
    x = box.get_attribute("valuex")
    y = calc(x)

    input_number = browser.find_element_by_id("answer")
    input_number.send_keys(y)

    checkbox_robot = browser.find_element_by_id("robotCheckbox")
    checkbox_robot.click()

    radiobutton_robot = browser.find_element_by_id("robotsRule")
    radiobutton_robot.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()