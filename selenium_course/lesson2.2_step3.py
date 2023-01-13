from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

# Ваш код, который считает формулу
def sum(x, y):
    return str(x + y)

try:

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который считывает элемент Х
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = int(x_element.text)
    # Ваш код, который считывает элемент Y
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = int(y_element.text)

    # Ваш код, который выбирает сумму X+Y
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum(x, y)) # ищем элемент с value=(sum(x, y))

    # Жмем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
