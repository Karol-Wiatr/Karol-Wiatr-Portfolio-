from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
waitfor = WebDriverWait(driver, 10)
driver.get("https://www.intercity.pl/pl/")
driver.maximize_window()
driver.implicitly_wait(10)
stacja_poczatkowa = driver.find_element(By.XPATH, "//input[@id='stname-0']")
stacja_koncowa = driver.find_element(By.XPATH, "//input[@id='stname-1']")
wybor_daty = driver.find_element(By.XPATH, "//input[@id='date_picker']")
godzina = driver.find_element(By.XPATH, "//input[@id='ic-seek-time']")
stacja_poczatkowa.send_keys("Warszawa Główna")
poczdrop = driver.find_element(By.XPATH, '//*[@id="searchTrainForm"]/div[1]/div[2]/div[1]/div/div/ul')
waitfor.until(ec.element_to_be_clickable(poczdrop))
poczdrop.click()
stacja_koncowa.send_keys("Wrocław Główny")
kondrop = driver.find_element(By.XPATH, '//*[@id="searchTrainForm"]/div[1]/div[2]/div[3]/div/div/ul')
waitfor.until(ec.element_to_be_clickable(kondrop))
kondrop.click()
wybor_daty.send_keys("2023-10-10")
godzina.click()
godziny = driver.find_elements(By.XPATH, "/html/body/div[3]/ul/li")
for godz in godziny:
    if godz.text == "09:00":
        godz.click()
        break


driver.find_element(By.XPATH, "//button[@name='search']").click()
time.sleep(8)
