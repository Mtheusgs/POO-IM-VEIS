# catalogo.py
from imovel import Imovel

class Catalogo:
    def __init__(self):
        self.imoveis = []

    def adicionar_imovel(self, imovel):
        self.imoveis.append(imovel)

    def retirar_imovel(self, rua,numero):
        self.imoveis = [imo for imo in self.imoveis if imo.endereco.rua != rua and imo.endereco.numero != numero]

    def alugar(self, endereco):
        for imovel in self.imoveis:
            if imovel.endereco == endereco and imovel.status == "disponivel_aluguel":
                imovel.status = "alugado"
                print(f"{endereco.rua}, Nº{endereco.numero} foi alugado.")
                return
        print(f"{endereco.rua}, Nº{endereco.numero} não está disponível para alugar.")

    def comprar(self, endereco):
        for imovel in self.imoveis:
            if imovel.endereco == endereco and imovel.status == "disponivel_venda":
                imovel.status = "vendido"
                print(f"{endereco.rua}, Nº{endereco.numero} foi vendido.")
                return
        print(f"{endereco.rua}, Nº{endereco.numero} não está disponível para venda.")


    def vender(self, imovel):
        self.adicionar_imovel(imovel)
        print(f"{imovel.endereco} esta na lista para a venda.")

    def exibir_imoveis(self):
        for imovel in self.imoveis:
            print(imovel)
