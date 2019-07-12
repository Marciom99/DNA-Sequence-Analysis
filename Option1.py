from sys import exit
import Interface, Modulos

#erro geral, quando ele pede o indice, se der 01 ele fica 1, tentar remover isso mais ha frente


def exercicio1():

    escolha = str(input(f"""
            1
            {'*'*20}
            \ta. Inserir manualmente uma sequência
            \tb. Gerar uma sequência aleatória
            \tc. Mostrar número total de elementos de uma sequência
            \td. Mostrar o número de ocorrências de uma determinada base ou sub-sequência e uma lista
             dos respeitos indices
            \te. Mostrar as frequências de um determiando conjunto de bases ou subsequências (número 
            total e relativo(%) de cada base)
            \tf. Mostrar uma sequência complementar (trocam os 'A' e 'T', 'G' e 'C')
            \tg. Voltar ao Menu anterior
            \th. Sair do Programa
            {'*'*20}\n
                """))



    if escolha.lower() == 'a':
        return exercicio1A()

    elif escolha.lower() == 'b':
        return exercicio1B()

    elif escolha.lower() == 'c':
        return exercicio1C()

    elif escolha.lower() == 'd':
        return exercicio1D()

    elif escolha.lower() == 'e':
        return exercicio1E()

    elif escolha.lower() == 'f':
        return exercicio1F()

    elif escolha.lower() == 'g':

        return Interface.interface()

    elif escolha.lower() == 'h':
        exit()

    else:
        print('Opção invalida')
        return exercicio1()


def exercicio1A():
        seq = Modulos.CriarSeq(1)
        print(seq)
        Interface.List.ListaSeq.append(seq)
        return exercicio1()


def exercicio1B():
   seq = Modulos.CriarSeq(2)
   Interface.List.ListaSeq.append(seq)
   return exercicio1()


def exercicio1C():
    ver = Modulos.Verlista()
    if ver == False:
        return exercicio1()

    Modulos.Contagem()

    while True:
        try:
            escolha = int(input('Escolha um indice valido para mostrar o número de nucleotidos na sequencia:'))

            print(f'A sequencia {Interface.List.ListaSeq[escolha]} tem {len(Interface.List.ListaSeq[escolha])} nucleotidos')
            return exercicio1()
        except (ValueError,IndexError):
            print('Indice Invalido, escolha  um válido')


def exercicio1D():
    ver = Modulos.Verlista()
    if ver ==False:
        return exercicio1()

    Modulos.Contagem()

    while True:
        try:
                escolha = int(input('Escolha um indice valido para mostrar o número de nucleotidos na sequencia:'))
                analise = Interface.List.ListaSeq[escolha]

                listaIndice = list()
                ocorrencias = 0
                localizar = str(input('Digite uma base ou uma subsequencia que seja procurada:')).upper()
                for i, v in enumerate(analise):
                    a = i
                    trace = ""
                    try:
                        while len(trace) - 1 < len(localizar) - 1:
                            trace += analise[a]
                            a += 1
                        if localizar == trace:
                            listaIndice.append(i)
                            ocorrencias += 1

                    except IndexError:
                            print("pelo except")

                if ocorrencias == 0:
                    print('Não foram encontradas ocorrencias')
                else:
                    print(listaIndice)
                    print(ocorrencias)
                    print("pelo normal")
                return exercicio1()

        except (ValueError,IndexError):
                print('Indice invalido, escolha um válido')


def exercicio1E():
    ver = Modulos.Verlista()
    if ver == False:
        return exercicio1()

    Modulos.Contagem()

    while True:
            try:
                escolha = int(input('Escolha um indice valido para mostrar o número de nucleotidos na sequencia:'))
                analise = Interface.List.ListaSeq[escolha]

                localizar = str(input('Escolha uma base ou sub-sequencia para mostrar a sua frequencia relativa:')).upper()
                ocorrencias = analise.count(localizar)
                print(f'Numero total {ocorrencias}')
                print(f'A sua percentagem relativa é {((len(localizar)*ocorrencias) / len(analise)) * 100:.2f}%')
                return exercicio1()

            except (ValueError, IndexError):
                print('Indice invalido, escolha um válido')


def exercicio1F():
    ver = Modulos.Verlista()
    if ver == False:
        return exercicio1()

    Modulos.Contagem()

    while True:
        try:
            escolha = int(input('Escolha um indice valido para mostrar o número de nucleotidos na sequencia:'))
            analise = Interface.List.ListaSeq[escolha]

            complementar = ''
            for letra in analise:
                if letra == "A":
                    complementar+="T"
                elif letra == "T":
                    complementar+="A"
                elif letra == "G":
                    complementar+="C"
                elif letra == "C":
                    complementar+="G"
                else:
                    complementar+='-'
            print(complementar)
            return exercicio1()

        except (ValueError,IndexError):
            print('Escolhe um indice invalido, escolha um válido')


