lista = []
qntd = int(input("Digite a quantidade de números que deseja digitar: "))
soma = 0
for i in range(qntd):
    num = float(input("Digite um número: "))
    lista.append(num)
    soma += num
media = soma/qntd
print(lista)
print("A média da lista acima é: ",media)