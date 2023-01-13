from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Ваш код, который считает формулу
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Жмем кнопку I want to go on a magical journey!
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

    # Жмем кнопку ОК в появившейся модалке
    confirm = browser.switch_to.alert
    confirm.accept()

    # Ваш код, который считывает элемент Х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

   
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

        
    # Жмем кнопку Submit
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

     
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
