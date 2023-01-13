from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//input[@type='text']")
    input1.send_keys("Костя")
    input2 = browser.find_element(By.XPATH, "//input[@name='last_name']")
    input2.send_keys("Орешкин")
    input3 = browser.find_element(By.XPATH, "//input[@class='form-control city']")
    input3.send_keys("Пермь")
    input4 = browser.find_element(By.XPATH, "//input[@id='country']")
    input4.send_keys("РФ")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
