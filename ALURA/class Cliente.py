class Cliente:
    
    def __init__(self, nome):
        self.__nome = nome
    @property
    def nome(self):
        return self.__nome.title()

cliente = Cliente("artur")
print(cliente.nome)