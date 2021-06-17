"""




valor = int(input("Insira o valor:\n"))

if valor % 2 ==0:
    print(f"O valor {valor} é PAR:\n")
else:
    print(f"o valor {valor} é IMPAR")

print("Fim do programa")



"""


nome = str(input("Insira seu nome:\n"))
idade = int(input("Insira saua Idade:\n"))
peso = int(input("Insira seu Peso:\n"))


if nome == "Tadeu":
    print("Prazer te ver aqui novamente!")
else:
    print("Nome registrado com Sucesso")

print(f"Seja bem vindo {nome}")
print("Idade registrada com sucesso")

if  idade >= 18:
    print("Verificando seus dados você é maior de idade")

else:
    print("Verificando seus dados você é menor de idade")

if peso <= 85:
    print("Vejo que esta dando pra ir ainda né brother")
elif peso > 140:
    print("Você precisa emagrecer.")
else:
    print("Um pouco de esforço basta.")