"""
Padrão de Projeto Singleton clássico em Python
Livro: Aprendendo Padrões de Projetos em Python, Autor Chetan Giridhar, 2016

Neste código:
- Quando fazemos s1 = Singleton(), o método __init__ é chamado, mas nenhum objeto novo é criado.
- Quando chamamos Singleton.getInstance() o objeto é criado.
"""

class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print(" __init__ method called.")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s1 = Singleton() # classe é inicilizada, mas o objeto não é criado
print("Object created", Singleton.getInstance()) # O objeto é criado aqui
s2 = Singleton() # instância já criada