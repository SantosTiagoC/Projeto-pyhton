""" ...

valor = int(input("Insira o valor:\n"))

print(f"O sucessor do valor {valor} é {valor +1} e seu antecessor é {valor -1}")
"""

"""..

Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

"""

km_rodados = float(input("Insira a quantidade de Km rodados:\n"))
dias_alugados = int(input("Insira a quantidade de dias alugados\n"))

total_a_pagar = dias_alugados * 60 + km_rodados * 0.15

print(f"Total de {km_rodados}")
print(f"total de dias alugados {dias_alugados}")
print(f"O total a pagar pelo uso do veiculo é R${total_a_pagar}")