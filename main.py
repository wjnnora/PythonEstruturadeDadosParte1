from array import array
from vetores import vetor
from listas import ListaLigada as ll

# Cria um vetor de inteiros
# vetor_inteiros = array('b', [1, 2, 3])
# print(vetor_inteiros)
# print(vetor_inteiros.index(2))

flag = True
while(flag):
    print(20 * "-", "MENU", 20 * "-")
    print("1. Vetores")
    print("2. Listas ligadas")
    print("0. Sair")
    opcoes = [0, 1, 2]
    try:
        op = int(input("Digite a opção desejada: "))
        if op not in opcoes:
            raise ValueError
    except ValueError:
        print("A opção desejada não existe. Tente novamento.")
    if op == 0:
        flag = False
    if op == 1:
        vetor_1 = vetor.Vetor()
        vetor_1.inserir_elemento_posicao(0, 10)
        vetor_1.inserir_elemento_posicao(1, 5)
        vetor_1.inserir_elemento_posicao(2, 4)
        vetor_1.inserir_elemento_posicao(2, 6)
        # vetor_1.inserir_elemento_final(1)
        # vetor_1.inserir_elemento_final(2)
        # vetor_1.inserir_elemento_final(3)
        # vetor_1.inserir_elemento_final(4)
        # vetor_1.inserir_elemento_final(4)
        print(vetor_1.retorna_todos_elementos())
        print(vetor_1)
        print("Tamanho do vetor: {}".format(vetor_1.tamanho_vetor()))
        print(vetor_1.contem(10))
        print(vetor_1.indice(13))
        vetor_1.remover_elemento(10)
        print(vetor_1.retorna_todos_elementos())
        vetor_1.remover_elemento(4)
        print(vetor_1.retorna_todos_elementos())
        vetor_1.remover_elemento_por_posicao(4)
        print(vetor_1.retorna_todos_elementos())
        print(vetor_1.remover_elemento_por_posicao(20))
        print(vetor_1.retorna_todos_elementos())

    elif op == 2:
        lista_teste = ll.ListaLigada()
        lista_teste.inserir(1)
        lista_teste.inserir(2)
        lista_teste.inserir(3)
        lista_teste.inserir(4)
        print(lista_teste)
        print(lista_teste.recupera_no(4))