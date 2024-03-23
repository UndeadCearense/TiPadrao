#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##### Trocar links completo(abre as pastas de grupos)
import time
import pyautogui as py


#caso houver mais de um link de referência a ser trocado nas planilhas, acrescentar nos links velhos
linkvelho='cole o link aqui'#  <<<<<

linkvelho2='cole o link aqui'
linkvelho3='cole o link aqui'

#link do novo cronograma
linknovo='cole o link aqui' #(não precisa da parte do EDIT em diante)


#link da URL onde ficam as pastas dos grupos
linkpastas='cole o link aqui'

py.PAUSE = 1
py.click(x=2066, y=850)


#abre pastas
time.sleep(10)#tempo até iniciar o código
for p in range(14):
    N=1
    py.doubleClick(x=3251, y=328+p*43)## (x=3732, y=351+t*48) Usar com zoom da página em 100%  esse serve para 3º
                                    #(x=3251, y=328+t*43) > Usar com zoom da página a 90% Esse serve para 5º e 7º
    time.sleep(3)
    n = N +1

##abre planilhas
    for t in range(16):
        N=1
        py.doubleClick(x=3251, y=328+t*43)## (x=3732, y=351+t*48) Usar com zoom da página em 100%  esse serve para 3º
                                    #(x=3251, y=328+t*43) > Usar com zoom da página a 90% Esse serve para 5º e 7º        
        time.sleep(1)    
        py.hotkey('ctrl', 'shift', 'tab')
        time.sleep(1)
        n = N +1
    time.sleep(15)
    py.hotkey('ctrl', 'tab')

##troca referências

###Link velho
    for u in range(16):
        py.click(x=1985, y=261)
        py.write('F8')
        py.press('enter')
        py.hotkey('ctrl', 'h')
        py.write(linkvelho)
        py.press('tab')
        py.write(linknovo)
        for i in range(6):
            py.press('tab')
        py.press('space')
        for j in range(3):
            py.press('tab')
        py.press('enter')
        py.press('enter')
        py.click(x=3105, y=836)
        time.sleep(2)
        py.hotkey('ctrl', 'tab')    
    py.hotkey('ctrl', 'tab')

###Link velho2
    
    #for u in range(16):
        #py.click(x=1985, y=261)
        #py.write('F8')
        #py.press('enter')
        #py.hotkey('ctrl', 'h')
        #py.write(linkvelho2)
        #py.press('tab')
        #py.write(linknovo)
        #for i in range(6):
            #py.press('tab')
        #py.press('space')
        #for j in range(3):
            #py.press('tab')
        #py.press('enter')
        #py.press('enter')
        #py.click(x=3105, y=836)
        #time.sleep(1.5)
        #py.hotkey('ctrl', 'tab')
    
    #py.hotkey('ctrl', 'tab')
    
###Link velho3

    #for u in range(16):
        #py.click(x=1985, y=261)
        #py.write('F8')
        #py.press('enter')
        #py.hotkey('ctrl', 'h')
        #py.write(linkvelho3)
        #py.press('tab')
        #py.write(linknovo)
        #for i in range(6):
            #py.press('tab')
        #py.press('space')
        #for j in range(3):
            #py.press('tab')
        #py.press('enter')
        #py.press('enter')
        #py.click(x=3105, y=836)
        #time.sleep(1.5)
        #py.hotkey('ctrl', 'tab')    
    #py.hotkey('ctrl', 'tab')


#permitir acesso(não permite da ficha de frequencia, ela tem q ser na mão)
    for c in range(15):
        py.hotkey('ctrl', 'tab')
        py.click(x=3017, y=761)

        
#LIMPAR CAIXA DE NOTAS (caso precise limpar)
    #for u in range(15):
        #py.click(x=1985, y=261)
        #py.write('D16:O69')
        #py.press('enter')
        #py.press('del')
        #py.click(x=2066, y=850)
        #py.hotkey('ctrl', 'shift', 'tab')
    #py.hotkey('ctrl', 'tab')

    
#fechar abas 
    for d in range(16):
        py.hotkey('ctrl', 'w')

    time.sleep(10)
    
    #renomear planilhas 
    for t in range(15):
        N = 1
        py.PAUSE = 0.2
        py.rightClick(x=3251, y=328+t*43)#(x=3732, y=351+t*48)  (x=3251, y=328+t*43)
        time.sleep(1)
        for i in range(2):
            py.press("down")        
        py.press("enter")
        
        #(para caso esteja 'Cópia de')        
        py.hotkey('ctrl', 'home')
        for j in range(9):
            py.press("del")
            
        #(para caso precise alterar algo no final de todas)        
        
        #py.hotkey('ctrl', 'end')
        #for b in range(2):
            #py.press('backspace')
        #py.write('')
        py.press("enter")
        time.sleep(2)
        n = N +1
    py.hotkey('ctrl', 'tab')

#renomear ficha de frequencia semanal(para caso esteja 'Cópia de') 
    py.rightClick(x=3251, y=973)
    time.sleep(1)
    for i in range(2):
        py.press("down")
    py.press("enter")
    py.hotkey('ctrl', 'home')
    for j in range(9):
        py.press("del")
    py.press("enter")
    time.sleep(2)
    
    ##Retorna pra as pastas
    py.click(x=2636, y=49)
    py.write(linkpastas)
    py.press('enter')
    time.sleep(7)
    n = N +1

