from abc import ABC, abstractmethod

class UsuarioInterface(ABC):
    @abstractmethod
    def register(self):
        """Abstract method for registering a user."""
        pass

    @abstractmethod
    def login(self):
        """Abstract method for logging in a user."""
        pass


class Usuario(UsuarioInterface):
    def __init__(self, nome=None, email=None, senha=None):
        self.nome = nome
        self.email = email
        self.senha = senha

    def register(self):
        print("=== Register ===")
        self.nome = input("Enter your name: ")
        self.email = input("Enter your email: ")
        self.senha = input("Create a password: ")
        

    def login(self, email:str, senha:str):
        if self.email == email and self.senha == senha:
            print(f"Welcome back, {self.nome}!")
            return True
        else:
            print("Invalid email or password.")
            return False
