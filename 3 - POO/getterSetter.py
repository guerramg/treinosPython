class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario #PRIVADO
        
    def show(self):
        print(f"Nome: {self.nome}, salário: R$ {self.__salario}")
        
    def getSalario(self):
        return self.__salario
    
    def setSalario(self, salario):
        self.__salario = salario
        
fulano = Funcionario("fulano", 3000)
siclano = Funcionario('siclano', 3000)

fulano.show()
siclano.show()

fulano.setSalario(5800)

print(fulano.getSalario())