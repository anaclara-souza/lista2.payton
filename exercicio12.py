#escreva um programa que pergunte o valor total da conta em seguida pergunte quantos clientes existem,divida a conta pelos clientes e exiba o quanto cada cliente deve pagar,seguida da mensagem"cada cliente deve pagar:"valor x

valortotal = int(input("Valor total da conta:"))
clientes = int(input("Quantos clientes voce tem?"))
pagamento = valortotal/clientes
print("cada clinte deve pagar:",pagamento)