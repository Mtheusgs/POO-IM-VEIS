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
    users = []

    while True:
        print("\n=== Sistema de Imoveis ===")
        print("1. Registrar")
        print("2. Login")
        print("3. Sair")
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
                if type(user).__name__ == "Corretor":
                    user.corretor_interface(catalogo)
                elif type(user).__name__ == "Cliente":
                    user.cliente_interface(catalogo, users)
        elif choice == "3":
            print("Saindo do sistema. Tchau!")
            break

        else:
            print("Opcao Invalida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
