from usuario import Usuario
from imovel import Imovel, Endereco

class Corretor(Usuario):
    def __init__(self, nome=None, email=None, senha=None, creci_num=None):
        super().__init__(nome, email, senha)
        self.creci_num = creci_num

    def register(self):
        super().register()
        self.creci_num = input("Insira seu numero CRECI: ")
        print(f"Corretor {self.nome} registrado com sucesso com o email: {self.email} e CRECI: {self.creci_num}.")

    def corretor_interface(self, catalogo):
        while True:
            print("\n=== Corretor Interface ===")
            print("1. Cadastrar Propriedade")
            print("2. Remover Propriedade")
            print("3. Ver Situação da Propriedade")
            print("4. Sair")
            choice = input("Escolha uma opção: ")

            if choice == "1":
                print("\n=== Cadastrar Propriedade ===")
                rua = input("Endereço (Rua): ")
                numero = int(input("Endereço (Número): "))
                cep = input("Endereço (CEP): ")
                tamanho = int(input("Tamanho (m²): "))
                valor = float(input("Valor: "))
                
                print("Status (Digite uma opção):")
                print("1. Disponível para aluguel")
                print("2. Disponível para venda")
                print("3. Não disponível")
                status_choice = input("Escolha o status (1/2/3): ")

                if status_choice == "1":
                    status = "disponivel_aluguel"
                elif status_choice == "2":
                    status = "disponivel_venda"
                else:
                    status = "indisponivel"

                garagem = input("Garagem (Sim/Não): ").lower() == "sim"
                comodos = int(input("Número de Cômodos: "))
                mobiliado = input("Mobiliado (Sim/Não): ").lower() == "sim"
                descricao = input("Descrição: ")

                endereco = Endereco(rua, numero, cep)
                novo_imovel = Imovel(endereco, tamanho, valor, status, garagem, comodos, mobiliado, descricao)
                catalogo.adicionar_imovel(novo_imovel)
                print("Propriedade cadastrada com sucesso!")

            elif choice == "2":
                print("\n=== Remover Propriedade ===")
                rua = input("Endereço (Rua) da propriedade a ser removida: ")
                numero = input("Numero da propriedade a ser removida: ")
                catalogo.retirar_imovel(rua,numero)
                print("Propriedade removida, se existente.")

            elif choice == "3":
                print("\n=== Situação da Propriedade ===")
                for imovel in catalogo.imoveis:
                    if imovel.status == "disponivel_aluguel":
                        status = "Disponível para aluguel"
                    elif imovel.status == "disponivel_venda":
                        status = "Disponível para venda"
                    elif imovel.status == "alugado":
                        status = "Alugado"
                    elif imovel.status == "vendido":
                        status = "Vendido"
                    else:
                        status = "Indisponível"
                    print(f"{imovel.endereco.rua}, Nº{imovel.endereco.numero}, Status: {status}")


            elif choice == "4":
                print("Saindo...")
                break

            else:
                print("Opção inválida. Tente novamente.")