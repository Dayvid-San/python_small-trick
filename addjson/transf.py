import json

nome = str(input('Olá! Qual é o seu nome?\n'))
sobrenome = str(input('Sobrenome\n'))
idade = int(input('E a sua idade?\n'))
job = str(input('Com o que você trabalha?\n'))


dados = {
    'nome': nome,
    'sobrenome': sobrenome,
    'idade': idade,
    'ocupacao': job
}

with open(r'.\dados.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)