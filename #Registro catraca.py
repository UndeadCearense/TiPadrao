#!/usr/bin/env python
# coding: utf-8

# In[1]:


###### DOWNLOAD RELATÓRIO ACESSOS CATRACA(PERÍODOS)######

import pyautogui as py
import pandas as pd
import sys
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver
import time
from datetime import date
from datetime import timedelta

login = "loginhere"
senha = "passwordhere"
hora1 = '07:00' #horário inicial
hora2 = '21:55' #horário final

hoje = date.today()
ontem = hoje - timedelta(days = 1)
print(ontem.strftime('%d/%m/%Y'))
######Login#####
driver=webdriver.Edge()
driver.maximize_window()
driver.get('https://192.168.200.2:30443/')
driver.find_element(By.XPATH, '/html/body/div/div[2]/button[3]').click()
driver.find_element(By.XPATH, '/html/body/div/div[3]/p[2]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[2]/form/div[1]/input').send_keys(login)
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[2]/form/div[2]/div/input').send_keys(senha)
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[2]/form/div[5]/button').click()
time.sleep(3)

####Acessar a guia de relatórios#####
driver.get('https://192.168.200.2:30443/#/view_report/global')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[1]/a[1]').click()

##Trocar para a data desejada##
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[1]/div[1]/div/input').click()
                    
ActionChains(driver)    .key_down(Keys.SHIFT)    .key_down(Keys.HOME)    .key_up(Keys.SHIFT)    .key_up(Keys.HOME)    .perform()
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[1]/div[1]/div/input').send_keys(hoje.strftime('%d/%m/%Y'))
time.sleep(1)
ActionChains(driver)    .key_down(Keys.TAB)    .key_up(Keys.TAB)    .key_down(Keys.TAB)    .key_up(Keys.TAB)    .key_down(Keys.SHIFT)    .key_down(Keys.HOME)    .key_up(Keys.SHIFT)    .key_up(Keys.HOME)    .perform()

##Trocar os para os horários desejados##
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div[1]/div/input').send_keys(hora1)
                    
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div[2]/div/input').click()
                    
ActionChains(driver)    .key_down(Keys.SHIFT)    .key_down(Keys.HOME)    .key_up(Keys.SHIFT)    .key_up(Keys.HOME)    .perform()
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div[2]/div/input').send_keys(hora2)
                    
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[4]/div/button').click()
                    
time.sleep(3)

#####Marcar o departamento somente de alunos#####

driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[3]/div/div[3]/div/div/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[3]/div/div[3]/div/ul/li/div[3]/a/div').click()
time.sleep(4)

####Baixar o relatório####
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/table/thead/tr/th[2]').click()
time.sleep(4)

driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[3]/a').click()

time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[3]/ul/li[1]/a').click()
time.sleep(10)

driver.quit()

####Transformar CSV em TXT####

from pathlib import Path
import os
import pandas as pd
from datetime import datetime


hoje = date.today()
caminho='D:\Raul Guenka\Downloads'
data_modificacao = lambda f: f.stat().st_mtime
#Organiza as planilhas em uma lista por ordem de modificação
directory = Path(caminho)
files = directory.glob('*.csv')
sorted_files = sorted(files, key=data_modificacao, reverse=True)
#Renomea a planilhas de acesso
file_type = '\.csv'
os.files = [f for f in os.listdir(caminho) if os.path.isfile(os.path.join(caminho, f))]
relatorio = pd.read_csv(sorted_files[0],sep=',',encoding='latin-1')
for i in range (len(relatorio)):
    #print(relatorio.iloc[i]['Hora'])
    #Divide a coluna em data e hora
    data, hora = relatorio.iloc[i]['Hora'].split(' ')
    dia, mes, ano = map(int, data.split('/'))
    hora, minuto, segundo = map(int, hora.split(':'))
    #ajusta o horário
    hora = hora-1
    #Grava denovo no dataframe
    relatorio.loc[i,'Hora'] = f'{dia}/{mes}/{ano} {hora}:{minuto}:{segundo}'
#relatorio.iloc[0]['Hora']=relatorio.iloc[0]['Hora']

fimrelatorio = len(relatorio)
#percorre a lista vendo os códigos
i=0
while(i<fimrelatorio):
    saida=0
    print("i= ", i)
    codigo=relatorio.loc[i]['Código']
    print("i= ", i)
    for j in range(i+1, fimrelatorio, 1):
        print("j= ", j)
        if (relatorio.loc[j]['Código']==codigo):
            if (saida!=0):
                relatorio = relatorio.drop(saida)
                fimrelatorio=fimrelatorio-1
                saida=j
            else:
                saida=j
    print(fimrelatorio)
    relatorio.reset_index(inplace=True,drop=True)
    i += 1
display(relatorio)
relatorio.to_csv(rf'{sorted_files[0]}', index = False)
os.rename(rf'{sorted_files[0]}', rf'{caminho}\relatorio{hoje}.txt')


# In[ ]:




