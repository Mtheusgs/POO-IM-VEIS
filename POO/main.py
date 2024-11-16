# main.py
from catalogo import Catalogo
from imovel import Imovel
from cliente import Cliente
from corretor import Corretor

def main():
    # Create a catalog
    catalogo = Catalogo()

    # Add some properties to the catalog
    imovel1 = Imovel("123 Main St", "Apartment", 80, 150000, "disponivel", True, 3, True, False, "Nice apartment.")
    imovel2 = Imovel("456 Side St", "House", 120, 250000, "disponivel", True, 5, True, True, "Spacious house.")

    catalogo.adicionar_imovel(imovel1)
    catalogo.adicionar_imovel(imovel2)

    # Display available properties
    print("Available properties:")
    catalogo.exibir_imoveis()

    # Perform some operations
    catalogo.alugar("123 Main St")
    catalogo.comprar("456 Side St")

    # Show updated list
    print("\nUpdated properties:")
    catalogo.exibir_imoveis()

    # Create a client and a realtor
    cliente = Cliente("John Doe", "john@example.com", "password123")
    corretor = Corretor("Alice Realtor", "alice@example.com", "realtorpass", "CRECI12345")

    # Client contacts support
    cliente.entrar_em_contato()

    # Realtor information
    print(corretor)

if __name__ == "__main__":
    main()
