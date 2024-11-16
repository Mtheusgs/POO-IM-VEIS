# main.py
from catalogo import Catalogo
from imovel import Imovel
from cliente import Cliente
from corretor import Corretor

def main():
    # Cria o catalogo
    catalogo = Catalogo()

    # Coloca algumas propriedades ao catalogo
    imovel1 = Imovel("123 Rua Principal", "Apartamento", 80, 150000, "disponivel", True, 3, True, False, "Bom apartamento.")
    imovel2 = Imovel("456 Rua Lateral", "Casa", 120, 250000, "disponivel", True, 5, True, True, "Casa espacosa.")

    catalogo.adicionar_imovel(imovel1)
    catalogo.adicionar_imovel(imovel2)

    # Mostra as propriedades disponiveis
    print("Available properties:")
    catalogo.exibir_imoveis()

    # Realiza algumas operacoes
    catalogo.alugar("123 Rua Principal")
    catalogo.comprar("456 Rua Lateral")

    # Mostrar lista atualizada
    print("\nAtualizar propridades: ")
    catalogo.exibir_imoveis()

    # Criando cliente e corretor
    cliente = Cliente("John Doe", "john@example.com", "password123")
    corretor = Corretor("Alice Realtor", "alice@example.com", "realtorpass", "CRECI12345")

    # Supporte ao Cliente
    cliente.entrar_em_contato()

    # Informacao do Corretor
    print(corretor)

if __name__ == "__main__":
    main()
