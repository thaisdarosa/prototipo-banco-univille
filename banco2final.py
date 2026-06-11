usuarios = [
    ["aluno1", "univille1", 193.94, 100.00],
    ["aluno2", "univille2", 250.00, 200.00],
    ["aluno3", "univille3", 150.00, 300.00],
    ["gerente", "GERENTE"]
]

while True:
    logado = False
    usuario_atual = None
    print("- UNIVILLE Internet Banking -")
    print("1. Acessar")
    print("2. Encerrar")

    opcao = input("Digite a opção desejada:")

    if opcao == "1":
        tentativas = 3

        while tentativas > 0:
            usuario = input("Digite o seu usuário:")
            senha = input("Digite a sua senha:")

            encontrado = None
            for u in usuarios:
                if u[0] == usuario and u[1] == senha:
                    encontrado = u
                    break

            if encontrado:
                print("Login realizado com sucesso!")
                logado = True
                usuario_atual = encontrado
                break
            else:
                print("Usuário e/ou senha inválidos.")
                tentativas -= 1
                print(f"Número de tentativas restantes: {tentativas}")

                if tentativas == 0:
                    print("- NÚMERO DE TENTATIVAS EXCEDIDAS. -")
                    break

    if logado:
        while True:
            print(" - Univille Internet Banking -")

            if usuario_atual[0] == "gerente":
                print(" 1. Alterar senha de usuário")
                print(" 2. Alterar limite de usuário")
                print(" 3. Encerrar")

            else:
                print(" 1. Consultar Saldo")
                print(" 2. Realizar Saque")
                print(" 3. Realizar Depósito")
                print(" 4. Consultar limite")
                print(" 5. Encerrar")

            menu = input("Digite a opção desejada:")

            if usuario_atual[0] == "gerente":
                if menu == "1":
                    print("Usuários:\n aluno1\n aluno2\n aluno3")
                    alvo = input("Digite o usuário que deseja alterar a senha:")
                    for u in usuarios:
                        if u[0] == alvo and u[0] != "gerente":
                            nova_senha = input("Digite a nova senha:")
                            u[1] = nova_senha
                            print("Senha alterada com sucesso.")
                            break
                    else:
                        print("Usuário não encontrado ou inválido.")

                elif menu == "2":
                    print("Usuários:\n aluno1\n aluno2\n aluno3")
                    alvo = input("Digite o usuário que deseja alterar o limite:")
                    for u in usuarios:
                        if u[0] == alvo and u[0] != "gerente":
                            novo_limite = float(input("Digite o novo limite R$:"))
                            u[3] = novo_limite
                            print("Limite alterado com sucesso.")
                            break
                    else:
                        print("Usuário não encontrado ou inválido.")

                elif menu == "3":
                    print("Sessão do gerente encerrada.")
                    break

            else:
                if menu == "1":
                    print(f"Saldo é R$: {usuario_atual[2]:.2f}")

                elif menu == "2":
                    valor_saque = float(input("Digite o valor do saque R$:"))
                    if valor_saque <= 0:
                        print("Valor inválido.")
                    elif valor_saque > usuario_atual[2] + usuario_atual[3]:
                        print("Saldo insuficiente.")
                    else:
                        usuario_atual[2] -= valor_saque
                        print(f"Saque realizado. Novo saldo R$: {usuario_atual[2]:.2f}")

                elif menu == "3":
                    valor_deposito = float(input("Digite o valor de depósito R$:"))
                    if valor_deposito > 0:
                        usuario_atual[2] += valor_deposito
                        print("Depósito realizado com sucesso.")
                    else:
                        print("Valor inválido.")

                elif menu == "4":
                    limite_disponivel = usuario_atual[2] + usuario_atual[3]
                    print(f"Limite da conta é R$: {usuario_atual[3]:.2f}")
                    print(f"Limite disponível: {limite_disponivel:.2f}")

                elif menu == "5":
                    print("Sessão encerrada.")
                    break

    elif opcao == "2":
        break

print("PROGRAMA ENCERRADO")
