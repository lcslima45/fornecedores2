#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 19:58:48 2020

@author: lima
"""


from fornecedores3 import fornecedores_pag
caminho = input('Insira o caminho do seu arquivo CSV\n')
fornecedores_pagamento = fornecedores_pag(caminho)
tabela='<tr>'
file = open('tabela_fornecedores.html', 'w')
for i in fornecedores_pagamento.keys():
   if(i!='data-'):
        fornecedor, soma_pagamento = fornecedores_pagamento[i]
        linha = """
            <td>{}</td>
            <td>{}</td>
            <td>{:.2f}</td>
        """.format(i, fornecedor,soma_pagamento)
        tabela =tabela+linha+'</tr>'
        
html = """<html><head><meta charset='utf-8'>
    <title>Minha página de teste</title>
  </head>
  
  <body>
  <table border=1 cellpading=2>
      <h2> Fornecedores com maior pagamento por mês</h2>
      <thead align='center'>
          <th><b>Mês</b></th>
          <th><b>Fornecedor</b></th>
          
          <th><b>Pagamento</b></th>
       </thead>
       <tbody align='center'>
           {}
       </tbody>
   </table>   
   </body>
   </html>
   """.format(tabela)
file.write(html)
file.close()
print('Olhe sua pasta raiz, o seu arquivo já está pronto :L ')

  