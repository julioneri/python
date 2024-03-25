peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
print('Seu indice de massa corporal (IMC) é {:.1f}'.format(imc))
if imc < 18.5:
    print('Status: Abaixo do peso.')
if 18.5 <= imc < 25:
    print('Status: Peso ideal.')
if 25 <= imc < 30:
    print('Status: Sobrepeso.')
if 30 <= imc < 40:
    print('Status: Obesidade.')
if imc >= 40:
    print('Status: Obesidade mórbita.')
