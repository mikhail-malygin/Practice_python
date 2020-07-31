from selenium import webdriver
import time
import math

def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = str(func(x))

    input = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)

    checkbox_robot = browser.find_element_by_id("robotCheckbox")
    checkbox_robot.click()

    radiobuton_robots = browser.find_element_by_id("robotsRule")
    radiobuton_robots.click()




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