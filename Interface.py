from sys import exit
import Option1,Option2,Option3,Option4,Option5

#erro geral, quando ele pede o indice, se der 01 ele fica 1, tentar remover isso mais ha frente

class List:
    ListaSeq = []
    ListaAlinha = []

def interface():
        print(List.ListaSeq)

        escolha = str(input(f"""
                    O que pretende fazer?
                    {'*' * 20}
                    \t1. Analisar uma sequências
                    \t2. Analisar um conjunto de sequências
                    \t3. Alinhar uma sequência
                    \t4. Operações com ficheiros de sequências
                    \t5. Visualizar
                    \t6. Sair
                    {'*' * 20}\n
                        """))
        if escolha=='1':
            return Option1.exercicio1()
        elif escolha =='2':
            return Option2.exercicio2()
        elif escolha =='3':
            return Option3.exercicio3()
        elif escolha =='4':
            return Option4.exercicio4()
        elif escolha =='5':
            return Option5.exercicio5()
        elif escolha == '6':
            exit()
        else:
            print('Opção Inválida')
            return interface()


if __name__ == '__main__':
    interface()

