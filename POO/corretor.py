from usuario import Usuario

class Corretor(Usuario):
    def __init__(self, nome=None, email=None, senha=None, creci_num=None):
        super().__init__(nome, email, senha)
        self.creci_num = creci_num

    def register(self):
        super().register()
        self.creci_num = input("Enter your CRECI number: ")
        print(f"Realtor {self.nome} registered successfully with email: {self.email} and CRECI: {self.creci_num}.")
