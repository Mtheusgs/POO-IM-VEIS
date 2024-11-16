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
                print(f"{endereco} foi alugado.")
                return
        print(f"{endereco} nao esta disponivel para alugar.")

    def comprar(self, endereco):
        for imovel in self.imoveis:
            if imovel.endereco == endereco and imovel.status == "disponivel":
                imovel.status = "vendido"
                print(f"{endereco} foi vendido.")
                return
        print(f"{endereco} nao esta disponivel a venda.")

    def vender(self, imovel):
        self.adicionar_imovel(imovel)
        print(f"{imovel.endereco} esta na lista para a venda.")

    def exibir_imoveis(self):
        for imovel in self.imoveis:
            print(imovel)
