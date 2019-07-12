from sys import exit
import Interface, Modulos
import matplotlib.pyplot as plt
import numpy as np

def exercicio5():
    escolha = str(input(f"""
                          O que pretende fazer?
                          {'*' * 20}
                          \ta. Mostrar num gráfico XY, a sequência de DNA (represente no eixo XX cada elemento da
                            sequência e no eixo YY o respetivo nucleótido representado por um número)
                          \tb. Mostrar uma figura com 4 gráficos do tipo histograma, para representar a distribuição de
                            cada nucleótido nas diferentes sequências.
                          \tc. Voltar ao Menu anterior
                          \td. Sair do Programa
                          {'*' * 20}\n
                              """))
    if escolha.lower() == 'a':
        return exercicio5A()
    elif escolha.lower() == 'b':
        return exercicio5B()
    elif escolha.lower() == 'c':
        return Interface.interface()
    elif escolha.lower() == 'd':
        exit()
    else:
        print('Opção Inválida')
        return exercicio5()


def exercicio5A():
    ver = Modulos.Verlista()
    if ver == False:
        return exercicio5()

    Modulos.Contagem()


    while True:
        try:
            escolha = int(input('Escolha um indice valido da lista:'))
            Interface.List.ListaSeq[escolha]
            IndiceL = list()
            Nuc= list()

            for ind,val in enumerate(Interface.List.ListaSeq[escolha]):
                IndiceL.append(ind)
                Nuc.append(val)

            plt.scatter(IndiceL,Nuc)
            plt.xticks(IndiceL)
            plt.title(f'Sequência {Interface.List.ListaSeq[escolha]}')
            plt.xlabel('Indice da sequencia')
            plt.ylabel('Nucleotido')
            plt.show()

            return exercicio5()


        except (ValueError, IndexError):
            print('Escolhe um indice invalido, escolha um válido')


def exercicio5B():
    ver = Modulos.Verlista()
    if ver == False:
        return exercicio5()

    LA = list()
    LG = list()
    LC = list()
    LT = list()
    for seq in Interface.List.ListaSeq:
        LA.append(seq.count('A'))
        LG.append(seq.count('G'))
        LC.append(seq.count('C'))
        LT.append(seq.count('T'))

    RA = np.arange(len(LA))
    RG = np.arange(len(LG))
    RC = np.arange(len(LC))
    RT = np.arange(len(LT))

    plt.figure(figsize=(30, 30))
    plt.subplot(2, 2, 1)
    plt.title('Nucleótido A')
    plt.xlabel('Indice da Sequência')
    plt.ylabel('Quantidade de nucleótidos')
    plt.bar(RA, LA)
    plt.xticks(RA)

    plt.subplot(2, 2, 2)
    plt.bar(RG, LG)
    plt.title('Nucleótido G')
    plt.xlabel('Indice da Sequência')
    plt.ylabel('Quantidade de nucleótidos')
    plt.xticks(RG)

    plt.subplot(2, 2, 3)
    plt.bar(RC, LC)
    plt.title('Nucleótido C')
    plt.xlabel('Indice da Sequência')
    plt.ylabel('Quantidade de nucleótidos')
    plt.xticks(RC)

    plt.subplot(2, 2, 4)
    plt.bar(RT, LT)
    plt.title('Nucleótido T')
    plt.xlabel('Indice da Sequência')
    plt.ylabel('Quantidade de nucleótidos')
    plt.xticks(RT)
    plt.show()

    return exercicio5()