nome = input("Digite seu Nome: ")
altura = float(input("Digite sua Altura: "))
peso = int(input("Digite seu Peso: "))
imc = peso / (altura ** 2)

print(f'{nome} Seu IMC é de: {imc:.2f}')
