"""
else if

elif == se assim como if == se

"""

print("Teste de comparação de numeros\n")

numero1 = int(input("Insira o valor1\n"))
numero2 = int(input("Insira o valor2\n"))


print(f"Valor1 é:  {numero1}     Valor2 é: {numero2}")

if numero1 == numero2:
    print("Os valores são iguais")
elif numero1 > numero2:
    print("O valor1 é maior")
elif numero1 < numero2:
    print("O valor1 é menor")
else:
    print("Os valores são diferentes")
