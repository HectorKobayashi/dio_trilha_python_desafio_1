menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# valor_entrada_saldo = 0
saldo = 0
limite = 500
lista_extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    valor_saque = 0
    valor_deposito = 0
    opcao = input(menu)


    if opcao == 'd':

        valor_deposito = float(input('Informe o valor de Depósito: '))

        if valor_deposito > 0 :
            saldo += valor_deposito
            lista_extrato.append("Depósito: R$ " + str(f"{valor_deposito:.2f}"))
        else:
            print("O valor de depósito é inválido")


    elif opcao == 's':
        
        valor_saque = round(float(input("Informe o valor de saque: ")), 2)

        if valor_saque > saldo:
            print("Saldo insuficiente")
        elif valor_saque > limite:
            print("O valor de saque excedeu o limite")
        elif numero_saques == 3:
            print("O número de saques diários foi excedido")

        elif valor_saque > 0:
            numero_saques += 1
            saldo -= valor_saque
            lista_extrato.append(f"Saque: R$ {valor_saque:.2f}")


    elif opcao == 'e':
        if not lista_extrato:
            print("Não há operações no extrato ")

        print("Extrato Bancário:\n")
        for i in lista_extrato:
            print(f"{i}")
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == 'q':
        break

print("Extrato Bancário:\n")
for i in lista_extrato:
    print(f"{i}")
print(f"\nSaldo: R$ {saldo:.2f}")

