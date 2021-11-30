import random

def jogar():
    print('Bem vindo ao jogo da forca... Vamos  jogar!')

    frutas = ['banana', 'uva', 'morango', 'caqui', 'caju', 'mexerica', 'damasco', 'abacaxi', 'melancia']
    objetos = ['cadeira', 'geladeira', 'lapis', 'anel', 'porta', 'parafusadeira', 'martelo', 'computador']
    paises = ['holanda', 'australia', 'portugal', 'moçambique', 'israel', 'alemanha', 'frança', 'inglaterra']

    opção_valida = False

    while not opção_valida:
        escolha = int(input(''' 
        [1] Objetos 
        [2] Frutas 
        [3] Países 
        Escolha um tema: '''))

        if escolha == 1:
            numero_aleatorio = random.randrange(0, len(objetos))
            palavras_secretas = objetos[numero_aleatorio].upper()
            letras_certas = ['_' for letra in palavras_secretas]
            opção_valida = True

        elif escolha == 2:
            numero_aleatorio = random.randrange(0, len(frutas))
            palavras_secretas = frutas[numero_aleatorio].upper()
            letras_certas = ['_' for letra in palavras_secretas]
            opção_valida = True

        elif escolha == 3:
            numero_aleatorio = random.randrange(0, len(paises))
            palavras_secretas = paises[numero_aleatorio].upper()
            letras_certas = ['_' for letras in palavras_secretas]
            opção_valida = True

        else:
            print('Opção inválida! Escolha uma opção: ')
            opção_valida = False

    enforcado = False
    acertou = False
    erros = 0

    print(letras_certas)
    print('A palavra tem', len(letras_certas), 'letras')

    while not acertou and not enforcado:
        chute = input('Qual a letra? ')
        chute = chute.strip().upper()

        if chute in palavras_secretas:
            index = 0

            for letra in palavras_secretas:
                if chute == letra:
                    letras_certas[index] = letra

                index += 1

        else:
            erros += 1
            desenho_forca(erros)

        enforcado = erros == 7
        acertou  = '_' not in letras_certas
        print(letras_certas)

    if acertou:
        msg_ganhou()

    else:
        msg_perdeu(palavras_secretas)

def msg_ganhou():
    print('Parabéns, você ganhou!')
    print('      ____________        ')
    print("    ' ._==_==_==_. '      ")
    print("    .-\\:        /-.       ")
    print("   |  (|:.      |)  |      ")
    print("     '-|:.      |-'        ")
    print("       \\::.     /         ")
    print("        '::.   .'          ")
    print("          )  (            ")
    print("          '  '            ")
    print("       _'      '_         ")
    print("     ' __________ '       ")
def msg_perdeu(palavra_secreta):
    print('Xiiiii você foi enforcado.')
    print(f'A palavra era {palavra_secreta}.')

def desenho_forca(erros):
    print('  _________  ')
    print(' |/        | ')

    if erros == 1:
        print(' |        (_)    ')
        print(' |               ')
        print(' |               ')
        print(' |               ')

    if erros == 2:
        print(' |       (_)     ')
        print(' |        |      ')
        print(' |               ')
        print(' |               ')

    if erros == 3:
        print(' |       (_)      ')
        print(' |       \|       ')
        print(' |                ')
        print(' |                ')

    if erros == 4:
        print(' |       (_)      ')
        print(' |       \|/      ')
        print(' |                ')
        print(' |                ')

    if erros == 5:
        print(' |       (_)      ')
        print(' |       \|/      ')
        print(' |        |       ')
        print(' |                ')

    if erros == 6:
        print(' |       (_)      ')
        print(' |       \|/      ')
        print(' |        |       ')
        print(' |       /        ')

    if erros == 7:
        print(' |       (_)      ')
        print(' |       \|/      ')
        print(' |        |       ')
        print(' |       / \      ')

    print(' |          ')
    print('_|___       ')
    print()
if(__name__ == '__main__'):
    jogar()