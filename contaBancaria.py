import textwrap
def deposito(saldo,valor,extrato,/):
    if saldo <= 0:
        print("Insira um valor de depósito válido!")
    else:
        saldo += valor
        extrato +=  f"Depósito: \t R$ {valor:.2f}\n"
        print(f"Depósito realizado com sucesso! Saldo Total: R$ {saldo:.2f}")
        return saldo, extrato

def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print(f"Valor do saque muito alto. O limite por saque é R$ {LIMITE_SAQUE:.2f}.")
    elif num_saques >= limite_saques:
        print("Número máximo de saques atingido.")
    elif valor>0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        num_saques += 1
        print(f"Saque realizado com sucesso! Saldo Total: R$ {saldo:.2f}")
    else: 
        print("\nOperação Falhou! O valor infermado é invalido!")
    return saldo, extrato

def conferir_extrato(saldo,/,*,extrato):
    print(extrato)

def cadastro_usuario(usuarios):
    cpf = input("Informe seu CPF (Somente numeros)")

    if cpf_existente(cpf,usuarios) == True:
        print("Usuario com cpf ja existente\n")
    else:
        nome = input("Informe o nome completo:")
        data_nascimento = input ("Informe a data de nascimento:")
        endereco = input("Informe o seu endereco:")
        usuarios.append({"nome":nome, "nascimento":data_nascimento, "endereco":endereco})
        print("Cadastro realizado com sucesso!")

def cpf_existente(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return True if usuarios_filtrados[0] else None
def cadastro_conta():

    return

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario'['nome']]}
        """
    print("=" + 100)
    print(textwrap.dedent(linha))


while True:
    LIMITE_SAQUE = 500.0
    TOTAL_SAQUES = 3
    extrato = ""
    num_saques = 0
    saldo = 100.0
    limite = 300.0
    usuarios_cadastrados = []
    contas = []
    AGENCIA = "0001"

    print("\nBem-vindo ao seu banco! Escolha uma operação:")
    print("1 - Depósito\n2 - Saque\n3 - Extrato\n4 - Sair\n5-Criar Usuario \n6 - Listar Contas \n7- Criar Conta Corrente")
    
    decisao = input("Digite a opção desejada: ")

    if decisao == "1":

        valor = float(input("Digite o valor do depósito: "))
        saldo,extrato = deposito(saldo,valor,extrato)

    elif decisao == "2":

        remocao = float(input("Digite o valor do saque: "))
        saldo,extrato = saque(saldo, valor, extrato, limite, TOTAL_SAQUES,LIMITE_SAQUE)

    elif decisao == "3":
        
        conferir_extrato(saldo, extrato)

    elif decisao == "4":

        print("Obrigado por usar nosso banco! Até mais.")
        break

    elif decisao == "5":

        numero_conta = len(contas) + 1
        conta = cadastro_usuario(AGENCIA, numero_conta, usuarios_cadastrados)

        if conta:
            contas.append(conta)

    elif decisao == "6":

        listar_contas(contas)

    elif decisao == "7":
        conta = cadastro_conta(AGENCIA,numero_conta,usuarios_cadastrados)

        if conta:
            contas.append(conta)
            numero_conta += 1
    else:
        print("Opção inválida! Tente novamente.")

    if num_saques == TOTAL_SAQUES:
        print("Você atingiu o limite de saques diários. Operações encerradas.")
        break
