'''
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256
O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
'''
import os


def ip_valido(ip_string):
    partes = ip_string.split('.')
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        parte_integer = int(parte)
        if parte_integer < 0 or parte_integer > 255:
            return False
    return True
if os.path.exists("entrada.txt"):
    ips = open("entrada.txt","r")
    lista_ips = ips.read().split("\n")
    invalido = []
    valido = []

    for lista in lista_ips:
        if ip_valido(lista):
            valido.append(lista)


        else:
            invalido.append(lista)


    print("IP VALIDO :\n", valido)
    print("IP INVALIDO :\n", invalido)
    with open("saida.txt", "w") as opfile:
        opfile.write("[Endereços válidos:]\n")
        opfile.write("\n".join(valido))
        opfile.write("\n\n\n[Endereços Inválidos:]\n")
        opfile.write("\n".join(invalido))



