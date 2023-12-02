class Emprestimo:
    def __init__(self, livro, data_emprestimo, data_devolucao):
        self._livro = livro
        self._data_emprestimo = data_emprestimo
        self._data_devolucao = data_devolucao

    @property
    def obter_livro(self):
        return self._livro

    @property
    def obter_data_emprestimo(self):
        return self._data_emprestimo

    @property
    def obter_data_devolucao(self):
        return self._data_devolucao

    def calcular_periodo_emprestimo(self):
        return (self._data_devolucao - self._data_emprestimo).days

    @classmethod
    def documentation(self):
        return """
            Classe Empréstimo:
                A classe Emprestimo é responsável por armazenar as informações essenciais de um empréstimo,
                incluindo detalhes do livro,
                datas de empréstimo e devolução. O que facilita a acompanhar as transações de empréstimo e a
                calcular a duração do empréstimo.
                Com essa classe, a biblioteca pode gerenciar empréstimos e devoluções de maneira mais eficiente.

            Atributos da classe Empréstimo:
                -> _livro : Armazena o objeto do tipo 'Livro' que esta sendo emprestado.
                -> _data_emprestimo : Armazena a data em que o empréstimo foi feito.
                -> _data_devolucao : Armazena a data de devolução  esperada para o livro emprestado.

            Métodos da classe Empréstimo: 
                -> obter_livro(self) : Retorna o objeto do tipo 'Livro' que esta sendo emprestado.
                -> obter_data_emprestimo(self) : Retorna a data de empréstimo.
                -> obter_data_devolucao(self) : Retorna a data de devolução esperada"""

