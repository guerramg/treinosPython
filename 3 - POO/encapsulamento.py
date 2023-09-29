class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario #PRIVADO
        
    def show(self):
        print(f"Nome: {self.nome}, salário: R$ {self.__salario}")
        
fulano = Funcionario('fulano', 5000)
siclano = Funcionario('siclano', 2800)

# fulano.__salario = 6000
fulano.show()
siclano.show()