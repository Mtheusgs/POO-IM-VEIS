from usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)

    def entrar_em_contato(self):
        print(f"O e-mail para contato do usuário é {self.email}")