"""
Exemplo de Singleton em Python para conexão a banco de dados
Livro: Aprendendo Padrões de Projetos em Python, Autor Chetan Giridhar, 2016

Caso de uso:
Considere um exemplo de um serviço de nuvem que envolva várias operações de leitura e escrita no banco de dados.
O serviço de nuvem completo está dividido em vários serviços que executam operações no banco de dados.
Uma ação na aplicação web chamará internamente uma API que, em algum momento, resultará em uma operação de banco de dados.

Pontos a considerar:
- Consistência entre as operações no banco de dados - uma operação não deve resultar em conflitos com outras operações.
- A utilização de memória e de CPU deve estar otimizada para o tratamento de várias operações no banco de dados.

Neste código:
- Criamos uma metaclasse chamada MetaSingleton. Nela, o método especial __call__ do Python é usado na metaclasse para criar um Singleton.
- A classe database está decorada com a classe MetaSingleton e começa a agir como um singleton. Assim, quando a classe database é instanciada, ela cria apenas um objeto.
- Quando uma aplicação quiser executar determinadas operações no banco de dados, ela instanciará a classe de banco de dados várias vezes, mas somente um objeto será criado.
- Como existe apenas um objeto, as chamadas ao banco de dados serão sincronizadas.
- Além do mais, isso não é custoso para os recursos do sistema, e podemos evitar problemas com recursos de memória ou CPU.

Observações:
Considere que temos uma configuração em cluster, com várias aplicações web, porém apenas um banco de dados.
Está não é uma boa situação para o Singleton porque, a cada adição de uma aplicação web, um novo Singleton será criado
e um novo objeto que faz consultas no banco de dados será adicionado. Isso resulta em operações não sincronizadas
no banco de dados e exige muito dos recursos.
Em casos assim, implementar um pool de conexões com o banco de dados será melhor do que implementar Singletons.
"""

import sqlite3

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    

class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj
    

db1 = Database().connect()
db2 = Database().connect()

print("Database Objects DB1", db1)
print("Database Objects DB2", db2)