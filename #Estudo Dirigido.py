#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import sys
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver
import time
login = "moodlelogin"
senha = "moodlepassword"

### Link da página onde estão as turmas de tec. enf ###
link = "moodlepage"

planilha = "Liberação Estudo Dirigido.xlsx"
alunos = pd.read_excel(planilha)
turma = "typeheretheclassname"

######Login#####
driver=webdriver.Edge()
driver.maximize_window()
driver.get('https://escolapadrao.com.br/saladeaula/my/')
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(login)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(senha)
driver.find_element(By.XPATH, '//*[@id="loginbtn"]').click()
time.sleep(2)
##### Página das Turmas de téc. enf #####
driver.get(link)
time.sleep(3)
####Seleciona a caixa de pesquisa ####
driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/section/div/div[1]/div/div[2]/div/form/div/input').click()
####Preenche com a turma correta ####
time.sleep(4)
driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/section/div/div[1]/div/div[2]/div/form/div/input').send_keys(turma)
####Seleciona a turma que irá realizar o estudo dirigido####
driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/section/div/div[1]/div/div[2]/div/form/div/div/button').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[5]/div[5]/div/div[2]/div/section/div/form/div[2]/div/div/ul/li/div/a').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[6]/div[4]/div/div[2]/div/section/div/form/div[2]/div[2]/div/div[2]/div[1]/a[1]').click()
time.sleep(7)
####Seção de participantes####
driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/nav/ul/li[3]').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div[5]/div[1]/div[2]/div/section/div/div[1]/div/div[1]/div/form/select').click()
time.sleep(2)
ActionChains(driver)    .key_down(Keys.ARROW_DOWN)    .key_up(Keys.ARROW_DOWN)    .key_down(Keys.ARROW_DOWN)    .key_up(Keys.ARROW_DOWN)    .key_down(Keys.ENTER)    .key_up(Keys.ENTER)    .perform()
#####Seleciona o grupo de Estudo dirigido####
driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/section/div/form/div/div/div[1]/div[1]/select/option[8]').click()
####Entra no grupo de Estudo Dirigido####
driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/section/div/form/div/div/div[2]/div[2]/input').click()
time.sleep(5)
####Insere a lista de alunos no grupo#####    
for index,row in alunos.iterrows():
    print(alunos)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/section/div/div/form/div/table/tbody/tr[1]/td[3]/div/div/input[1]').send_keys(row["Nome"])
    time.sleep(1)
    ActionChains(driver)        .key_down(Keys.ENTER)        .key_up(Keys.ENTER)        .perform()
    time.sleep(1)
####CLica no botão Limpar####        
    driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/section/div/div/form/div/table/tbody/tr[1]/td[3]/div/div/input[2]').click()
time.sleep(3)
driver.quit

