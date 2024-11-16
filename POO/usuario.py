class Usuario:
    def __init__(self, nome, email, senha):
        self.nome=nome
        self.email=email
        self.senha=senha

    def login(self, email, senha):
        return self.email == email and self.senha == senha