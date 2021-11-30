from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'),sg.Input(key='usuario',size=(25,1))],
    [sg.Text('  Senha'),sg.Input(key='senha',password_char='*',size=(25,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de Login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Fernando' and valores['senha'] == '00112233':
            print('Seja Bem vindo Mutchatcho!')

# Tela simples usando a Biblioteca PySimpleGUI