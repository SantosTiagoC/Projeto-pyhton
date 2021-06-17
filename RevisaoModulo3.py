""" ..."""

#print(input("insira o dado: "))

#mensagem = str(input("digite a sua mensagem"))
#print(mensagem)

int(9)

float(9.87)

str("tudo entre aspas")

bool(True)

salario = int(input("Insira o salario a receber reajuste:"))
porcentagem = int(input(f"insira quantos % voce quer analisar do valor: {salario} "))
reajuste = salario * porcentagem / 100

print(f"valor Bruto{salario}")
print(f"{porcentagem}% do salario {salario} é {salario*porcentagem/100}")
##print(f"O salario de {salario} com a {porcentagem}% de aumento é {salario + salario * porcentagem / 100}")
#print(f"O salario de {salario} com {porcentagem}% de desconto é {salario - salario * porcentagem /100}")

print(f"O salario de {salario} com a {porcentagem}% de aumento é {salario + reajuste}")
print(f"O salario de {salario} com {porcentagem}% de desconto é {salario - reajuste}")