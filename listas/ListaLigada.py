from .no import No

class ListaLigada():
    def __init__(self):
        self.__primeiro_no = None
        self.__ultimo_no = None
        self.__posicao = 0

    def inserir(self, elemento):
        """ Método que insere um elemento na lista.
            Param: elemento que será inserido na lista.
        return: None
        """
        novo_no = No(elemento)
        if self.esta_vazia():
            self.__primeiro_no = novo_no
            self.__ultimo_no = novo_no
        else:
            self.__ultimo_no.proximo = novo_no
            self.__ultimo_no = novo_no
        self.__posicao += 1

    def esta_vazia(self):
        """ Método que verifica se a lista está vazia.
            Param: None.
        return: True ou False.
        """
        return self.__posicao == 0

    def __str__(self):
        """ Método que retorna uma lista de elementos da lista.
            Param: None.
        return: lista de elementos."""
        temp = self.__primeiro_no
        elementos = ''
        while(temp):
            elementos += f' {temp.elemento}'
            temp = temp.proximo
        return elementos

    def recupera_no(self, posicao):
        """ Método que retorna um elemento da lista a partir da posicão passada por parâmentro.
            Param: posição do elemento a ser retornado.
        return: elemento a ser recuperado."""
        if posicao >= self.__posicao or posicao < 0:
            return -1
        temp = self.__primeiro_no
        for index in range(posicao):
            temp = temp.proximo
        return temp.elemento

    def inserir_posicao(self, elemento, posicao):
        if posicao >= self.__posicao or posicao < 0:
            return -1
        temp_inicio = self.__primeiro_no
        temp_fim = self.__ultimo_no
        for index in range(posicao):
            temp_inicio = temp_inicio.proximo
        temp_inicio.proximo = elemento
        temp_inicio = elemento