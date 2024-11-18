from usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome=None, email=None, senha=None):
        super().__init__(nome, email, senha)

    def entrar_em_contato(self):
        print(f"O e-mail para contato do usuário é {self.email}")

    def cliente_interface(self, catalogo, users):
        while True:
            print("\n=== Cliente Menu ===")
            print("1. Ver Imóveis Disponíveis")
            print("2. Imóveis Disponíveis para Alugar")
            print("3. Imóveis Disponíveis para Comprar")
            print("4. Alugar Imóvel")
            print("5. Comprar Imóvel")
            print("6. Suporte")
            print("7. Sair")
            choice = input("Escolha uma opção: ")

            if choice == "1":
                print("\nImóveis disponíveis:")
                catalogo.exibir_imoveis()

            elif choice == "2":
                print("\n=== Imóveis Disponíveis para Alugar ===")
                for imovel in catalogo.imoveis:
                    if imovel.status == "disponivel_aluguel":
                        print(imovel)

            elif choice == "3":
                print("\n=== Imóveis Disponíveis para Comprar ===")
                for imovel in catalogo.imoveis:
                    if imovel.status == "disponivel_venda":
                        print(imovel)

            elif choice == "4":
                endereco_rua = input("Digite o endereço (Rua) do imóvel que deseja alugar: ")
                numero = int(input("Digite o número do imóvel: "))
                for imovel in catalogo.imoveis:
                    if imovel.endereco.rua == endereco_rua and imovel.endereco.numero == numero:
                        catalogo.alugar(imovel.endereco)
                        break
                else:
                    print("Imóvel não encontrado.")

            elif choice == "5":
                endereco_rua = input("Digite o endereço (Rua) do imóvel que deseja comprar: ")
                numero = int(input("Digite o número do imóvel: "))
                for imovel in catalogo.imoveis:
                    if imovel.endereco.rua == endereco_rua and imovel.endereco.numero == numero:
                        catalogo.comprar(imovel.endereco)
                        break
                else:
                    print("Imóvel não encontrado.")

            elif choice == "6":
                print("Corretores: \n")
                for user in users:
                    if isinstance(user, Usuario) and type(user).__name__ == "Corretor":
                        print(f"Nome: {user.nome}, E-mail: {user.email}, CRECI: {user.creci_num}.\n")

            elif choice == "7":
                print("Saindo...")
                break

            else:
                print("Opção inválida. Tente novamente.")