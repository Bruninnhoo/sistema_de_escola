import os

alunos = [
    {
        'nome': 'Bruno',
        'idade': '16',
        'notas': {
            'matematica': 8.5,
            'portugues': 6.0,
            'ingles': 8.0,
        },
        'media': 7.5,
    },
]

def main():
    os.system('cls')
    print('Sistema de notas')
    print('Selecione uma das opções abaixo\n')

    print('1 - Cadastrar aluno')
    print('2 - Exibir relátorio geral')
    print('3 - Buscar aluno')
    print('4 - Verificar menor nota')
    print('5 - Verificar maior nota')
    print('6 - Sair')

    opcao = input('\n-> ')

    if opcao == '1':
        cadastrar_aluno()
        fim_execução()
    if opcao == '2':
        exibir_relatorio()
        fim_execução()
    if opcao == '3':
        buscar_aluno()
        fim_execução()
    if opcao == '4':
        verificar_menor_media()
        fim_execução()
    if opcao == '5':
        verificar_maior_média()
        fim_execução()
    if opcao == '6':
        os.system('cls')
        sair()
    else:
        input('Opção selecionada desconhecida, Aperte Enter para voltar')
        main()

def fim_execução():
    print()
    input('Aperte ENTER para voltar ao menu')
    main()

def cadastrar_aluno():
    os.system('cls')
    nome = input('Digite o nome do aluno: ')
    while True:
        try:
            idade = int(input('Digite a idade do aluno: '))
            break
        except ValueError:
            print('O valor digitado não é um número')
    novo_aluno ={
        'nome': nome,
        'idade': idade,
        'notas': {}
    }
    for i in range(0, 3):
        nome_materia = input(f'Digite o nome da matéria {i + 1}: ')
        while True:
            try:
                nota_materia = float(input(f'Digite a nota de {nome_materia}: '))
                break
            except ValueError:
                os.system('cls')
                print('O valor digitado não é um número')

        novo_aluno['notas'][nome_materia] = nota_materia
    
    novo_aluno['media'] = calcular_media(novo_aluno)
    alunos.append(novo_aluno)

    exibir_relatorio(novo_aluno)

def exibir_relatorio(arg=None):
    if arg is None:
        print('=====Relatório=====')
        for aluno in alunos:
            print(f'Nome: ' + aluno['nome'])
            print(f'Idade: ' + aluno['idade'])

            for materia, nota in aluno['notas'].items():
                print(f'{materia}: {nota}')

            print(f'Média geral: {aluno['media']}')
            print()
    else:
        print(f'Nome: {arg['nome']}')
        print(f'Idade: {arg['idade']}')

        for materia, nota in arg['notas'].items():
            print(f'{materia}: {nota}')

        print(f'Média: {arg['media']}')
        print()
        

def buscar_aluno():
    busca = input('Digite o nome do aluno que deseja busca: ')
    for aluno in alunos:
        if aluno['nome'] == busca:
            exibir_relatorio(aluno)
            return
    print('Aluno não encontrado')
    

def sair():
    exit()

def calcular_media(arg=None):
    if arg is None:
        for aluno in alunos:
            somatoria = 0
            quantidade = 0

            for materia, nota in aluno['notas'].items():
                somatoria += nota
                quantidade += 1

            media_aluno = somatoria/quantidade

            print(round(media_aluno,2))

    else:
        somatoria = 0
        quantidade = 0

        for materia, nota in arg['notas'].items():
            somatoria += nota
            quantidade += 1

        media_aluno = somatoria/quantidade

        return round(media_aluno, 2)

def verificar_maior_média():
    maior_media = 0
    nome_aluno = ''

    for aluno in alunos:
        if aluno['media'] > maior_media:
            maior_media = aluno['media']
            nome_aluno = aluno['nome']
    
    print('===== Maior Média ======')
    print(f'{nome_aluno}: {maior_media}')

def verificar_menor_media():
    menor_media = 99999
    nome_aluno = ''

    for aluno in alunos:
        if aluno['media'] < menor_media:
            menor_media = aluno['media']
            nome_aluno = aluno['nome']
    
    print('===== Menor Média =====')
    print(f'{nome_aluno}: {menor_media}')

if __name__ == "__main__":
    main()

