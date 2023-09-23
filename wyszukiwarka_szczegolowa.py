from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.intercity.pl/pl/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="searchTrainForm"]/p/a').click()
# Wskazanie stacji początkowej i końcowej
stacja_poczatkowa = driver.find_element(By.XPATH, '//*[@id="stname-0"]')
stacja_poczatkowa.send_keys("Warszawa Główna")
stpoczdrop = driver.find_element(By.XPATH, '//*[@id="searchTrainForm"]/div[1]/div[2]/div[1]/div/div/ul')
stpoczdrop.click()
stacja_koncowa = driver.find_element(By.XPATH, '//*[@id="stname-1"]')
stacja_koncowa.send_keys("Wrocław Główny")
stkondrop = driver.find_element(By.XPATH, '//*[@id="searchTrainForm"]/div[1]/div[2]/div[3]/div/div/ul')
stkondrop.click()
radio_odjazd = driver.find_element(By.XPATH, '//*[@id="inlineRadio2"]')
radio_przyjazd = driver.find_element(By.XPATH, '//*[@id="inlineRadio1"]')
print(f"Opcja odjazdu jest wybrana: {radio_odjazd.is_selected()}")
print(f"Opcja przyjazdu jest wybrana: {radio_przyjazd.is_selected()}")
# Wybór daty
kalendarz = driver.find_element(By.XPATH, '//*[@id="date_picker"]')
kalendarz.clear()
kalendarz.send_keys("2023-10-10")
# Wybór godziny
driver.find_element(By.XPATH, '//*[@id="ic-seek-time"]').click()
godziny = driver.find_elements(By.XPATH, '/html/body/div[3]/ul/li')
for godzina in godziny:
    if godzina.text == "09:00":
        godzina.click()
        break


# Wybór czasu na przesiadkę
driver.find_element(By.ID, 'czas_na_przesiadke').click()
czasy = driver.find_elements(By.XPATH, '//*[@id="czas_na_przesiadke"]/option')
for czas in czasy:
    if czas.text == "Co najmniej 20 minut":
        czas.click()
        break


# Wybór przewoźnika
przewoznicy = driver.find_elements(By.XPATH, '//*[@id="searchTrainForm"]/div[1]/div[3]/div[3]/fieldset/div/input')
print(f"Ilość przewoźników: {len(przewoznicy)}")
lista_przewoznikow = []
for przewoznik in przewoznicy:
    element = przewoznik.get_attribute("value")
    lista_przewoznikow.append(element)
    if element in ("tlk", "ppo"):
        przewoznik.click()


print(f"Lista przewoźników: {lista_przewoznikow}")
# Wybór opcji połączenia kolejowego
opcje = driver.find_elements(By.XPATH, '//*[@id="searchTrainForm"]/div[1]/div[4]/fieldset/div/input')
print(f"Ilość opcji: {len(opcje)}")
lista_opcji = []
for opcja in opcje:
    choice = opcja.get_attribute("name")
    lista_opcji.append(choice)
    if choice in ("direct"):
        opcja.click()


print(f"Lista opcji: {lista_opcji}")
# Kliknięcie "Wyszukaj"
driver.find_element(By.XPATH, '//*[@id="searchTrainForm"]/div[3]/div[2]/button').click()
time.sleep(5)
