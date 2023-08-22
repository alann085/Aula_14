lista = [2,3,1,4,5,6,8,7,9]

qntdpar = 0
qntdimpar = 0

for num in lista:
        if (num % 2) == 0:
            print(num,"é par")
            qntdpar += 1
        else:
            print(num,"é impar")
            qntdimpar += 1

print(f"Quantidade de pares: {qntdpar}, quantidade de impares: {qntdimpar}")
