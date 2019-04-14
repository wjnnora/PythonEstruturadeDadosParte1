from listas import ListaLigada as ll

class Fila():

    def __init__(self):
        self.__elementos = ll.ListaLigada()

    def enfileirar(self, elemento):
        """ Método que insere um elemento na fila.
            Param:
                elemento: elemento a ser inserido na fila.
            return: None
        """
        self.__elementos.inserir(elemento)

    def esta_vazio(self):
        """ Método que verifica se uma fila está vazia.
            Param:
                None
            return: True ou False.
            """
        return self.__elementos.esta_vazia()

    def desenfileirar(self):
        """ Método que desenfilera uma fila.
            Param:
                None
            return: retorna o primeiro elemento da fila.
        """
        if not self.__elementos:
            return None
        resultado = self.__elementos.recupera_no(0)
        self.__elementos.remover_posicao(0)
        return resultado.elemento

    def __str__(self):
        """ Método que retorna todos os elementos da fila.
            Param:
                None
            return: retorna todos os elementos da fila.
        """
        return self.__elementos.__str__()