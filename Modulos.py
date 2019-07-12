import Interface
from random import choice


def Verlista():
    if len(Interface.List.ListaSeq) ==0:
        print('O len é 0')
        return False
    else:
        return


def Contagem():
    print('Sequências da Lista')
    for ind, seq in enumerate(Interface.List.ListaSeq):
        print(f'Indice {ind} - {seq}')
    return


def CriarSeq(option):

    if option ==1:
        sequencia = str(input('Introduza manualmente uma sequencia usando AGTC:')).upper()
        if len(sequencia) ==0:
            print('A sequencia não contem nucleotidos')
            return CriarSeq(option)
        for letra in sequencia:
            if letra not in "atgc".upper():
                print('Sequencia contem caracteres invalidos')
                return CriarSeq(option)
        return sequencia

    elif option ==2:
        try:
            lenght = int(input('Numero de bases na sequencia'))
            DNA = ""
            for i in range(lenght):
                DNA += choice('AGCT')
            print(DNA)
            return DNA

        except ValueError:
            print('Digitou um erro...')
            return CriarSeq(option)


def hamdist(seq1, seq2):

    differences = 0
    for n1, n2 in zip(seq1, seq2):
        if n1 != n2:
            differences += 1
    return differences