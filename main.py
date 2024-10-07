from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from time import sleep

endereco = 'Av. Guapira, 117 - Tucuruvi'

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)


#abrindo navegador
driver.get("https://www.google.com/maps")

#informe o endereço
botao_buscar = driver.find_element(By.ID, 'searchboxinput')
botao_buscar.clear()
botao_buscar.send_keys(endereco)
botao_buscar.send_keys(Keys.RETURN)

#clicar em rotas
xpath = '//button[@data-value="Rotas"]'
wait = WebDriverWait(driver, timeout=2)
botao_rota = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
botao_rota.click()

sleep(600)