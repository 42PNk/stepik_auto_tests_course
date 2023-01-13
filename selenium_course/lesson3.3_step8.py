from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

# Ваш код, который считает формулу
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:



    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока цена не упадет до 100$
    WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    # Ваш код, который находит кноку Book
    button1 = browser.find_element(By.CSS_SELECTOR, "#book")
    button1.click()
    
    # Ваш код, который считывает элемент Х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Жмем кнопку Submit
    button2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    button2.click()

     
finally:
    
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
