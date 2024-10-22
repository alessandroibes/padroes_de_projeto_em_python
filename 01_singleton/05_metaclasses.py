"""
Metaclasses em Python
Livro: Aprendendo Padrões de Projetos em Python, Autor Chetan Giridhar, 2016

Observação:
- O método especial __call__ do Python é chamado quando um objeto precisa ser criado para uma classe já existente.

Neste código:
- Quando instanciamos a classe int com int(4, 5), o método __call__ da metaclasse MyInt é chamado, o que significa que a metaclasse agora controla a instanciação do objeto.
"""


class MyInt(type):
    def __call__(cls, *args, **kwds):
        print("***** Here's My int *****", args)
        print("Now do whatever you want with these objects...")
        return  type.__call__(cls, *args, **kwds)
    

class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


i = int(4, 5)