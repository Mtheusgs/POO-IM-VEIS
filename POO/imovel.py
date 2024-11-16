
class Endereco():
    def __init__(self, rua:str, numero:int, cep:str):
        self.rua = rua
        self.numero = numero
        self.cep = cep

class Categoria():
    def __init__(self, tipo:str):
        self.tipo = tipo#TODO: mudar para enum

class Imovel:
    def __init__(self, endereco:Endereco,categoria:Categoria,tamanho:int,valor:float,status:bool,garagem:bool,num_comodos:int,acessibilidade:bool,mobiliado:bool,descricao = None):
        self.endereco=endereco
        self.categoria=categoria
        self.tamanho=tamanho
        self.valor=valor
        self.status=status
        self.garagem=garagem
        self.comodos=num_comodos
        self.acessibilidade=acessibilidade
        self.mobiliado=mobiliado
        self.descricao=descricao

    def exibir_no_mapa(self):
        print(f"Mostrando link :  {self.endereco}")

    def fotos(self):
        print(f"Mostre fotos do {self.endereco}")

    def __str__(self):
        return f"{self.categoria} na  {self.endereco}, {self.tamanho} m^2, preço: {self.valor}"
    
if __name__ == '__main__':
    imovel01 = Imovel(
            Endereco('Rua tal', 123, '27373732772'),
            Categoria('comercial')
    )
            