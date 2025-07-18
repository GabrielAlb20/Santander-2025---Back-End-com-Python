balance = 0
withdraw_limit = 500
statement = ""
withdraw_count = 0
DAILY_WITHDRAW_LIMIT = 3

while True:
    print("\n===== MENU =====")
    print("[d] Depositar")
    print("[w] Sacar")
    print("[s] Extrato")
    print("[q] Sair")
    option = input("Escolha uma opção: ").lower()

    if option == "d":
        amount = float(input("Informe o valor do depósito: R$ "))
        
        if amount > 0:
            balance += amount
            statement += f"Depósito: R$ {amount:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    elif option == "w":
        if withdraw_count >= DAILY_WITHDRAW_LIMIT:
            print("Erro: Limite de saques diários atingido.")
        else:
            amount = float(input("Informe o valor do saque: R$ "))

            if amount > balance:
                print("Erro: Saldo insuficiente.")
            elif amount > withdraw_limit:
                print(f"Erro: Limite máximo por saque é R$ {withdraw_limit:.2f}.")
            elif amount <= 0:
                print("Erro: O valor do saque deve ser positivo.")
            else:
                balance -= amount
                statement += f"Saque:    R$ {amount:.2f}\n"
                withdraw_count += 1
                print("Saque realizado com sucesso.")

    elif option == "s":
        print("\n===== EXTRATO =====")
        print("Não foram realizadas movimentações." if not statement else statement)
        print(f"Saldo atual: R$ {balance:.2f}")
        print("====================")

    elif option == "q":
        print("Encerrando o sistema... Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Opção inválida. Por favor, escolha novamente.")
