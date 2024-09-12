from veiculo import veiculo

class caminhao(veiculo):
    def __init__(self, marca, modelo, placa, ano, capacidade):
        super().__init__(marca, modelo, placa,ano)
        self.__capacidade = capacidade
    #Sobrescrita do método __str__()
    def __str__(self):
        #Invoco o método __str__() da SUPERCLASSE (Veiculo)
        # Armazeno o retorno na variável "retorno"
        retorno = super().__str__()
        #Retorno a concatenação do valor da variável
        # "retorno" com as "__cilindradas"
        return f'''{retorno}
 - Capacidade: {self.__capacidade}'''