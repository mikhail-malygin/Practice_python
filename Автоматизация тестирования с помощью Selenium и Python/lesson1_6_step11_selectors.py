from selenium import webdriver
import time

link = ("http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html")

for i in range(2):
    try:
        browser = webdriver.Chrome()
        browser.get(link[i])

        input_first_name = browser.find_element_by_css_selector("div.first_block div.first_class input")
        input_first_name.send_keys("Mikhail")
        input_last_name = browser.find_element_by_css_selector("div.first_block div.second_class input")
        input_last_name.send_keys("Malygin")
        input_email = browser.find_element_by_css_selector("div.first_block div.third_class input")
        input_email.send_keys("test@mail.ru")


        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
