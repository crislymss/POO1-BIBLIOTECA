from livro import Livro
from emprestimo import Emprestimo
from usuario import Usuario
from biblioteca import Biblioteca
from documentation import Documentation
from item import Item



def exibir_menu():
    print("\n========== SISTEMA BIBLIOTECARIO ===========")
    print("\nMENU:")
    print("1. Cadastrar Cliente")
    print("2. Remover Cliente")
    print("3. Alterar Dados do Cliente")
    print("4. Cadastrar Livro")
    print("5. Emprestar Livro")
    print("6. Devolver Livro")
    print("7. Mostrar clientes cadastrados")
    print("8. Mostrar relatório geral")
    print("9. Mostrar livros cadastrados")
    print("10. Mostrar histórico do cliente pelo ID")
    print("11. Remover Livro da Biblioteca")
    print("12. Mostrar documentação")
    print("13. Sair")


if __name__ == "__main__":
    biblioteca = Biblioteca()

    while True:
        exibir_menu()
        try:
            opcao = input("Escolha uma opção: ")
        except:
            print('Escolha uma opção válida.')

        if opcao == "1":
            nome_cliente = input("Digite o nome do cliente: ")
            id_cliente = input("Digite o ID do cliente: ")
            biblioteca.cadastrar_usuario(nome_cliente, id_cliente)

        elif opcao == "2":
            id_cliente = input("Digite o ID do cliente a ser removido: ")
            biblioteca.remover_cliente(id_cliente)

        elif opcao == "3":
            id_cliente = input("Digite o ID do cliente a ser alterado: ")
            if id_cliente in biblioteca._usuarios:
                novo_nome = input("Digite o novo nome: ")
                biblioteca._usuarios[
                    id_cliente
                ].obter_nome = novo_nome  # Atribui o novo nome usando a propriedade
                print("Nome do cliente alterado.")
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":
            titulo_livro = input("Digite o título do livro: ")
            autor_livro = input("Digite o autor do livro: ")
            biblioteca.adicionar_livro(titulo_livro, autor_livro)

        elif opcao == "5":
            id_cliente = input("Digite o ID do cliente: ")
            titulo_livro = input("Digite o título do livro: ")
            autor_livro = input("Digite o autor do livro: ")
            biblioteca.emprestar_livro(id_cliente, titulo_livro, autor_livro)

        elif opcao == "6":
            id_cliente = input("Digite o ID do cliente: ")
            titulo_livro = input("Digite o título do livro: ")
            autor_livro = input("Digite o autor do livro: ")
            biblioteca.devolver_livro(id_cliente, titulo_livro, autor_livro)

        elif opcao == "7":
            biblioteca.mostrar_clientes()

        elif opcao == "8":
            biblioteca.mostrar_relatorio_geral()

        elif opcao == "9":
            biblioteca.mostrar_livros_cadastrados()

        elif opcao == "10":
            id_cliente = input(
                "Digite o ID do cliente para exibir o histórico de empréstimos: "
            )
            biblioteca.mostrar_historico_completo_emprestimos_id(id_cliente)

        elif opcao == "11":
            titulo_livro = input("Digite o título do livro a ser removido: ")
            autor_livro = input("Digite o autor do livro a ser removido: ")
            biblioteca.remover_livro_biblioteca(titulo_livro, autor_livro)

        elif opcao == "12":
            Documentation.register(Livro)
            Documentation.register(Emprestimo)
            Documentation.register(Usuario)
            Documentation.register(Biblioteca)
            Documentation.register(Item)

            while True:
                print("\nEscolha uma classe para ver a documentação: ")
                print("1. Livro")
                print("2. Empréstimo")
                print("3. Usuário")
                print("4. Biblioteca")
                print("5. Item")
                print("6. Voltar Para o Menu Original")

                escolha = input("informe a opcao desejada: ")

                if escolha == "1":
                    if issubclass(Livro, Documentation):
                        if not hasattr(biblioteca, "documentation"):
                            raise Exception("Não implementou o método documentação")

                        else:
                            print(Livro.documentation())

                    else:
                        print("Não é subclasse de Documetation")

                elif escolha == "2":
                    if issubclass(Emprestimo, Documentation):
                        if not hasattr(Emprestimo, "documentation"):
                            raise Exception("Não implementou o método documentação")

                        else:
                            print(Emprestimo.documentation())

                    else:
                        print("Não é subclasse de Documetation")

                elif escolha == "3":
                    if issubclass(Usuario, Documentation):
                        if not hasattr(Usuario, "documentation"):
                            raise Exception("Não implementou o método documentação")

                        else:
                            print(Usuario.documentation())

                    else:
                        print("Não é subclasse de Documetation")

                elif escolha == "4":
                    if issubclass(Biblioteca, Documentation):
                        if not hasattr(Biblioteca, "documentation"):
                            raise Exception("Não implementou o método documentação")

                        else:
                            print(Biblioteca.documentation())

                    else:
                        print("Não é subclasse de Documetation")

                elif escolha == "5":
                    if issubclass(Item, Documentation):
                        if not hasattr(Item, "documentation"):
                            raise Exception("Não implementou o método documentação")
                        
                        else:
                            print(Item.documentation())
                    else:
                        print("Não é subclasse de Documentation")
                         

                elif escolha == "6":
                    print("Voltando par o Menu principal...")
                    break

                else:
                    print("Opcao incorreta, tente novamente!")

        elif opcao == "13":
            print("Encerrando o sistema da biblioteca...")
            print("Sistema Encerrado!!")
            break

        else:
            print("Opção inválida. Tente novamente!")
