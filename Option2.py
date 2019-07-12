from sys import exit
import Interface, Modulos



def exercicio2():
    escolha = str(input(f"""
            2
            {'*'*20}
            \ta. Inserir uma sequência
            \tb. Remover uma sequência
            \tc. Mostrar o número de ocorrências de uma determinada base ou sub-sequência e uma lista dos respetivos índices, em cada uma das sequências
            \td. Mostrar as frequências de um determinado conjunto de bases ou sub-sequências (número total e relativo(%) de cada base), em cada uma das sequências
            \te. Mostrar as sequências complementares
            \tf. Voltar ao Menu anterior
            \tg. Sair do Programa
            {'*'*20}\n
                """))


    if escolha.lower() == 'a':
        return exercicio2A()

    elif escolha.lower() == 'b':
        return exercicio2B()

    elif escolha.lower() == 'c':
        return exercicio2C()

    elif escolha.lower() == 'd':
        return exercicio2D()

    elif escolha.lower() == 'e':
        return exercicio2E()

    elif escolha.lower() == 'f':
        return Interface.interface()

    elif escolha.lower() == 'g':
         exit()

    else:
        print('Opção invalida')
        return exercicio2()


def exercicio2A():
    escolha = str(input('''Quer introduzir uma sequência
    1 - Manual
    2 - Aleatória
    '''))

    if escolha =='1':
        seq = Modulos.CriarSeq(1)
    elif escolha =='2':
        seq = Modulos.CriarSeq(2)
    else:
        print('Escolheu uma opção inválida')
        return exercicio2()

    if len(Interface.List.ListaSeq)>0:
        Modulos.Contagem()
        while True:
            try:
                opcao = int(input('Escolha um indice válido:'))
                Interface.List.ListaSeq.insert(opcao,seq)
                return exercicio2()

            except ValueError:
                print('Indice inválido, escolha um indice valido')

    else:
        print('A lista ainda não tem elementos.')
        Interface.List.ListaSeq.insert(0,seq)
        return exercicio2()


def exercicio2B():
    if len(Interface.List.ListaSeq)<0:
        print('Não existem sequências')
        return exercicio2()

    Modulos.Contagem()

    while True:
        try:
            opcao = int(input('Escolha um indice válido para remover uma sequencia:'))
            del(Interface.List.ListaSeq[opcao])
            return exercicio2()

        except (ValueError,IndexError):
            print('Indice inválido, escolha um indice valido')


def exercicio2C():
    ver = Modulos.Verlista()
    if ver == False:
        return exercicio2()

    localizar = str(input('Digite uma base ou uma subsequencia que seja procurada:')).upper()

    for ints,seq in enumerate(Interface.List.ListaSeq):
                listaIndice = list()
                ocorrencias = 0
                for i,v in enumerate(seq):
                    a = i
                    trace = ""
                    try:
                        while len(trace)-1 <len(localizar)-1:
                                trace+=seq[a]
                                a+=1
                        if localizar == trace:
                                listaIndice.append(i)
                                ocorrencias+=1

                    except IndexError:

                        print("pelo except")

                print(ints)
                print(listaIndice)
                print(ocorrencias)


    return exercicio2()


def exercicio2D():
    ver = Modulos.Verlista()
    if ver == False:
        return exercicio2()

    localizar = str(input('Digite uma base ou uma subsequencia que seja procurada:')).upper()
    for ind,seq in enumerate(Interface.List.ListaSeq):
        ocorrencias = seq.count(localizar)
        print(f'Numero total {ocorrencias}')
        print(f'Para o indice {ind} a percentagem relativa é {((len(localizar)*ocorrencias) / len(seq)) * 100:.2f}%')
    return exercicio2()


def exercicio2E():
    ver = Modulos.Verlista()
    if ver == False:
        return exercicio2()

    for ind,seq in enumerate(Interface.List.ListaSeq):
        complementar = ''
        print(f'Para o indice {ind} temos o complementar ', end='')
        for nuc in seq:
            if nuc =='A':
                complementar+='T'
            elif nuc == 'T':
                complementar += 'A'
            elif nuc == 'G':
                complementar += 'C'
            elif nuc =='C':
                complementar += 'G'
            else:
                complementar+='-'
        print(complementar)
    return exercicio2()
