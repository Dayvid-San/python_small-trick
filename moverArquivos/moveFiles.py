import os
import shutil

#oldAdress = "/home/dayvidsan/'Área de Trabalho'/Projetos/soundsOnline/sounds"
oldAdress  ='./songs/'
newAdress = '/home/dayvidsan/Música/'


lista = os.listdir(oldAdress) #lista separando apenas os arquivos do caminho.

# *** lista_len recebe o tamanho da lista ***
lista_len = len(lista)
x = 0

while x < lista_len:
    caminhoCompleto_old = oldAdress + lista[x] #variável recebe caminho + arquivo, conforme indice
    caminhoCompleto_new = newAdress + lista[x] #variável recebe caminho + arquivo, conforme indice
    shutil.move(caminhoCompleto_old, caminhoCompleto_new) #módulo 'shutil.move()' move os arquivos
    print((x+1), '-', lista[x]) #apenas para ver como está sendo feito
    x += 1