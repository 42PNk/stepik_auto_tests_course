from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Ваш код, который считает формулу
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который считывает элемент Х
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)

  
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    
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
