""" Exercicios"""
"""    1
mostrar = str(input("Escreva sua frase:\n"))

print(f"A frase digitada foi:{mostrar}")

"""
"""    2
Nome = str(input("Digite seu nome: "))
Idade = int(input("Digite sua idade: "))
Peso = float(input("Digite seu peso: "))


print(f"Seu nome é: {Nome}\nSua idade é: {Idade}\nE seu peso é: {Peso}")

"""

"""    3  

valor = int(input("Insira o valor a verificar:\n"))

print(f" O valor inserido é {valor} o sucessor do valor inserido é {valor +1} e seu antecessor é {valor -1}")

"""

"""     4   

valor = int(input("Insira o valor a verificar"))
print(f"valor inserido é {valor}\n O dobro do valor é {valor * 2}\n O tripo do valor é {valor * 3}\n e sua raiz quadrada é {valor **0.5}")
print(f"valor inserido é {valor}\n O dobro do valor é {valor * 2}\n O tripo do valor é {valor * 3}\n e sua raiz quadrada é {valor **(1/2)}")

"""

"""    5   
ano_nascimento  = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o seu ano atual: "))
idade = ano_atual - ano_nascimento

print(f"Tendo como base o ano {ano_nascimento} concluimos que a sua idade é {idade}")

"""
"""    6 
preço = float(input("Insira o preço do produto:\n"))
print(f"O preço {preço} com 25% de desconto fica {preço - preço * 25 /100:.2f}")

 """

""" 7 
salario = int(input("Insira o Salario do funcionario:"))
print(f"O salario {salario} com aumento de 25% totaliza {salario + salario*25/100:.2f}")

"""

"""  8  

valor = int(input("Insira um valor a verificar a taboada\n"))
print(f"{valor} x 1 == {valor * 1}")
print(f"{valor} x 2 == {valor * 2}")
print(f"{valor} x 3 == {valor * 3}")
print(f"{valor} x 4 == {valor * 4}")
print(f"{valor} x 5 == {valor * 5}")
print(f"{valor} x 6 == {valor * 6}")
print(f"{valor} x 7 == {valor * 7}")
print(f"{valor} x 8 == {valor * 8}")
print(f"{valor} x 9 == {valor * 9}")
print(f"{valor} x 10 == {valor * 10}")

"""

"""   9 

dado1 = int(input("Insira um numero"))
dado2 = str(input("Insira um numero"))

print(type(dado1) == type(dado2))

"""

"""    10  

km_rodados = float(input("Insira a quantidade de Km rodados:\n"))
dias_alugados = int(input("Insira a quantidade de dias alugados\n"))

total_a_pagar = dias_alugados * 60 + km_rodados * 0.15

print(f"Total de {km_rodados}")
print(f"total de dias alugados {dias_alugados}")
print(f"O total a pagar pelo uso do veiculo é R${total_a_pagar}")

"""


""" 11

idade = int(input("Insira sua idade\n"))
meses = 12 * idade
dias = 31 * meses

print(f"Sua idade é {idade}")
print(f"Você tem {meses} Meses de vida")
print(f"Você tem {dias} dias de vida")

"""

"""  12 

total = 780000
primeiro = total * 46 / 100
segundo = total * 32 / 100
terceiro = total * 22 / 100

print(f"O Primeiro ganhador recebeu R$:{primeiro}")
print(f"O Segundo ganhador recebeu R$:{segundo}")
print(f"O Terceiro ganhador recebeu R$:{terceiro}")

"""

""" 13
celsius = float(input("Insira a tempuratura em Cº\n"))
fahrenheit = celsius * 1.8 + 32
print(f"{celsius} Graus celsius convertidos em Farenheit fica {fahrenheit:.2f}")

"""
""" 14 

nota1 = float(input("Insira a nota do aluno"))
nota2 = float(input("Insira a nota do aluno"))
nota3 = float(input("Insira a nota do aluno"))
nota4 = float(input("Insira a nota do aluno"))

print(f"A media entre as notas é {nota1} {nota2} {nota3} {nota4} é {(nota1+nota2+nota3+nota4)/4}")

"""

#""" 15

largura = float(input("Insira a largura da parede\n"))
altura = float(input("Insira a altura da parede\n"))

area = largura * altura
litros_tinta = area /2

print(f"A parede {largura} X {altura} tem sua area total em {area}")
print(f"Serão necessarios {litros_tinta} litros de tinta para pinta-la")

#"""