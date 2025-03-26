from time import sleep

def menu():
    menu = """\n========================
         MENU
         
Por favor, selecione a 
opção desejada:
1 - Saque
2 - Depósito
3 - Extrato
4 - Criar conta
5 - Listar contas
6 - Novo usuário
0 - Sair

========================"""
    print(menu)

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depóstio realizado no valor de R${valor}.\n"
        print("\nDepósito realizado com sucesso. Retornando ao menu.")
        sleep(2.5)
    else:
        print("\nO valor inserido é inválido. Retornando ao menu.")
        sleep(2.5)
        
    return saldo, extrato

        
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_saques = numero_saques > limite_saques
    excedeu_limite = valor > limite
    
    if excedeu_saldo:
        print("Você não tem saldo suficiente para esta operação.")
        sleep(2)
    elif excedeu_limite:
        print("Falha na operção. O valor do saque excede o limite.")
        sleep(2)
    elif excedeu_saques:
        print("Falha na operação. Número máximo de saques excedido.")
        sleep(2)
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque realizado no valor de {valor}.\n"
        numero_saques += 1
        print("Saque realizado com sucesso. Retornando ao menu.")
        sleep(1.5)
        
    else:
        print("O valor inserido é inválido. Retonando ao menu.")
        sleep(1.5)
        
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
        print("EXTRATO".center(24, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R${saldo}")
        print("=".center(24, "="))
        sleep(4)
        
def filtrar_usuario(cpf, usuario):
    usuarios_filtrados = [usuario for usuario in usuario if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
        
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números)\n>")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Este CPF já está cadastrado.")
        return

    nome = input("Informe seu nome completo\n>")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa)\n>")
    endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/estado)\n>")
    
    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso. Seja bem-vindo!")
    sleep(2)
    
        
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário (apenas números)\n>")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso. Seja bem-vindo!")
        sleep(4)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuarios}
        
    else:
        print("Usuário não encontrado. Retornando ao menu principal.")
        sleep(2)

    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=".center(24, "="))
        print(linha)
    sleep(5)
    
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 1000
    extrato = ""
    numero_saques = 0
    usuario = []
    contas = []
    
    while True:
        menu()
        opcao = int(input(">"))
        
        if opcao == 1:
            valor = float(input("Informe o valor do saque.\n>"))
            saldo, extrato = saque(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES
                )
            
        elif opcao == 2:
            valor = float(input("Informe o valor do depósito\n>"))
            saldo, extrato = deposito(saldo, valor, extrato)
                        
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == 4:
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuario)
            
            if conta:
                contas.append(conta)
            
        elif opcao == 5:
            listar_contas(contas)
            
        elif opcao == 6:
            criar_usuario(usuario)
            
        elif opcao == 0:
            break
        
        else:
            print("Opção inválida. Selecione novamente.")
            sleep(1.5)
    
main()