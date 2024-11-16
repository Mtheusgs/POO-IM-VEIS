# catalogo.py
from imovel import Imovel

class Catalogo:
    def __init__(self):
        self.imoveis = []

    def adicionar_imovel(self, imovel):
        self.imoveis.append(imovel)

    def retirar_imovel(self, endereco):
        self.imoveis = [imo for imo in self.imoveis if imo.endereco != endereco]

    def alugar(self, endereco):
        for imovel in self.imoveis:
            if imovel.endereco == endereco and imovel.status == "disponivel":
                imovel.status = "alugado"
                print(f"{endereco} has been rented.")
                return
        print(f"{endereco} is not available for rent.")

    def comprar(self, endereco):
        for imovel in self.imoveis:
            if imovel.endereco == endereco and imovel.status == "disponivel":
                imovel.status = "vendido"
                print(f"{endereco} has been sold.")
                return
        print(f"{endereco} is not available for sale.")

    def vender(self, imovel):
        self.adicionar_imovel(imovel)
        print(f"{imovel.endereco} is now listed for sale.")

    def exibir_imoveis(self):
        for imovel in self.imoveis:
            print(imovel)
