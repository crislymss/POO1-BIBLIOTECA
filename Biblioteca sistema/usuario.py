
class Usuario():
    def __init__(self, nome, usuario_id):
        self._nome = nome
        self._usuario_id = usuario_id
        self._livros_emprestados = []
        self._emprestimos_devolvidos = []

    @property
    def obter_nome(self):
        return self._nome

    @obter_nome.setter
    def obter_nome(self, novo_nome): 
        self._nome = novo_nome

    @property
    def obter_usuario_id(self):
        return self._usuario_id

    @property
    def obter_livros_emprestados(self):
        return self._livros_emprestados

    @property
    def obter_emprestimos_devolvidos(self):
        return self._emprestimos_devolvidos

    def adicionar_emprestimo(self, emprestimo):
        self._livros_emprestados.append(emprestimo)

    def adicionar_emprestimo_devolvido(self, emprestimo):
        self._emprestimos_devolvidos.append(emprestimo)

    @classmethod
    def documentation(self):
        return """
            Classe Usuario: 
                Essa classe é essencial para rastrear as atividades do empréstimo e devolução  de cada 
                usuáriona biblioteca. Cada vez que um livro é emprestado ou devolvido, o usuário 
                correspondente terá seus registros atualizados. Isso permite que a biblioteca acompanhe os livros
                emprestados por cada usuario.
                        
            Atributos da classe Usuário: 
                -> _nome : Armazena o nome do usuário
                -> _usuario_id : Armazena o id unico do usuario
                -> _livros_emprestados : Lista que armazena empréstimos ativos(objetos da classe 'Empréstimo' )
                -> _emprestimos_devolvidos : Lista que armazena empréstimo ja devolvidos
                                            (objetos da  classe 'Emprestimo' )
            
            Método da classe Usuário: 
                -> obter_nome : Retorna o nome do usuário.
                -> obter_nome.setter : Permite alterar o nome do usuario
                -> obter_usuario_id : Retorna o id do usuario
                -> obter_livros_emprestados : Retorna a lista de empréstimos ativos
                -> obter_emprestimos_devolvidos : Retorna a lista de empréstimos já devolvidos
                -> adicionar_emprestimo(emprestimo): Adiciona um objeto 'Emprestimo' a lista de empréstimos ativos
                -> adicionar_emprestimo_devolvido(emprestimo) : Adiciona um objeto 'Emprestimo' á 
                   lista de emprestimo devolvidos."""

