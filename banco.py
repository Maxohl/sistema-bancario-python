# Variaveis
saque = 0.0
deposito = 0.0
saldo = 0.0
limite = 500.0
extrato = ""
opcao = -1
limite_diario = 0

#enquanto o usuario não escolhar Sair, mostrar o menu e perguntar qual opção ele quer.
while True :
    print(f"""
    ============== MENU ==============
      
    1 - Saldo
    2 - Sacar
    3 - Depositar
    4 - Extrato
    5 - Sair
      
    ==================================
      
     Obrigado por usar nosso sistema \n""")
    opcao = int(input("Qual operação você deseja realizar? : "))

# opção 1, visualizar o saldo dísponivel
    if opcao == 1:
        submenu = True
        while submenu != False:
            print(f""" 
    ============== SALDO ==============

    Saldo Disponível : R$ {saldo:.2f}

    ===================================

        Pressione Enter para voltar.
            """)
            input()
            submenu = False

# opção 2 saques, saques não podem passar do limite, devem ser um numero positivo, e apenas 3 saques por dia.   
    elif opcao == 2:
        saque = float(input("Informe o valor para sacar: "))
        if (saque <= limite) and (saque > 0) and (saque <= saldo) and (limite_diario < 3):
            saldo -= saque
            limite_diario += 1
            extrato += f"""Saque no valor de R$ {saque:.2f} \n"""
            print("Sacando...")
        
        elif (saque > limite):
            print(f"""Você não pode sacar mais do que {limite} por dia.""")

        elif (limite_diario >= 3):
            print("Você atingiu o limite de saques por dia, favor tentar novamente mais tarde.")

        elif (saque <= limite) and (saque > saldo):
            print("Não há saldo o suficiente") 
        
        else :
            print("Você entrou com um valor inválido, tente novamente.")

# opção 3, depósitos, não há limites mas o valor dever ser um numero positivo.
    elif opcao == 3:
        deposito = float(input("Informe o valor a ser depositado: "))
        if deposito <= 0:
            print("Apenas numéros positivos acima de Zero podem ser depositados.")
        else:
            saldo += deposito
            extrato += f"""Depósito no valor de R$ {deposito:.2f} \n"""
            print("Valor depositado com sucesso!")

# opção 4 mostrar o extrato, dever ter todos os saques e depósitos salvos.
    elif opcao == 4:

        print("\n============== EXTRATO ==============\n")

        print("Não foram realizadas movimentações." if not extrato else extrato)
              
        print(f"""\nSaldo dísponivel : R$ {saldo:.2f}\n""")

        print("\n=====================================\n")

        print("Pressione Enter para voltar.")
        input()

# Sair do programa
    elif opcao == 5:
        break

# Se o usuário escolher uma opção não existente
    else:
        print("Operação inválida, por favor selecione a operação desejada.")


print("Volte sempre!")