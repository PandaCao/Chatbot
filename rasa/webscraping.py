from selenium import webdriver
from selenium.webdriver.common.by import By
# cesta do chromedriveru
PATH = r"C:\Users\lowak\Desktop\Skola\Chatbot\chromedriver.exe"

# pro otevření Chromu
driver = webdriver.Chrome(PATH)

# url stránky
url = 'https://www.spseplzen.cz/kontakty/'

# otevření url stránky v prohlížeči
driver.get(url)

# XPATH v proměnných
reditelka_path = '//*[@id="post-540"]/div[2]/div[1]/div[1]/div/div/div[4]/div/p[1]'
kontakty_path = '//*[@id="post-540"]/div[2]/section/div[1]/div[1]/div/div/div/div/p[2]'

# pole, ve kterých získáváme elementy ze stránky
link = [driver.find_elements(By.XPATH, reditelka_path), driver.find_elements(By.XPATH, kontakty_path)]

# cykly, kdybychom měli jen jeden, vypíše to objekt místo textu
for i in link:
    for y in i:
        print(y.text)
