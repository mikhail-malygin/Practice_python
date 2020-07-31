from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select



try:
    link = " http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_id("num1")
    number1 = int(element1.text)
    element2 = browser.find_element_by_id("num2")
    number2 = int(element2.text)
    sum = str(number1 + number2)


    list_numbers = Select(browser.find_element_by_tag_name("select"))
    list_numbers.select_by_value(sum)


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