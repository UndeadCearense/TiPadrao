#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Liberação da atividade de estudo dirigido para alunos
import pandas as pd
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver
import time
login = "digite aqui"
senha = "digite aqui"

### Link da página de participantes###

groups = "linkdapagina"


####planilha com a lista de alunos###
planilha = "planilha com a lista de alunos.xlsx"
alunos = pd.read_excel(planilha)


######Login#####
driver=webdriver.Edge()
driver.maximize_window()
driver.get('https://escolapadrao.com.br/saladeaula/my/')
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(login)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(senha)
driver.find_element(By.XPATH, '//*[@id="loginbtn"]').click()
time.sleep(2)

####Entra no grupo de Estudo Dirigido####
driver.get (groups)
time.sleep(5)
####Insere a lista de alunos no grupo#####    
for index,row in alunos.iterrows():
    print(alunos)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/section/div/div/form/div/table/tbody/tr[1]/td[3]/div/div/input[1]').send_keys(row["Código"])
    time.sleep(1)
    ActionChains(driver)        .key_down(Keys.ENTER)        .key_up(Keys.ENTER)        .perform()
    time.sleep(2)
####Cica no botão Limpar####        
    driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/section/div/div/form/div/table/tbody/tr[1]/td[3]/div/div/input[2]').click()
time.sleep(3)
driver.quit()

