from listas import ListaLigada as ll

class Fila():

    def __init__(self):
        self.__elementos = ll.ListaLigada()

    def enfileirar(self, elemento):
        self.__elementos.inserir(elemento)

    def esta_vazio(self):
        return self.__elementos.esta_vazia()

    def desenfileirar(self):
        if not self.__elementos:
            return None
        resultado = self.__elementos.recupera_no(0)
        self.__elementos.remover_posicao(0)
        return resultado.elemento

    def __str__(self):
        return self.__elementos.__str__()