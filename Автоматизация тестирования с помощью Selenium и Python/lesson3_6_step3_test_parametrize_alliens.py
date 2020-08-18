import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

message = ''

@pytest.fixture(scope = "function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    #browser.implicitly_wait(20)
    yield browser
    print("\nquit browser..")
    browser.quit()



@pytest.mark.parametrize('id', ["236895", "236896", "236897", "236898",
                                "236899", "236903", "236904", "236905"])
def test_check_feedback(browser, id):
    link = f"https://stepik.org/lesson/{id}/step/1"
    browser.get(link)
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "submit-submission")))

    # Ищем элемент со строкой ввода и вводим туда ответ
    input_text = browser.find_element_by_css_selector(".textarea")
    answer = str(math.log(int(time.time())))
    input_text.send_keys(answer)
    button_send = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button_send.click()

    # Находим текст фидбека
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "again-btn")))
    text_feedback = browser.find_element_by_css_selector(".smart-hints__hint")
    check_text_feedback = text_feedback.text

    # Сравниваем фактический фидбек с ожидаемым. Если отличаются, то
    # добавляем этот фактический фидбек в строку и выводим строку на экран
    global message
    if check_text_feedback != "Correct!":
        message += check_text_feedback
        if link == "https://stepik.org/lesson/236905/step/1":
            print("Final message: " + message)
    assert check_text_feedback == "Correct!", "Error message"




