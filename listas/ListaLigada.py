from .no import No

class ListaLigada():

    def __init__(self):
        self.__primeiro_no = None
        self.__ultimo_no = None
        self.__tamanho = 0

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
        self.__tamanho += 1

    def inserir_posicao(self, elemento, posicao):
        """ Método que insere um elemento da lista a partir de sua posição.
            Param:
                elemento: elemento a ser inserido na lista.
                posicao: posicao do elemento a ser inserido na lista.
            return: None"""
        if posicao >= self.__tamanho or posicao < 0:
            return -1
        elif posicao == 0:
            novo_no = No(elemento)
            novo_no.proximo = self.__primeiro_no
            self.__primeiro_no = novo_no
        elif self.__tamanho == posicao:
            novo_no = No(elemento)
            novo_no.proximo = self.__ultimo_no
            self.__ultimo_no = novo_no
        else:
            novo_no = No(elemento)
            no_anterior = self.recupera_no(posicao-1)
            no_atual = self.recupera_no(posicao)
            no_anterior.proximo = novo_no
            novo_no.proximo = no_atual
        self.__tamanho += 1

    def remover_elemento(self, elemento):
        """ Método que remove um elemento da lista por elemento.
            Param:
                elemento: elemento a ser removido da lista.
            return: None
        """
        if not self.contem(elemento):
            print("Não existe esse elemento na lista.")
        no_remover = self.indice_elemento(elemento)
        self.remover_posicao(no_remover)

    def remover_posicao(self, posicao):
        """ Método que remove um elemento da lista dada a sua posição.
            Param:
                posicao: posição do elemento a ser removido da lista.
            return: -1 se não existir a posição na lista.
        """
        if posicao >= self.__tamanho or posicao < 0:
            return -1
        elif posicao == 0:
            proximo_no = self.__primeiro_no.proximo
            self.__primeiro_no = None
            self.__primeiro_no = proximo_no
        elif posicao == self.__tamanho - 1:
            no_anteior = self.recupera_no(self.__tamanho - 2)
            no_anteior.proximo = None
            self.__ultimo_no = no_anteior
        else:
            no_remover = self.recupera_no(posicao)
            no_anteior = self.recupera_no(posicao - 1)
            no_anteior.proximo = no_remover.proximo
            no_remover.proximo = None
        self.__tamanho -= 1


    def esta_vazia(self):
        """
            Método que verifica se a lista está vazia.
            Param:
                None.
            return: True ou False.
        """
        return self.__tamanho == 0

    def contem(self, elemento):
        """ Método que verifica se existe um elemento na lista.
            Param:
                elemento: elemento a ser verificado.
            return: True ou False"""
        for index in range(self.__tamanho):
            no_atual = self.recupera_no(index)
            if no_atual.elemento == elemento:
                return True
        return False

    def indice_elemento(self, elemento):
        """ Método que verifica qual a posição do elemento na lista.
            Param:
                elemento: elemento a ser verificado.
            return: posição do elemento.
        """
        for index in range(self.__tamanho):
            no_atual = self.recupera_no(index)
            if no_atual.elemento == elemento:
                return index
        return False


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
        if posicao >= self.__tamanho or posicao < 0:
            return -1
        temp = self.__primeiro_no
        for index in range(posicao):
            temp = temp.proximo
        return temp
