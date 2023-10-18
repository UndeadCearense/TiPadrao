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

accef = 11
eja2 = 25
eja1 = 12
#### Especificar qual turma de eja para abrir os templates corretamente
curso = eja2
#### Usuário e senha
login = "loginhere"
senha = "passwordhere"
####

planilha = "thespreadsheetdirectoryhere"

turmas = pd.read_excel(planilha)

driver = webdriver.Edge()
driver.maximize_window()
driver.get('https://www.sponteeducacional.net.br/Default.aspx?Page=/SPDiretor/Central.aspx')
driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div[2]/div/div[1]/div[2]/input[1]").send_keys(login)
driver.find_element(By.XPATH, '//*[@id="txtSenha"]').send_keys(senha)
driver.find_element(By.XPATH, '//*[@id="btnok"]').click()
time.sleep(10)
driver.get('https://www.sponteeducacional.net.br/SPNotas/NotasParciaisDisciplinas.aspx')
for index,row in turmas.iterrows():
    print(turmas)
    driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_pnlFiltros"]/div[2]/div[2]/span[2]/span[1]/span/span[2]').click()
    driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys(row["Turma"])
    time.sleep(5)
    ActionChains(driver)        .key_down(Keys.ENTER)        .key_up(Keys.ENTER)        .perform()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_divDisciplina"]/span[2]/span[1]/span/span[2]/b').click()
    driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys("fis")
    ActionChains(driver)        .key_down(Keys.ARROW_DOWN)        .key_up(Keys.ARROW_DOWN)        .key_down(Keys.ENTER)        .key_up(Keys.ENTER)        .perform()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_AdicionarAvaliacao_div"]/div/center/span').click()
    time.sleep(5)
    ActionChains(driver)        .key_down(Keys.ENTER)        .key_up(Keys.ENTER)        .perform()
    time.sleep(4)
    ActionChains(driver)        .send_keys('fis')        .key_down(Keys.ARROW_UP)        .key_up(Keys.ARROW_UP)        .key_down(Keys.ARROW_UP)        .key_up(Keys.ARROW_UP)        .key_down(Keys.ENTER)        .key_up(Keys.ENTER)        .perform()
    time.sleep(4)
    ActionChains(driver)        .key_down(Keys.TAB)        .key_up(Keys.TAB)        .key_down(Keys.ENTER)        .key_up(Keys.ENTER)        .key_down(Keys.ARROW_DOWN)        .key_up(Keys.ARROW_DOWN)        .key_down(Keys.ENTER)        .key_up(Keys.ENTER)        .perform()
    time.sleep(4)
    ActionChains(driver)        .key_down(Keys.TAB)        .key_up(Keys.TAB)        .key_down(Keys.TAB)        .key_up(Keys.TAB)        .key_down(Keys.ENTER)        .key_up(Keys.ENTER)        .perform()
    time.sleep(6)
    for j in range(curso):
        ActionChains(driver)            .key_down(Keys.TAB)            .key_up(Keys.TAB)            .key_down(Keys.ENTER)            .key_up(Keys.ENTER)            .perform()
        time.sleep(6)
        ActionChains(driver)            .key_down(Keys.ARROW_DOWN)            .key_up(Keys.ARROW_DOWN)            .key_down(Keys.ENTER)            .key_up(Keys.ENTER)            .perform()
        time.sleep(4)
        ActionChains(driver)            .key_down(Keys.TAB)            .key_up(Keys.TAB)            .perform()
        time.sleep(3)
        ActionChains(driver)            .key_down(Keys.TAB)            .key_up(Keys.TAB)            .key_down(Keys.ENTER)            .key_up(Keys.ENTER)            .perform()
        time.sleep(4)
        ActionChains(driver)            .key_down(Keys.TAB)            .key_up(Keys.TAB)            .key_down(Keys.ENTER)            .key_up(Keys.ENTER)            .send_keys('ava')            .key_down(Keys.ENTER)            .key_up(Keys.ENTER)            .perform()
        time.sleep(5)
        ActionChains(driver)            .key_down(Keys.TAB)            .key_up(Keys.TAB)            .key_down(Keys.TAB)            .key_up(Keys.TAB)            .key_down(Keys.ENTER)            .key_up(Keys.ENTER)            .perform()
        time.sleep(8)            
time.sleep(8)
driver.quit()

