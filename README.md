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
    <li>
        <a href="#gerandoSenhas">Gerador de senhas</a>
    </li>
    <li>
        <a href="#audioemvideo">Transformando vídeo em áudio</a>
    </li>
    <li>
        <a href="#aboutNumber">Descobrindo sobre o número</a>
    </li>
    <li>
        <a href="#cutImage">Cortando Imagem</a>
    </li>
    <li>
        <a href="#instaFollwers">Listando seguidores do instagram</a>
    </li>
</ul>


## Transformar em executavel
No terminal, digite:
````bash
$ pip install pyinstaller
$ pyinstaller 'nome do arquivo'
````

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

## <div name='gerandoSenhas'>Gerando senhas</div>
Necessário importar:
````py
import random
from string import digits
from string import punctuation
from string import ascii_letters
````

Primeiro juntamos todos os simbolos e letras:
````py
symbols = ascii_letters + digits + punctuation
````

e então os juntamos aleatóriamente com:
````py
password = "".join(secure_random.choice(symbols) for i in range(30)) 
````

## <div name='audioemvideo'>Transformando áudio em vídeo</div>
Necessário importar:
````bash
pip install moviepy
````

Primeiro carregamos o arquivo do vídeo
````py
video = moviepy.editor.VideoFileClip("video.mp4")
````

e então extraimos o áudio
````py
audio_data = video.audio
````

para depois criarmos o arquivo de áudio nomeando ele
````py
audio_data.write_audiofile("audio_do_video.mp3")
````

## <div name='aboutNumber'>Descobrindo sobre o numero</div>
Para descobrirmos mais sobre um número de telefone vamos usar a biblioteca **Phonenumbers**.<br>
Para instalar o **Phonenumbers**:
````bash
pip install phonenumbers
````

Primeiro, capturamos o numero de telefone e ajustamos para usar o phonenumbers
````py
telefone_ajustado = phonenumbers.parse(telefone)
````

Para descobrir a localização, usamos o Geocoder.
````py
from phonenumbers import geocoder
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
````

Bem! Para deixar o número no formato especifico do país de origem ou para o formato internacional, podemos usar o format_number
````py
telefone_formatado = phonenumbers.format_number(telefone_formulario_ajustado,phonenumbers.PhoneNumberFormat.NATIONAL)

telefone_internacional = phonenumbers.format_number(telefone_ajustado,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
````


## <div name="cutImage">Cortando Imagens</div>
Para cortar uma imagem é necessário importar o Pillow
````bash
pip install pillow
````

Carregar a imagem original
````py
imagem = Image.open(r'mia.jpg')
````

Passar as coordenadas
````py
esquerda, cima, direita, baixo = (250,10,500,250)
````

E então usar o **Crop** para cortar a Imagem
````py
imagem_cortada = imagem.crop((esquerda, cima, direita, baixo))
````


## <div name="instaFollwers">Listando seguidores do instagram</div>

Para isso é necessário importar o Instaloader.<br>
````bash
pip install instaloader
````

Carregue a função desejada dentro de uma variável e ponha a sua senha e usuário para login.

````py
insloa = instaloader.Instaloader()
insloa.login('Usuario', 'Senha')
````

Carregando seguidores e os que está seguindo
````py
followers = instaloader.Profile.from_username(insloa, 'dayvid_jr_').get_followers()
followees = instaloader.Profile.from_username(insloa, 'dayvid_jr_').get_followees()
````

Visualizando os dados
````py
# Seguidores
print(str(followers._data['count']))

# Seguindo
print(str(followees._data['count']))

# Informação de seguidores
print(str(followees._data['edges']))
````