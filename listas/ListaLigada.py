from .no import No

class ListaLigada():

    def __init__(self):
        self.__primeiro_no = None
        self.__ultimo_no = None
        self.__posicao = 0

    def inserir(self, elemento):
        """
            Método que insere um elemento na lista.
            Param:
                elemento: elemento que será inserido na lista.
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

    def inserir_posicao(self, elemento, posicao):
        """ Método que insere um elemento da lista a partir de sua posição.
            Param:
                elemento: elemento a ser inserido na lista.
                posicao: posicao do elemento a ser inserido na lista.
            return: None"""
        if posicao >= self.__posicao or posicao < 0:
            return -1
        elif posicao == 0:
            novo_no = No(elemento)
            novo_no.proximo = self.__primeiro_no
            self.__primeiro_no = novo_no
        elif self.__posicao == posicao:
            novo_no = No(elemento)
            novo_no.proximo = self.__ultimo_no
            self.__ultimo_no = novo_no
        else:
            novo_no = No(elemento)
            no_anterior = self.recupera_no(posicao-1)
            no_atual = self.recupera_no(posicao)
            no_anterior.proximo = novo_no
            novo_no.proximo = no_atual
        self.__posicao += 1

    def esta_vazia(self):
        """
            Método que verifica se a lista está vazia.
            Param:
                None.
            return: True ou False.
        """
        return self.__posicao == 0

    def __str__(self):
        """
            Método que retorna uma lista de elementos da lista.
            Param:
                None.
            return: lista de elementos."""
        temp = self.__primeiro_no
        elementos = ''
        while(temp):
            elementos += f' {temp.elemento}'
            temp = temp.proximo
        return elementos

    def recupera_no(self, posicao):
        """
            Método que retorna um elemento da lista a partir da posicão passada por parâmentro.
            Param:
                posição: posicao do elemento a ser retornado.
            return: elemento a ser recuperado."""
        if posicao >= self.__posicao or posicao < 0:
            return -1
        temp = self.__primeiro_no
        for index in range(posicao):
            temp = temp.proximo
        return temp
