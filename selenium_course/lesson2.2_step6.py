from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Ваш код, который считает формулу
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который считывает элемент Х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Ваш код, который скроллит экран на 100 пикселей вниз
    # browser.execute_script("window.scrollBy(0, 100);")

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Ваш код, который скроллит кнопку Submit (важно соблюдать порядок. То есть сперва заполнить
    # обязательное поле, а потом уже скроллить кнопку)  
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    # Активируем чекбокс
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    # Активируем радиобаттон
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option1.click()

    # Жмем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

     
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
