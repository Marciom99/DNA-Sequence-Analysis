from sys import exit
import Interface, Modulos

def exercicio4():
    escolha = str(input(f"""
                       O que pretende fazer?
                       {'*' * 20}
                       \ta. Carregar as sequências guardadas num ficheiro
                       \tb. Guardar uma sequência ou lista de sequências num ficheiro
                       \tc. Voltar ao Menu anterior
                       \td. Sair do Programa
                       {'*' * 20}\n
                           """))
    if escolha.lower() == 'a':
        return exercicio4A()
    elif escolha.lower() == 'b':
        return exercicio4B()
    elif escolha.lower() == 'c':
        return Interface.interface()
    elif escolha.lower() == 'd':
        exit()
    else:
        print('Opção Inválida')
        return exercicio4()


def exercicio4A():
    escolha = str(input('''Tem algum ficheiro criado com sequências?
                         1- Tem um ficheiro criado
                         2- Não tem um ficheiro criado'''))

    if escolha =='1':
        try:
            nome = str(input('Introduza o nome do ficheiro que contém sequências: '))
            ficheiro = open(nome,'r')
            dados = list(ficheiro.read().split())
            for seq in dados:
                Interface.List.ListaSeq.append(seq)
            print('Carregamento Concluido')
            return exercicio4()

        except FileNotFoundError:
            print('Esse ficheiro não existe')
            return exercicio4()

    elif escolha=='2':
        return exercicio4()
    else:
        print('Opção inválida')
        return exercicio4A()


def exercicio4B():
    escolha = str(input('''Quer guardar as sequências num ficheiro?
                             1- Sim
                             2- Não '''))

    if escolha=='1':
        nome = str(input('Introduza o nome do ficheiro que quer guardar as sequências: '))
        ficheiro = open(nome,'a')
        for seq in Interface.List.ListaSeq:
            ficheiro.write(seq + ' ')

        ficheiro.close()
        print('Saving Concluido')
        return exercicio4()

    elif escolha=='2':
        return exercicio4()
    else:
        print('Opção inválida')
        return exercicio4A()