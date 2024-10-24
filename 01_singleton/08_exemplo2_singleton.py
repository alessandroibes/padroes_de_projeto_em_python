"""
Exemplo de Singleton em Python para serviço de sanidade
Livro: Aprendendo Padrões de Projetos em Python, Autor Chetan Giridhar, 2016

Caso de uso:
Considere um serviço de verificação de sanidade (como o Nagios) para a nossa infraestrutura.
Criaremos a classe HealthCheck, que é implementada como um Singleton.
Vamos manter também uma lista de servidores nos quais a verificação de sanidade deve ser feita.
Se um servidor for removido dessa lista, o software de verificação de sanidade deverá detectar isso e
removê-lo dos softwares configurados para ser verificados.

Neste código:
- Os objetos hc1 e hc2 são iguais, pois a classe é um Singleton.
- Os servidores são adicionados à infraestrutura para verificação de sanidade com o método addServer().
- Inicialmente, a iteração da verificação de sanidade é executada nesses servidores.
- O método changeServer() remove o último servidor e adiciona outro à infraestrutura programada para a verificação de sanidade.
- Quando a verificação é executada na segunda iteração, ela tem a lista de servidores alterada.
"""

class HealthCheck:
    _instance = None

    def __new__(cls, *args, **kwags):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwags)
        return HealthCheck._instance
    
    def __init__(self):
        self._servers = []
    
    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")


hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.addServer()
print("Schedule health check for servers (1)..")
for i in range(4):
    print("Checking ", hc1._servers[i])

hc2.changeServer()
print("Schedule health check for servers (2)..")
for i in range(4):
    print("Checking ", hc2._servers[i])