class Vetor():

    def __init__(self, tamanho=0):
        self.__tamanho = tamanho
        self.__elemento = [None] * tamanho
        self.__posicao = 0

    def tamanho_vetor(self):
        """ Método que retorna o tamanho do vetor.
            Param: None.
        return: tamanho do vetor (int).
        """
        return len(self.__elemento)

    def __str__(self):
        """ Método que retorna uma string contendo todos os elementos do vetor separados por espaço.
            Param: None.
        return: string contendo todos os elementos do vetor.
        """
        return " ".join(str(i) for i in self.__elemento)

    def contem(self, elemento):
        """ Método que verifica a existência de um determinado elemento no vetor.
            Param: elemento a ser verificado.
        return: False ou True.
        """
        return elemento in self.__elemento

    def indice(self, elemento):
        """ Método que retorna o índice do elemento a ser verificado.
            Param: elemento a ser verificado.
        return: índice do elemento (int)3
        """
        if elemento in self.__elemento:
            return self.__elemento.index(elemento)
        else:
            return -1

    def inserir_elemento_posicao(self, posicao, elemento):
        """ Método que insere um elemento no vetor a partir de uma posição.
            Param: posicao que indica a posição que será inserido o elemento.
        return: None.
        """
        vetor_inicio = self.__elemento[:posicao] + [None]
        vetor_inicio[-1] = elemento
        vetor_final = self.__elemento[posicao:]
        self.__elemento = vetor_inicio + vetor_final
        self.__posicao += 1

    def inserir_elemento_final(self, elemento):
        """ Método que insere um elemento no vetor na última posição do vetor.
            Param: elemento a ser inserido no vetor.
        return: None.
        """
        if self.__posicao >= len(self.__elemento):
            self.__elemento += [None]
        self.__elemento[self.__posicao] = elemento
        self.__posicao += 1

    def remover_elemento(self, elemento):
        """ Método que remove um elemento do vetor a partir do seu valor.
            Param: elemento a ser removido da lista.
        return: -1 (False, caso o elemento a ser retirado não existe no vetor).
        """
        posicao = None
        if elemento in self.__elemento:
            posicao = self.__elemento.index(elemento)
            inicio_vetor = self.__elemento[:posicao]
            final_vetor = self.__elemento[posicao+1:]
            self.__elemento = inicio_vetor + final_vetor
            self.__posicao -= 1
        return -1

    def remover_elemento_por_posicao(self, posicao):
        if posicao >= 0 and posicao < len(self.__elemento):
            vetor_inicio = self.__elemento[:posicao]
            vetor_final = self.__elemento[posicao+1:]
            self.__elemento = vetor_inicio + vetor_final
            self.__posicao -= 1
        else:
            return -1

    def retornar_elemento(self, posicao):
        """ Método que retorna um elemento a partir da posição passada por parâmetro.
            Param: posição do elemento a ser retornado.
        return: elemento.
        """
        return self.__elemento[posicao]

    def retorna_todos_elementos(self):
        """ Método que retorna todos os elementos do vetor.
            Param: None
        return: uma lista contendo todos os elementos.
        """
        lista_elementos = []
        for i in range(len(self.__elemento)):
            if self.__elemento[i] is None:
                break
            lista_elementos.append(self.__elemento[i])
        return lista_elementos