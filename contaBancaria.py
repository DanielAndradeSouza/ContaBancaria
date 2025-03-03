TOTAL_EXTRATO = []
num_saques = 0
TOTAL_SAQUES = 3
saldo = 100.0
LIMITE_SAQUE = 500.0

def deposito(insercao):
    global saldo
    if insercao <= 0:
        print("Insira um valor de depósito válido!")
    else:
        saldo += insercao
        TOTAL_EXTRATO.append(f"Depósito: +R$ {insercao:.2f}")
        print(f"Depósito realizado com sucesso! Saldo Total: R$ {saldo:.2f}")

def saque(remocao):
    global saldo, num_saques
    if remocao > saldo:
        print("Saldo insuficiente.")
    elif remocao > LIMITE_SAQUE:
        print(f"Valor do saque muito alto. O limite por saque é R$ {LIMITE_SAQUE:.2f}.")
    elif num_saques >= TOTAL_SAQUES:
        print("Número máximo de saques atingido.")
    else:
        saldo -= remocao
        num_saques += 1
        TOTAL_EXTRATO.append(f"Saque: -R$ {remocao:.2f}")
        print(f"Saque realizado com sucesso! Saldo Total: R$ {saldo:.2f}")

def extrato():
    print("\n=== Extrato Bancário ===")
    if not TOTAL_EXTRATO:
        print("Nenhuma operação foi efetuada em sua conta.")
    else:
        for ext in TOTAL_EXTRATO:
            print(ext)
    print(f"Saldo Total: R$ {saldo:.2f}")
    print("========================\n")

while True:
    print("\nBem-vindo ao seu banco! Escolha uma operação:")
    print("1 - Depósito\n2 - Saque\n3 - Extrato\n4 - Sair")
    
    decisao = input("Digite a opção desejada: ")

    if decisao == "1":
        insercao = float(input("Digite o valor do depósito: "))
        deposito(insercao)
    elif decisao == "2":
        remocao = float(input("Digite o valor do saque: "))
        saque(remocao)
    elif decisao == "3":
        extrato()
    elif decisao == "4":
        print("Obrigado por usar nosso banco! Até mais.")
        break
    else:
        print("Opção inválida! Tente novamente.")

    if num_saques == TOTAL_SAQUES:
        print("Você atingiu o limite de saques diários. Operações encerradas.")
        break
