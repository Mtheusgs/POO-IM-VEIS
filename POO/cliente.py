from usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome=None, email=None, senha=None):
        super().__init__(nome, email, senha)

    def entrar_em_contato(self):
        print(f"O e-mail para contato do usuário é {self.email}")

    def cliente_interface(self, catalogo):
        while True:
            print("\n=== Cliente Menu ===")
            print("1. Ver Imóveis Disponíveis")
            print("2. Sair")
            choice = input("Escolha uma opção: ")

            if choice == "1":
                print("\nImóveis disponíveis:")
                catalogo.exibir_imoveis()

            elif choice == "2":
                print("Saindo da interface Cliente.")
                break

            else:
                print("Opção inválida. Tente novamente.")