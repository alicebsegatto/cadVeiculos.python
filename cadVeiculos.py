from carro import carro
from moto import moto
from veiculo import veiculo
listaVeiculos = []

def cadastrar():
    print("Qual o tipo de veiculo: (1) Carro - (2) Moto")
    tipo = input()
    print("Digite a marca:")
    marca = input()
    print("Digite o modelo:")
    modelo = input()
    print("Digite a placa:")
    placa = input()
    listaVeiculos.append([marca, modelo, placa])

def listar():
    if len(listaVeiculos) == 0:
        print("Não existem veículos cadastrados")
    else:
        i = 1
        for veiculo in listaVeiculos:
            print(f"Veículo: {i}")
            print(f" - Marca: {veiculo[0]}")
            print(f" - Modelo: {veiculo[1]}")
            print(f" - Placa: {veiculo[2]}")
            i += 1

def excluir():
    listar()
    print("Digite a placa que deseja excluir")
    placa = input()
    encontrou = False
    for veiculo in listaVeiculos:
        if veiculo[2] == placa:
            listaVeiculos.remove(veiculo)
            encontrou = True
            break
    if encontrou:
        print("Veículo excluido")
    else:
        print("Veículo não encontrado")

while True:
    print("Escolha uma das opções:")
    print("1 - Cadastrar Veículos")
    print("2 - Listar Veículos")
    print("3 - Excluir Veículo")
    print("0 - Sair")
    opcao = input()

    try: 
        opcao = int(opcao)
    except:
        print("Opção Inválida")

    if opcao == 1:
         cadastrar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        excluir()
    elif opcao == 0:
        break
    else:
        print("Opção Inválida")