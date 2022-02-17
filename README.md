# Small Tricks
Pequenas ferramentas

## Transformar em executavel
No terminal, digite:
$ pip install pyinstaller <br>
$ pyinstaller <nome do arquivo>


## adicionar .json 
````py
import json

# code
# json.dump indica primeiro o nome da variavel e depois o tipo de arquivo em quserá transformada
with open(r'.\dados.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)

````
