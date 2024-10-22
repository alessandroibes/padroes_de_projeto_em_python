"""
Padrão de Projeto Singleton com Metaclasses em Python
Livro: Aprendendo Padrões de Projetos em Python, Autor Chetan Giridhar, 2016

Observação:
- para controlar a criação e inicialização de uma classe, as metaclasses sobrescrevem os métodos __new__ e __init__.
"""


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    

class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)