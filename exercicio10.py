#escreva um programa que pergunte quantos pedaços o bolo tem,em seguida pergunte ao usuario quantos pedaços ainda tem e exiba uma mensagen da sua escolha

bolototal = int (input("Quantas fatia o bolo tem?"))
comeu = int (input("Quantos fatias voce comeu?"))
resultado = bolototal - comeu
print("As sobras foram:",resultado,"voce come demais!!!")
