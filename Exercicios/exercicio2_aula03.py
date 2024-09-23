def entradaUsuario():
    global acao
    print('''
    1: Cadastrar novo aluno.
    2: Listar alunos cadastrados.
    3: Procurar aluno pelo nome.
    4: SAIR.
    ''')
    acao = int(input('O que deseja fazer? '))

def cadastraAluno():
    print('Cadastro de aluno. Preencha as informações:')
    ok = 0
    while(ok == 0):
        matricula = input('Matrícula: ')
        nome = input('Nome: ')
        email = input('E-mail: ')
        curso = input('Curso: ')
        if (not matricula or not nome or not email or not curso):
            print("Entrada vazia ! Redigite.\n")
        else:

            if (nome.isdigit()):
                print("Somente caracteres no nome !!! Redigite.\n")
            else:
                if (not matricula.isdigit()):
                    print("Somente números na matrícula !!! Redigite.\n")
                else:
                    ok = 1 
    else:
            aluno = f'{matricula},{nome}, {email}, {curso}\n'
 
    with open('alunos.txt', 'a', encoding='UTF-8') as arquivo:
        arquivo.write(aluno) 
        print('Cadastrado!!!\n')

def listaAluno():

    try:
 
        with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
            listaAlunos = arquivo.read().split('\n') 
        print('\nLista de alunos cadastrados:')
        print('Matrícula,Nome, Email, Curso')
        for aluno in listaAlunos: 
            print(aluno)

    except FileNotFoundError:
        print('Arquivo não existe. Cadastre primeiro !!!\n')

def procuraAluno():
    try:
        print('Buscar aluno por nome:')
        busca = input('Nome: ')
        if (not busca):
            print ('Entrada vazia !!!')
        else:
            with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
                listaAlunos = arquivo.read().split('\n') 
                resultado = None
            for aluno in listaAlunos:
                if (aluno):
                    nomeAluno = aluno.split(',')[1].rstrip()
                    if busca == nomeAluno:
                        resultado = aluno 
                break
            if resultado == None: 
                print('\nNão foi encontrado nenhum aluno com esse nome.\n')
            else:
                print(resultado+'\n')
    except FileNotFoundError:
        print('Arquivo não existe. Cadastre primeiro !!!\n')


while True:
    entradaUsuario()
    if acao == 1:
        cadastraAluno()
    elif acao == 2:
        listaAluno()
    elif acao == 3:
        procuraAluno()
    elif acao == 4:
        break
    else:
        print('\n::::: Escolha uma das quatro opções! :::::\n')