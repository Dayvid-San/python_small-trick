import json

nome = str(input('Olá! Qual é o seu nome?\n'))
idade = int(input('E a sua idade?\n'))

dados = {
    'nome': nome,
    'idade': idade
}

with open(r'.\dados.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)