from usuario import Usuario

class Corretor(Usuario):
    def __init__(self, nome, email, senha, creci_num):
        super().__init__(nome, email, senha)
        self.creci_num=creci_num

    def entrar_em_contato(self):
        print(f"Corretor {self.nome}, CRECI: {self.creci_num} e seu email: {self.email}.")