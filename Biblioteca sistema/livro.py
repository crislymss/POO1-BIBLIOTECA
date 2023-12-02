from item import Item


class Livro(Item):
    def __init__(self, titulo, autor, disponivel=True):
        super().__init__(titulo, autor, disponivel)

    @property
    def obter_titulo(self):
        return self._titulo

    @property
    def obter_autor(self):
        return self._autor

    @property
    def esta_disponivel(self):
        return self._disponivel

    @property
    def definir_disponivel(self):
        return self._disponivel

    @definir_disponivel.setter
    def definir_disponivel(self, valor):
        self._disponivel = valor

    @classmethod
    def documentation(self):
        return """
            Classe Livro:
                A classe Livro é uma subclasse da classe abstrata 'Item' e representa um tipo especifico
                de item na biblioteca, que é um livro. Ela herda atributos e métodos da classe
                'Item' e também adiciona atributos e métodos específicos para representar as 
                características de um livro

            Atributos da classe Livro:
                -> A classe 'Livro' não adiciona atributos adicionais além dos herdados da classe 'Item'.

            Métodos da classe Livro:
                -> obter_titulo(self) : Implementa o método abstrato 'obter_titulo()' da classe Item . 
                                       Retorna o título do livro.
                -> obter_autor(self) : Implementa o método abstrato 'obter_autor()' da classe 'Item'.
                                       Retorna o autor do livro.
                -> esta_disponivel(self) : Implementa o método abstrato 'esta_disponivel()' da classe 'Item'.
                                           Retorna o status de disponibilidade do livro.
                -> definir_disponivel(self, valor) : Implementa o método abstrato 'definir_disponivel()' 
                                            da classe 'Item'. Permite definir o status de disponibilidade do livro."""

