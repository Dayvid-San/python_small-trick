from googlesearch import search
import json

query = input('O que está procurando hoje?\n')
numeroLinks = int(input('Qual o número de links eu devo mostrar?\n'))

result = list(
    search(
        query,
        lang='pt-br',
        num_results=numeroLinks
    )
)


with open(r'.\links.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)

print('Os seus links estão em prontos :)')