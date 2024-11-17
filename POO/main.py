from catalogo import Catalogo
from imovel import Imovel
from cliente import Cliente
from corretor import Corretor


def register_user(user_type):
    if user_type == "Cliente":
        cliente = Cliente()
        cliente.register()
        return cliente
    elif user_type == "Corretor":
        corretor = Corretor()
        corretor.register()
        return corretor


def login_user(users):
    print("\n=== Login ===")
    email = input("Insira seu email: ")
    senha = input("Insira sua senha: ")

    for user in users:
        if user.email == email:
            if user.login(email, senha) == True:
                return user
    print("Nenhum usuario com este email ou crediciais invalidas.")
    return None


def main():
    catalogo = Catalogo()

    imovel1 = Imovel("123 Rua Principal", "Apartamento", 80, 150000, "disponivel", True, 3, True, False, "Bom apartamento.")
    imovel2 = Imovel("456 Rua Lateral", "Casa", 120, 250000, "disponivel", True, 5, True, True, "Casa espacosa.")

    catalogo.adicionar_imovel(imovel1)
    catalogo.adicionar_imovel(imovel2)

    users = []

    while True:
        print("\n=== Sistema de Imoveis ===")
        print("1. Registrar")
        print("2. Login")
        print("3. Ver Imoveis Disponiveis")
        print("4. Sair")
        choice = input("Escolha uma opcao: ")

        if choice == "1":
            print("1. Registre como Cliente")
            print("2. Registre como Corretor")
            choice_type_user = input("Escolha uma opcao: ")

            if choice_type_user == "1":
                user = register_user("Cliente")
                users.append(user)
            if choice_type_user == "2":
                user = register_user("Corretor")
                users.append(user)

        elif choice == "2":
            user = login_user(users)
            if user:
                print(f"\nBem vindo, {user.nome}! Voce esta logado como {type(user).__name__}.")

        elif choice == "3":
            print("\nImoveis disponiveis:")
            catalogo.exibir_imoveis()

        elif choice == "4":
            print("Saindo do sistema. Tchau!")
            break

        else:
            print("Opcao Invalida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()
