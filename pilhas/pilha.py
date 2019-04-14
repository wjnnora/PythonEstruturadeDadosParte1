from listas import lista_duplamente_ligada as ldl


class Pilha():
    def __init__(self):
        self.__elementos = ldl.ListaDuplamenteLigada()

    def empilhar(self, elemento):
        self.__elementos.inserir(elemento)

    def esta_vazia(self):
        return self.__elementos.esta_vazia()

    def desempilhar(self):
        if self.esta_vazia():
            return None
        resultado = self.__elementos.recupera_no(self.__elementos.tamanho - 1)
        self.__elementos.remover_posicao(self.__elementos.tamanho - 1)
        return resultado.elemento

    def __str__(self):
        return self.__elementos.__str__()