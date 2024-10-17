"""
Padrão de Projeto Singleton Monostate (v2) em Python
Livro: Aprendendo Padrões de Projetos em Python, Autor Chetan Giridhar, 2016

Neste código:
- Ajustamos o método __new__ responsável pela criação da instância do objeto.
"""

class Borg:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj

b1 = Borg()
b2 = Borg()

b1.x = 4

# b1 e b2 sçao objetos distintos
print("Borg Object 'b1': ", b1)
print("Borg Object 'b2': ", b2)

# b1 e b2 compartilham o mesmo estado
print("Object State 'b1': ", b1.__dict__)
print("Object State 'b2': ", b2.__dict__)