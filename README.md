# fornecedores2

## Descrição

Segunda versão do exercício proposto em Python e HTML. Agora temos uma arquivo CSV como exemplo de entrada abaixo.

empresa,fornecedor,data,valor <br>
A,F1,2018-12-10,1000.00 <br>
A,F2,2018-12-11,1500.00 <br>
A,F2,2019-01-20,1500.00 <br>
A,F1,2019-01-20,2000.00 <br>
B,F2,2019-01-31,400.00  <br>
A,F3,2019-03-01,500.00  <br>
B,F3,2019-03-06,900.01  <br>
B,F1,2019-03-06,1400.00 <br>

E queremos obter a tabela em HTML da figura

![alt text](https://github.com/lcslima45/fornecedores2/blob/master/Screenshot%20from%202020-02-04%2014-25-21.jpg)


O objetivo agora é achar o fornecedor maximal cuja soma de pagamentos em um dado mês é máxima, ou seja, queremos achar o grupo de fornecedores cuja soma de pagamentos por empresa representa a soma máxima do conjunto de pagamentos. 

Para isso utilizaremos os scripts fornecedores3.py e construtor_html.py. 



Obs.: Foi reportado um bug na versão anterior na criação da chave-mês do dicionário que já foi devidamente consertado e simplificado.

## Execução

Baixe os arquivos fornecedores3.py e construtor_html.py, também baixe o arquivo pagamentos_sample.csv neste repositório. 

Ao terminar, abra o terminal e vá para a pasta onde estão os arquivos, aplique o comando

```
python3 construtor_html.py
```
Ao aplicar o comando a seguinte mensagem vai aparecer

```
python3 construtor_html.py
Insira o caminho do seu arquivo CSV
       
```
Você deve digitar o endereço do arquivo CSV no mesmo formato da entrada do exemplo da execução.
Caso o arquivo esteja na mesma pasta dos .py é só fazer o comando abaixo
```
python3 construtor_html.py
Insira o caminho do seu arquivo CSV
pagamentos_sample.csv       
```
Se não, faça algo parecido com esse comando:

```
python3 construtor_html.py
Insira o caminho do seu arquivo CSV
p/home/lima/Desktop/pagamentos_sample.csv       
```
O programa vai executar e gerar um arquivo html na mesma pasta que você salvou os .py

## Lógica de execução

No script referente ao arquivo fornecedores3.py
A função principal do script recebe uma entrada fornecida pelo usuário, que deve corresponder ao arquivo CSV na mesma forma que a do exemplo.

As linhas do CSV foram lidas e tratadas para uma estrutura de dados do tipo dicionário, onde são associdos um valor a uma chave. 

As chaves do dicionario é gerada na hora da leitura do arquivo e associa um mês com uma string da seguinte forma 

Ano-Mes <br>
2019-07 <br>
2019-10 <br>

Em cada chave do dicionário são salvos em uma lista as linhas do arquivo CSV que pertencem aquele mês, cada linha é um array com quatro posições, respectivamente: empresa, fornecedor, data, pagamento.

Uma vez que todos as linhas estão associdas com as suas respectivas chaves, podemos procurar o valor máximo de soma de pagamentos em cada mês. Para isso utilizaremos outro dicionário chamado soma_fornecedores que para cada mês vai guardar as somas dos fornecedores que foram pagos para aquele período de tempo. Após o armazenamento das somas, decidimos quem são os fornecedores com o valor máximo e salvamos no dicionário fornecedores_pagamento_maximo.
