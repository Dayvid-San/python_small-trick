# Small Tricks
Pequenas ferramentas e truques usando python

### Não se perca! ;)
<ul>
    <li>
        <a href="#json">Add arquivos JSON</a>
    </li>
    <li>
        <a href="#interface">Interface Gráfica Simples</a>
    </li>
    <li>
        <a href="#pdf">Criar PDF</a>
    </li>
</ul>


## Transformar em executavel
No terminal, digite:
$ pip install pyinstaller <br>
$ pyinstaller 'nome do arquivo'


## <div name='json'>Adicionar .json</div>
````py
import json

# code
# json.dump indica primeiro o nome da variavel e depois o tipo de arquivo em quserá transformada
with open(r'.\dados.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)

````

## <div name='interface'>Interface simples</div>
````bash
pip install PySimpleGUI
````

Para escolher o tema:<br>
````py
sg.theme('Nome do tema')
````

Para adicionar os elementos da janela:
````py
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar login')],
    [sg.Button('Entrar')]
]
````


### Estilização
O **size** define o tamanho 



## <div name='pdf'>Criar PDF</div>
````bash
pip install reportlab
````

