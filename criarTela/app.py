from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar login')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de login', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED: #Caso o usuário saia da aplicação
        break
    if eventos == 'Entrar':
        # Validação de usuários
        if valores['usuario'] == 'dayvid' and valores['senha'] == '1123456':
            print('Bem-vido! :)')
        else:
            print('Who are you?')