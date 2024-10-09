from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException, WebDriverException

from time import sleep


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)

#abrindo navegador
driver.get("https://www.google.com/maps")

#maximizar navegador
driver.maximize_window()

def esta_na_aba_de_rotas():
    xpath = '//button[@aria-label="Fechar rotas"]'    
    botao_rota = driver.find_element(By.XPATH, xpath)
    return len(botao_rota) > 0 

#informe o endereço
def adiciona_destino(endereco, num_box=1):    
    if not esta_na_aba_de_rotas():
        botao_buscar = driver.find_element(By.ID, 'searchboxinput')
        botao_buscar.clear()
        botao_buscar.send_keys(endereco)
        botao_buscar.send_keys(Keys.RETURN)
    else:        
        xpath = '//div[contains(@id, "direction-searchbox")]//input'
        box = driver.find_element(By.XPATH, xpath)
        box = [c for c in box if c.is_displayed()]
        if len(box) >= num_box:
             box_endereco = box[num_box-1]
             box_endereco.send_keys(Keys.CONTROL + 'a')
             box_endereco.send_keys(Keys.DELETE)
             box_endereco.send_keys(endereco)          
             box_endereco.send_keys(Keys.RETURN) 
        else:
            print(f'Não foi possível adicionar o endereço {len(box)} | {(num_box)}')

#clicar em rotas
def abre_rotas():
    xpath = '//button[@data-value="Rotas"]'
    wait = WebDriverWait(driver, timeout=2)
    botao_rota = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    botao_rota.click()

    #aguardar tela de rotas abrir
    xpath = '//button[@aria-label="Fechar rotas"]'
    wait = WebDriverWait(driver, timeout=2)
    botao_rota = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    
if __name__ == '__main__':
    endereco = [
                'Av. Guapira, 117 - Tucuruvi',
                'Av. Mazzei, 100 - Tucuruvi',
                'Rua Aranguera, 52 - Vila gustavo',            
               ]
    adiciona_destino(endereco, 1)
    abre_rotas()

    sleep(600)