from datetime import datetime, timedelta
from livro import Livro
from emprestimo import Emprestimo
from usuario import Usuario
from datetime import datetime, timedelta



class Biblioteca:
    def __init__(self):
        self._livros = []
        self._usuarios = {}
        self._emprestimos = []

    def adicionar_livro(self, titulo, autor):
        for livro in self._livros:
            if livro.obter_titulo == titulo and livro.obter_autor == autor:
                print(
                    f"O livro '{titulo}' de '{autor}' já está cadastrado na biblioteca."
                )
                return  #sair sem adicionar o livro, porque ja ta cadastrado

        livro = Livro(titulo, autor)  #vou criar um objeto livro
        self._livros.append(livro)
        print(f"Livro '{titulo}' de '{autor}' adicionado à biblioteca.")

    def buscar_livro(self, titulo):
        for livro in self._livros:
            if livro.obter_titulo() == titulo:
                return livro
        return None

    def cadastrar_usuario(self, nome, usuario_id):
        if usuario_id in self._usuarios:
            print("Já existe um usuário com esse ID.")
            return
        usuario = Usuario(nome, usuario_id)
        self._usuarios[usuario_id] = usuario
        print(f"Usuário '{nome}' cadastrado com ID {usuario_id}.")

    def emprestar_livro(self, usuario_id, livro_titulo, livro_autor):
        usuario = self._usuarios.get(usuario_id)

        if usuario:
            if len(usuario.obter_livros_emprestados) >= 2:
                print(
                    f"{usuario.obter_nome} já tem 2 livros emprestados. Você precisa devolver um livro antes de pegar outro emprestado."
                )
                return

            livros_encontrados = [
                livro
                for livro in self._livros
                if livro.obter_titulo == livro_titulo
                and livro.obter_autor == livro_autor
            ]

            if not livros_encontrados:
                print(
                    f"O livro '{livro_titulo}' de '{livro_autor}' não está disponível na biblioteca."
                )
                return

            livro_disponivel = None
            for livro in livros_encontrados:
                if livro.esta_disponivel:
                    livro_disponivel = livro
                    break

            if livro_disponivel:
                data_emprestimo = datetime.now()
                data_devolucao = data_emprestimo + timedelta(
                    days=7
                )  # prazo para devolver é 7 dias
                livro_disponivel.definir_disponivel = (
                    False  # Definir o livro como indisponível
                )
                emprestimo = Emprestimo(
                    livro_disponivel, data_emprestimo, data_devolucao
                )
                usuario.adicionar_emprestimo(emprestimo)
                self._emprestimos.append(emprestimo)
                formato_data_hora = "%Y-%m-%d %H:%M:%S"
                print(
                    f"'{livro_disponivel.obter_titulo}' de '{livro_disponivel.obter_autor}' emprestado para {usuario.obter_nome}."
                )
                print(
                    f"Data do Empréstimo: {data_emprestimo.strftime(formato_data_hora)}"
                )
                print(
                    f"Prazo de Devolução: {data_devolucao.strftime('%Y-%m-%d')} (7 dias)"
                )
            else:
                print(
                    f"O livro '{livro_titulo}' de '{livro_autor}' não está disponível no momento."
                )

        else:
            print("Usuário não encontrado ou informações incorretas do livro")

    def devolver_livro(self, usuario_id, livro_titulo, livro_autor):
        usuario = self._usuarios.get(usuario_id)

        if usuario:
            emprestimos_ativos = usuario.obter_livros_emprestados

            emprestimo_encontrado = None
            for emprestimo in emprestimos_ativos:
                emprestimo_livro = emprestimo.obter_livro
                if (
                    emprestimo_livro.obter_titulo == livro_titulo
                    and emprestimo_livro.obter_autor == livro_autor
                ):
                    emprestimo_encontrado = emprestimo
                    break

            if emprestimo_encontrado:
                data_devolucao = datetime.now()
                emprestimo_encontrado.obter_livro.definir_disponivel = True
                emprestimo_devolvido = Emprestimo(
                    emprestimo_encontrado.obter_livro,
                    emprestimo_encontrado.obter_data_emprestimo,
                    data_devolucao,
                )
                usuario.adicionar_emprestimo_devolvido(emprestimo_devolvido)
                emprestimos_ativos.remove(emprestimo_encontrado)
                print(
                    f"'{emprestimo_encontrado.obter_livro.obter_titulo}' de '{emprestimo_encontrado.obter_livro.obter_autor}' devolvido por {usuario.obter_nome}."
                )
            else:
                print(
                    f"{usuario.obter_nome} não possui o livro '{livro_titulo}' de '{livro_autor}' emprestado."
                )
        else:
            print("Usuário não encontrado.")

    def mostrar_clientes(self):
        if not self._usuarios:
            print("Não há clientes cadastrados.")
            return

        print("\nCLIENTES CADASTRADOS:")
        for usuario_id, usuario in self._usuarios.items():
            print(f"ID: {usuario_id}, Nome: {usuario.obter_nome}")

    def mostrar_livros_cadastrados(self):
        if not self._livros:
            print("Não há livros cadastrados na biblioteca.")
            return

        print("\nLIVROS CADASTRADOS:")
        for livro in self._livros:
            disponibilidade = "Disponível" if livro.esta_disponivel else "Emprestado"
            print(
                f"Título: {livro.obter_titulo}, Autor: {livro.obter_autor}, Disponibilidade: {disponibilidade}"
            )

    def mostrar_relatorio_geral(self):
        total_livros = len(self._livros)
        total_usuarios = len(self._usuarios)

        print("\nRELATÓRIO GERAL DA BIBLIOTECA:")
        print(f"Total de Livros da biblioteca: {total_livros}")
        print(f"Total de Usuários da biblioteca: {total_usuarios}")

    def mostrar_historico_completo_emprestimos_id(self, usuario_id):
        usuario = self._usuarios.get(usuario_id)
        if usuario:
            historico_emprestimos = (
                usuario.obter_livros_emprestados + usuario.obter_emprestimos_devolvidos
            )
            if historico_emprestimos:
                print(
                    f"\nHISTÓRICO COMPLETO DE EMPRÉSTIMOS PARA O USUÁRIO {usuario.obter_nome} (ID: {usuario.obter_usuario_id}):"
                )
                for emprestimo in historico_emprestimos:
                    formato_data_hora = "%Y-%m-%d %H:%M:%S"
                    data_emprestimo_formatada = (
                        emprestimo.obter_data_emprestimo.strftime(formato_data_hora)
                    )
                    data_devolucao_formatada = emprestimo.obter_data_devolucao.strftime(
                        formato_data_hora
                    )
                    status = (
                        "Devolvido"
                        if emprestimo in usuario.obter_emprestimos_devolvidos
                        else "Em andamento"
                    )
                    livro = emprestimo.obter_livro
                    print(f"Título do Livro: {livro.obter_titulo}")
                    print(f"Autor do Livro: {livro.obter_autor}")
                    print(f"Data de Empréstimo: {data_emprestimo_formatada}")
                    print(f"Data de Devolução: {data_devolucao_formatada}")
                    print(f"Status: {status}")
                    print("=" * 40)
            else:
                print("Nenhum histórico de empréstimos encontrado para este usuário.")
        else:
            print("Usuário não encontrado.")

    def remover_cliente(self, usuario_id):
        usuario = self._usuarios.get(usuario_id)
        if usuario:
            if any(
                not emprestimo.obter_livro.esta_disponivel
                for emprestimo in usuario.obter_livros_emprestados
            ):
                print(
                    "Não é possível remover esse cliente. Ele pegou livros e não os devolveu ainda."
                )
            else:
                del self._usuarios[usuario_id]
                print(f"Usuário com ID {usuario_id} removido.")
        else:
            print("Usuário não encontrado.")

    def remover_livro_biblioteca(self, titulo, autor):
        livro_encontrado = None
        for livro in self._livros:
            if livro.obter_titulo == titulo and livro.obter_autor == autor:
                livro_encontrado = livro
                break

        if livro_encontrado:
            if any(
                not emprestimo.obter_livro.esta_disponivel
                for emprestimo in self._emprestimos
            ):
                print(
                    "Não é possível remover esse livro. Ele está emprestado no momento."
                )
            else:
                self._livros.remove(livro_encontrado)
                print(f"Livro '{titulo}' de '{autor}' removido da biblioteca.")
        else:
            print(f"O livro '{titulo}' de '{autor}' não foi encontrado na biblioteca.")

    @classmethod
    def documentation(self):
        return """
            Classe Biblioteca: 
                        
                A classe 'Biblioteca é basicamente o núcleo do sistema bibliotecário e coordena as operações
                relacionadas a administração dos livros, clientes(usuários) e empréstimo.
            
            Atributos da classe Biblioteca:
                -> _livros : Uma lista que armazena objetos do tipo 'Livro', ou seja, 
                             livros cadastrados na biblioteca
                -> _usuarios : Um dicionario que associa IDs de usuario a objetos da classe Usuario
                -> _emprestimo : Uma lista que armazena objetos do tipo 'Emprestimo'. 
                        
            Métodos da classe Biblioteca: 
                -> adicionar_livro(titulo, autor): Adiciona um novo livro na biblioteca
                -> buscar_livro(titulo): Busca um livro na biblioteca pelo titulo
                -> cadastrar_usuario(nome, usuario_id): Cadastra um novo usuario na biblioteca
                -> emprestar_livro(usuario_id, livro_titulo, livro_autor): Realiza o empréstimo de 
                                                                          um livro para um usuário.
                -> devolver_livro(usuario_id, livro_titulo, livro_autor): Registra a devolução de 
                                                                          um livro por um usuário.
                -> mostrar_clientes(): Mostra a lista de clientes cadastrados na biblioteca.
                -> mostrar_relatorio_geral(): Exibe um relatório geral com informações sobre livros e usuários.
                -> mostrar_livros_cadastrados(): Lista todos os livros cadastrados na biblioteca.
                -> mostrar_historico_completo_emprestimos_id(usuario_id): Mostra o histórico completo de 
                                                                          empréstimos de um usuário.
                -> remover_cliente(usuario_id): Remove um cliente (usuário) da biblioteca.
                -> remover_livro_biblioteca(titulo, autor): Remove um livro da biblioteca. """
