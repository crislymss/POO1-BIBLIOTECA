from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, titulo, autor, disponivel=True):
        self._titulo = titulo
        self._autor = autor
        self._disponivel = disponivel

    @abstractmethod
    def obter_titulo(self):
        pass

    @abstractmethod
    def obter_autor(self):
        pass

    @abstractmethod
    def esta_disponivel(self):
        pass

    @abstractmethod
    def definir_disponivel(self, disponivel):
        pass

    @classmethod
    def documentation(self):
        return """
        Classe Item:
                    A classe Item é uma classe abstrata que serve como uma base para outros tipos
                    de itens que podem ser armazenados na biblioteca. Esta classe contém atributos e 
                    métodos que podem ser compartilhados por suas subclasses, como a classe Livro.

                    Atributos da Classe Item: 
                        -> _titulo : Esse atributo armazena o titulo do Item.
                        -> _autor : Esse atributo armazena o autor do item.
                        -> _disponivel : Esse atributo armazena um valor booleano 
                                        indicando se o item está disponivel ou não.

                    Métodos Abstratos:
                        -> obter_titulo() : Esse método abstrato deve ser implementado nas subclasses.
                                            Retorna o o titulo do item.
                        -> obter_autor() : Método abstrato que deve ser implementado nas subclasses.
                                            Retorna o autor do item.
                        -> esta_disponivel() : Método abstrato que dever ser implementado nas subclasses.
                                               Retorna indicando se o item esta disponivel
                        -> definir_disponivel (disponivel) : Método abstrato que deve ser implementado nas subclasses"""
