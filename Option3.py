from sys import exit
import Interface, Modulos
from Bio import pairwise2
from Bio.pairwise2 import format_alignment


def exercicio3():
    escolha = str(input(f"""
            3
            {'*'*20}
            \ta. Apagar um elemento da sequência, substituindo-o por ‘-‘
            \tb. Adicionar um novo elemento ‘-‘ à sequência, numa determinada posição
            \tc. Mostrar a distância de Hamming entre duas sequências com o mesmo comprimento.
            \td. Mostrar o número de matches e mismatches entre as duas sequências. Se uma sequência for
            de menor comprimento do que outra, essa diferença de comprimento entre as duas
            sequências deverá ser preenchida com ‘-‘. 
            \te. Alinhar duas sequências e guardar numa lista de sequencias alinhadas.
            \tf. Voltar ao Menu anterior
            \tg. Sair do Programa
            {'*'*20}\n
                """))


    if escolha.lower() == 'a':
        return exercicio3A()

    elif escolha.lower() == 'b':
        return exercicio3B()

    elif escolha.lower() == 'c':
        return exercicio3C()

    elif escolha.lower() == 'd':
        return exercicio3D()

    elif escolha.lower() == 'e':
        return exercicio3E()

    elif escolha.lower() == 'f':
        return Interface.interface()

    elif escolha.lower() == 'g':
        exit()

    else:
        print('Opção invalida')
        return exercicio3()


def exercicio3A():
    ver = Modulos.Verlista()
    if ver ==False:
        return exercicio3()

    Modulos.Contagem()

    while True:
        try:
            escolha = int(input('Escolha um indice valido da lista:'))
            Interface.List.ListaSeq[escolha]
            while True:
                try:
                    Eliminar = int(input(f'{Interface.List.ListaSeq[escolha]} - Escolha a posição do elemento que quer remover'))
                    assert Eliminar >0, 'Indice invalido'
                    erase = list(Interface.List.ListaSeq[escolha])
                    erase[Eliminar-1] = '-'
                    erase = ''.join(erase)
                    Interface.List.ListaSeq[escolha] = erase
                    return exercicio3()
                except (ValueError,IndexError,AssertionError):
                    print('Escolha uma posição válida')

        except (ValueError,IndexError):
            print('Escolhe um indice invalido, escolha um válido')


def exercicio3B():
    ver = Modulos.Verlista()
    if ver == False:
        return exercicio3()

    Modulos.Contagem()

    while True:
        try:
            escolha = int(input('Escolha um indice valido da lista:'))
            Interface.List.ListaSeq[escolha]
            while True:
                try:
                    Adicionar = int(input(f'{Interface.List.ListaSeq[escolha]} - Escolha a posição do elemento que para adicionar'))
                    assert Adicionar > 0, 'Indice invalido'
                    add = list(Interface.List.ListaSeq[escolha])
                    add.insert(Adicionar - 1,'-')
                    add = ''.join(add)
                    Interface.List.ListaSeq[escolha] = add
                    return exercicio3()
                except (ValueError, IndexError, AssertionError):
                    print('Escolha uma posição válida')

        except (ValueError, IndexError):
            print('Escolhe um indice invalido, escolha um válido')


def exercicio3C():
    ver = Modulos.Verlista()
    if ver == False:
        return exercicio3()

    comparar = 0
    for ind,v1 in enumerate(Interface.List.ListaSeq):
        listaComp = Interface.List.ListaSeq.copy()
        del(listaComp[ind])
        for v2 in listaComp:
            if len(v1) == len(v2):
                comparar+=1


    if comparar<=0:
        print('Não é possivel fazer a distância usando a lista atual')
        return exercicio3()

    Modulos.Contagem()

    while True:
        try:
            escolha1 = int(input('Escolha um indice valido da lista:'))
            Interface.List.ListaSeq[escolha1]
            escolha2 = int(input('Escolha outro indice valido da lista que seja diferente do primeiro:'))
            Interface.List.ListaSeq[escolha2]
            assert escolha1!=escolha2, 'Não podem ser indices iguais'
            assert len(Interface.List.ListaSeq[escolha1])== len(Interface.List.ListaSeq[escolha2]), 'Não podem ter tamanhos diferentes'

            dif = Modulos.hamdist(Interface.List.ListaSeq[escolha1],Interface.List.ListaSeq[escolha2])
            print(f'Existem {dif} diferenças')
            return exercicio3()


        except (ValueError, IndexError,AssertionError):
            print('Escolhe um indice invalido, escolha um válido')


def exercicio3D():
    ver = Modulos.Verlista()
    if ver == False or len(Interface.List.ListaSeq)<=1:
        return exercicio3()

    Modulos.Contagem()

    while True:
        try:
            escolha1 = int(input('Escolha um indice valido da lista:'))
            Interface.List.ListaSeq[escolha1]
            escolha2 = int(input('Escolha outro indice valido da lista que seja diferente do primeiro:'))
            Interface.List.ListaSeq[escolha2]

            alignment = pairwise2.align.globalxx(Interface.List.ListaSeq[escolha1],Interface.List.ListaSeq[escolha2])
            for a in alignment:
                print(format_alignment(*a))
            return exercicio3()


        except (ValueError, IndexError):
            print('Escolhe um indice invalido, escolha um válido')


def exercicio3E():
    ver = Modulos.Verlista()
    if ver == False or len(Interface.List.ListaSeq) <= 1:
        return exercicio3()

    Modulos.Contagem()

    while True:
        try:
            escolha1 = int(input('Escolha um indice valido da lista:'))
            Interface.List.ListaSeq[escolha1]
            escolha2 = int(input('Escolha outro indice valido da lista que seja diferente do primeiro:'))
            Interface.List.ListaSeq[escolha2]

            alignment = pairwise2.align.globalxx(Interface.List.ListaSeq[escolha1], Interface.List.ListaSeq[escolha2])

            for ali in alignment:
                Interface.List.ListaAlinha.append(ali[0:2])

            print(f'Para este caso temos {len(Interface.List.ListaAlinha)} combinações para as sequências {Interface.List.ListaSeq[escolha1]} e {Interface.List.ListaSeq[escolha2]} que são')
            for i,v in enumerate(Interface.List.ListaAlinha):
                print(f'Combinação {i+1}: {v}')
            return exercicio3()


        except (ValueError, IndexError):
            print('Escolhe um indice invalido, escolha um válido')
