
valor1 = int(input("Digite o primeiro valor: "))

valor2 = 0
while(valor2 <= valor1):
    valor2 = int(input("Digite o segundo valor: "))
    if (valor2 <= valor1):
        print("O segundo valor deve ser MAIOR que o primeiro.")

somaTotalInteiros = 0
for i in range(valor1, valor2+1):
    somaTotalInteiros += i

print(f"A soma total dos valores inteiros é: {somaTotalInteiros}")
