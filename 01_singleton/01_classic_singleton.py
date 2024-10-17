"""
Padrão de Projeto Singleton clássico em Python
Livro: Aprendendo Padrões de Projetos em Python, Autor Chetan Giridhar, 2016

Teremos duas tarefas principais:
1) Permitiremos a criação de apenas uma instância da classe Singleton.
2) Se uma instância já existir, serviremos o mesmo objeto novamente.

Neste código:
- Sobrescrevemos o método __new__ para controlar a criação do objeto.
- O objeto s1 é criado com o método __new__, mas antes disso é feita uma verificação para saber se o objeto já existe.
- O método hasattr é usado para verificar se o objeto cls tem a propriedade instance, que confere se a classe já tem um objeto.
- No momento em que o objeto s1 é solicitado, hasattr() detecta que um objeto já existe e, então, s1 aloca a instância do objeto existente.

Observações:
- __new__ é um método especial do Python para instanciar objetos.
- hassattr é um método especial do Python para saber se um objeto tem determinada propriedade.
"""

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    
s1 = Singleton()
print("Object created", s1)

s2 = Singleton()
print("Object created", s2)
