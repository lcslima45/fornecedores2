#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:01:39 2020

@author: lima
"""


import csv

def fornecedores_pag(caminho):
    dicionario = {}
    fornecedores_pagamento_maximo={}

    ##Abrindo arquivo
    with open(caminho, 'r') as ficheiro:
        arquivo = csv.reader(ficheiro)
        #criando chave do mês para o dicionário
        for linha in arquivo:
            if ('data' not in linha[2]): 
                data_aux = linha[2].split('-').copy()
                chave_mes = '{}-{}'.format(data_aux[0], data_aux[1])
            #inserindo cada item pertencente ao seu mês no local da chave
                if chave_mes in dicionario:
                    dicionario[chave_mes].append(linha)
                else:
                    dicionario[chave_mes] = []
                    dicionario[chave_mes].append(linha)
    ficheiro.close()
    #ordenando um novo dicionário onde colocaremos os pagamentos máximos
     #procurando máximos
    for i in sorted(dicionario.keys()):
        soma_fornecedores = {}
        for p in range(len(dicionario[i])):
            
            chave_fornecedor = dicionario[i][p][1]
            if (chave_fornecedor in soma_fornecedores.keys()):
                soma_fornecedores[chave_fornecedor] = soma_fornecedores[chave_fornecedor] + float(dicionario[i][p][3])
            else:
                soma_fornecedores[chave_fornecedor] = float(dicionario[i][p][3]) 
        maximo = max(soma_fornecedores.values())
        for s in soma_fornecedores.items():
            fornecedor, soma = s
            if (soma == maximo):
                fornecedores_pagamento_maximo[i] = (fornecedor, soma)
                
    return fornecedores_pagamento_maximo