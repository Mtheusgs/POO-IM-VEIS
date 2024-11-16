from catalogo import Catalogo
from imovel import Imovel
from cliente import Cliente
from corretor import Corretor


def register_user(user_type):
    """
    Handles the registration of either a Cliente or Corretor.
    """
    if user_type == "Cliente":
        cliente = Cliente()
        cliente.register()
        return cliente
    elif user_type == "Corretor":
        corretor = Corretor()
        corretor.register()
        return corretor


def login_user(users):
    """
    Handles the login of a user by checking the email and password.
    """
    print("\n=== Login ===")
    email = input("Enter your email: ")
    senha = input("Enter your password: ")

    for user in users:
        if user.email == email:
            if user.login():
                return user
    print("No user found with this email or invalid credentials.")
    return None


def main():
    # Initialize the catalog
    catalogo = Catalogo()

    # Add some properties to the catalog
    imovel1 = Imovel("123 Rua Principal", "Apartamento", 80, 150000, "disponivel", True, 3, True, False, "Bom apartamento.")
    imovel2 = Imovel("456 Rua Lateral", "Casa", 120, 250000, "disponivel", True, 5, True, True, "Casa espacosa.")

    catalogo.adicionar_imovel(imovel1)
    catalogo.adicionar_imovel(imovel2)

    # List to store registered users
    users = []

    while True:
        print("\n=== Real Estate System ===")
        print("1. Register as Client")
        print("2. Register as Realtor")
        print("3. Login")
        print("4. View Available Properties")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # Register as Client
            user = register_user("Cliente")
            users.append(user)

        elif choice == "2":
            # Register as Realtor
            user = register_user("Corretor")
            users.append(user)

        elif choice == "3":
            # Login
            user = login_user(users)
            if user:
                print(f"\nWelcome, {user.nome}! You are logged in as {type(user).__name__}.")

        elif choice == "4":
            # View Available Properties
            print("\nAvailable properties:")
            catalogo.exibir_imoveis()

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
