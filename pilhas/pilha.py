from listas import lista_duplamente_ligada as ldl


class Pilha():

    def __init__(self):
        self.__elementos = ldl.ListaDuplamenteLigada()

    def empilhar(self, elemento):
        """ Método que empilha um elemento.
            Param:
                elemento: elemento a ser empilhado na pilha.
            return: None
        """
        self.__elementos.inserir(elemento)

    def esta_vazia(self):
        """ Método que verifica se uma pilha está vazia.
            Param:
                None
            return: True ou False.
        """
        return self.__elementos.esta_vazia()

    def desempilhar(self):
        """ Método que desempilha uma pilha.
            Param:
                None
            return: retorna o primeiro elemento da pilha.
        """
        if self.esta_vazia():
            return None
        resultado = self.__elementos.recupera_no(self.__elementos.tamanho - 1)
        self.__elementos.remover_posicao(self.__elementos.tamanho - 1)
        return resultado.elemento

    def __str__(self):
        """ Método que retorna todos os elementos de uma pilha.
            Param:
                None
            return: retorna todos os elementos de uma pilha.
        """
        return self.__elementos.__str__()