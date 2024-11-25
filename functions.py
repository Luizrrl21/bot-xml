
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def pasta():
    import os
    import shutil
    
    dir = './xmls' #Criação da Pasta para baixar xml
    if os.path.exists(dir): # Verifica se a pasta existe
        shutil.rmtree(dir) # Se existir, remove a pasta e seu conteúdo
    os.mkdir(dir) # Cria a pasta
    current_dir = os.path.dirname(os.path.abspath(__file__)) # Obtém o caminho absoluto da pasta onde o script está rodando
    path = os.path.join(current_dir, "xmls") # Constrói o caminho completo para a pasta "xmls"
    print(f"Criando path {path}")

    return path

def element_input(driver:str, xpath:str, value:str):
    try:
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        username.send_keys(value)
    except Exception as e: print(e)

def dynamic_id_input(driver:str, xpath:str, value:str):
    label_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
)
    value = value.strftime("%d/%m/$Y")
    input_id = label_element.get_attribute("for") # Localizar o atributo 'for' do <label>
    input_element = driver.find_element(By.ID, input_id) # Usar o ID para localizar o input
    input_element.send_keys(value) # Ação no elemento (por exemplo, preencher a data)

def element_click (driver:str, xpath:str):
        try:
            element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            element.click()
        except Exception as e: print(e)
        # return "Erro!"
    

def table_search(driver:str, fornecedor:str):
    while True:
        linha = 2
        xpath = f'//*[@id="mat-dialog-0"]/app-modal-fornecedor/div/div/div[3]/div/table/tr[{str(linha)}]/td[1]'
        element = driver.find_element(By.XPATH, xpath)
        if fornecedor == element.text:
            element_click(driver=driver, xpath=f'//*[@id="mat-dialog-0"]/app-modal-fornecedor/div/div/div[3]/div/table/tr[{str(linha)}]/td[3]/cds-fab/button')
            break
        else:
            linha = linha + 1
            print("Erro ao achar o Fornecedor")

