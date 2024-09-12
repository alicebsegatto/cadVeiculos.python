from veiculo import veiculo
class carro(veiculo):
    def __init__(self,marca,modelo,placa,ano,n_portas):
        super().__init__(marca,modelo,placa,ano)
        self.__n_portas = n_portas
        #override - sobrescrever o metodo __str__()
    def __str__(self):
        ret = super().__str__()
        return f'''{ret}
- Num. Portas: {self.__n_portas}'''