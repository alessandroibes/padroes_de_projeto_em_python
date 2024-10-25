"""
Padrão de Projeto Simple Factory em Python
Livro: Aprendendo Padrões de Projetos em Python, Autor Chetan Giridhar, 2016

Neste código:
- Criamos um produto Abstract chamado Animal.Animal, é uma classe-base abstrata e tem o método do_say()
- Criamos dois produtos (cat e Dog) a partir da interface Animal e implementamos do_say() com os sons apropriados produzidos por esses animais
- ForestFactory é uma fábrica que tem o método make_sound()
- De acordo com o tipo de argumento passado pelo cliente, uma instância apropriada de Animal será criada em tempo de execução e o som correto será exibido

Observações:
- ABCMeta é a metaclasse especial do Python para criar uma classe Abstract
"""


from abc import ABCMeta, abstractmethod


class Animal(metaclass = ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


## fábrica forest definida
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()
    

## código do cliente
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)