"""
Padrão de Projeto Singleton Monostate em Python
Livro: Aprendendo Padrões de Projetos em Python, Autor Chetan Giridhar, 2016

Neste código:
- Atribuimos a variável de classe __shared_state à variável __dict__.
- O Python usa __dict__ para armazenar o estado de todos os objetos de uma classe.
- Atribuímos __shared_state propositalmente a todas as instâncias criadas.
- Quando criamos 'b1' e 'b2', temos dois objetos distintos.
- Os estados b1.__dict__ e b2.__dict__ são iguais.
- Mesmo que a variável x do objeto mude para o objeto b1, 
  a mudança será copiada para a variável __dict__ compartilhada entre todos os objetos.

Observações:
- __dict__ é uma variável especial em Python.
"""

class Borg:
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b1 = Borg()
b2 = Borg()

b1.x = 4

# b1 e b2 sçao objetos distintos
print("Borg Object 'b1': ", b1)
print("Borg Object 'b2': ", b2)

# b1 e b2 compartilham o mesmo estado
print("Object State 'b1': ", b1.__dict__)
print("Object State 'b2': ", b2.__dict__)