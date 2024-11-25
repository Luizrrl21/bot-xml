def bot(dt_inicial, dt_final, fornecedor):
    import time
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from functions import element_click, element_input, table_search, dynamic_id_input, pasta

    #Instalação + Config chromedriver
    service = Service(ChromeDriverManager().install())
    path = pasta()
    options = Options()
    options.add_argument("--allow-running-insecure-content")  # Allow insecure content
    options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://example.com")  # Replace example.com with your site's domain
    options.add_experimental_option("prefs", {
    "download.default_directory": path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
    driver = webdriver.Chrome(service=service, options=options)

    #Entrar no site
    driver.maximize_window()
    driver.get('https://fornecedores.gmsuite.com.br')
    
    #Login
    element_input(driver=driver, xpath='//*[@id="username"]', value='fr0110490')
    element_input(driver=driver, xpath='//*[@id="password"]', value='#Master20211')
    element_click(driver=driver, xpath='//*[@id="kc-login"]')

    #Navegação
    element_click(driver=driver, xpath='/html/body/app-root/app-clean-shell/app-clean-shell-content/cds-sidenav/mat-drawer-container/mat-drawer/div/app-sidenav/div/app-sidenav-node/div/cds-tree/cds-nested-tree-node/div/button') #Fornecedores
    time.sleep(1)

    element_click(driver=driver, xpath='/html/body/app-root/app-clean-shell/app-clean-shell-content/cds-sidenav/mat-drawer-container/mat-drawer/div/app-sidenav/div/app-sidenav-node[2]/div/cds-tree/cds-nested-tree-node/div/button') #Área do Fornecedor
    time.sleep(1)

    element_click(driver=driver, xpath='/html/body/app-root/app-clean-shell/app-clean-shell-content/cds-sidenav/mat-drawer-container/mat-drawer/div/app-sidenav/div/app-sidenav-node[3]/div/cds-tree/cds-nested-tree-node[4]/div/button') #Contas a Pagar
    time.sleep(1)

    element_click(driver=driver, xpath='//*[@id="mat-dialog-1"]/app-modal-help-description/header/button') #Fechar pop-up
    
    #Procurar o fornecedor
    print(fornecedor)
    time.sleep(2)
    table_search(driver=driver, fornecedor=fornecedor)
    time.sleep(3)

    #Inpt das Datas
    dynamic_id_input(driver=driver, xpath='//label[contains(text(),"Data de emissão inícial")]', value=dt_inicial)
    dynamic_id_input(driver=driver, xpath='//label[contains(text(),"Data de emissão final")]', value=dt_final)
    element_click(driver=driver, xpath='/html/body/app-root/app-clean-shell/app-clean-shell-content/cds-sidenav/mat-drawer-container/mat-drawer-content/app-contas-pagar/div[4]/app-filtro/div[2]/div/cds-button[3]/button')
    time.sleep(1)


    element_click(driver=driver, xpath='//mat-select[@aria-label="Itens por página:"]')
    element_click(driver=driver, xpath='//*[@id="mat-option-49"]')
    time.sleep(10)

    linha = 1
    while True: #Iteração por notas 
        if linha <= 51: #Condição de paginação
            try: 
                linha += 1 #Pula a linha do cabeçário e começa a iterar a partir da segunda linha
                nota = element_click(driver=driver, xpath=f"/html/body/app-root/app-clean-shell/app-clean-shell-content/cds-sidenav/mat-drawer-container/mat-drawer-content/app-contas-pagar/div[4]/div/div[1]/table/tr[{str(linha)}]/td[9]/cds-button/button") #Abrir Nota
                if nota == "Erro!": break
                time.sleep(1.5)
                download = element_click(driver=driver, xpath='//*[@id="print"]/footer/cds-button[1]/button') #Baixar Nota
                if download == "Erro!": break
                time.sleep(1.5)
                close = element_click(driver=driver, xpath='//*[@id="print"]/header/button') #Fechar Nota
                if close == "Erro!": break
                time.sleep(1.5)
            except:
                print("fim")
                break
        else:
            try:
                linha = 1 #Redefine o Índice da Iteração
                element_click(driver=driver, xpath='/html/body/app-root/app-clean-shell/app-clean-shell-content/cds-sidenav/mat-drawer-container/mat-drawer-content/app-contas-pagar/div[4]/div/div[2]/div/cds-paginator/mat-paginator/div/div/div[2]/button[2]') #Próxima página
            except:
                print("fim")
                break


    #Gerar Excel

    time.sleep(100)
