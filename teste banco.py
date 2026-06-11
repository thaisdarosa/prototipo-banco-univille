adms = ["gerente"]
senhadms = ["gerente"]

usuarios = ["aluno", "aluno1", "aluno2"]
senhas = ["univille", "univille1", "univille2"]

saldos = [193.94, 500.00, 1000.00]
limites = [100.00, 200.00, 300.00]

while True:

    print("\n- UNIVILLE Internet Banking -")
    print("1. Acessar conta")
    print("2. Acesso administrador")
    print("3. Encerrar")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":

        tentativas = 3
        logado = False

        while tentativas > 0:

            usuario_digitado = input("Digite o usuário: ")

            encontrou = False

            for i in range(len(usuarios)):
                if usuario_digitado == usuarios[i]:
                    encontrou = True
                    break

            if encontrou:

                senha_digitada = input("Digite a senha: ")

                if senha_digitada == senhas[i]:
                    print("Login realizado com sucesso!")
                    cliente_logado = i
                    logado = True
                    break
                else:
                    tentativas -= 1
                    print("Usuário ou senha inválidos.")
                    print(f"Tentativas restantes: {tentativas}")

            else:
                tentativas -= 1
                print("Usuário ou senha inválidos.")
                print(f"Tentativas restantes: {tentativas}")

        if logado:

            while True:

                print("\n- Menu Cliente -")
                print("1. Consultar saldo")
                print("2. Realizar saque")
                print("3. Realizar depósito")
                print("4. Consultar limite")
                print("5. Encerrar sessão")

                menu = input("Digite a opção desejada: ")

                if menu == "1":

                   print("\n")
                   print(f"Saldo: R$ {saldos[cliente_logado]:.2f}")

                elif menu == "2":

                    valor_saque = float(input("Digite o valor do saque: R$ "))

                    if valor_saque <= 0:
                        print("\n")
                        print("Valor inválido.")
                        print("Operação não realizada.")

                    elif valor_saque > saldos[cliente_logado] + limites[cliente_logado]:
                        print("\n")
                        print("Saldo insuficiente.")
                        print("Operação não realizada.")

                    else:
                        saldos[cliente_logado] = saldos[cliente_logado] - valor_saque

                        print("\n")
                        print("Saque realizado com sucesso.")
                        print(f"Novo saldo: R$ {saldos[cliente_logado]:.2f}")

                elif menu == "3":

                    valor_deposito = float(input("Digite o valor do depósito: R$ "))

                    if valor_deposito > 0:

                        saldos[cliente_logado] = saldos[cliente_logado] + valor_deposito

                        print("\n")
                        print("Depósito realizado com sucesso.")
                        print("\n")
                        print(f"Novo saldo: R$ {saldos[cliente_logado]:.2f}")

                    else:
                        print("Valor inválido.")
                        print("Operação não realizada.")

                elif menu == "4":

                    limite_disponivel = (
                        saldos[cliente_logado] + limites[cliente_logado]
                    )

                    print("\n")
                    print(f"Limite: R$ {limites[cliente_logado]:.2f}")
                    print("\n")
                    print(f"Limite disponível: R$ {limite_disponivel:.2f}")

                elif menu == "5":

                    print("Sessão encerrada.")
                    break

                else:
                    print("Opção inválida.")

    elif opcao == "2":

        tentativas = 3
        adm_logado = False

        while tentativas > 0:

            usuario_adm = input("Digite o usuário administrador: ")

            encontrou = False

            for i in range(len(adms)):
                if usuario_adm == adms[i]:
                    encontrou = True
                    break

            if encontrou:

                senha_adm = input("Digite a senha: ")

                if senha_adm == senhadms[i]:
                    adm_logado = True
                    print("Administrador autenticado.")
                    break

                else:
                    tentativas -= 1
                    print("Usuário ou senha inválidos.")
                    print(f"Tentativas restantes: {tentativas}")

            else:
                tentativas -= 1
                print("Usuário ou senha inválidos.")
                print(f"Tentativas restantes: {tentativas}")

        if adm_logado:

            while True:

                print("\nClientes cadastrados:")

                for i in range(len(usuarios)):
                    print(f"{i} - {usuarios[i]}")

                cliente_selecionado = int(
                    input("Digite o índice do cliente: ")
                )

                if cliente_selecionado < 0 or cliente_selecionado >= len(usuarios):
                    print("Cliente inválido.")
                    continue

                while True:

                    print(
                        f"\nCliente selecionado: "
                        f"{usuarios[cliente_selecionado]}"
                    )

                    print("1. Consultar saldo")
                    print("2. Consultar limite")
                    print("3. Alterar senha")
                    print("4. Alterar limite")
                    print("5. Trocar cliente")
                    print("6. Encerrar")

                    menu = input("Digite a opção desejada: ")

                    if menu == "1":

                        print(
                            f"Saldo: "
                            f"R$ {saldos[cliente_selecionado]:.2f}"
                        )

                    elif menu == "2":

                        print("\n")
                        print(f"Limite:"f"R$ {limites[cliente_selecionado]:.2f}")

                    elif menu == "3":

                        nova_senha = input("Digite a nova senha: ")

                        senhas[cliente_selecionado] = nova_senha

                        print("\n")
                        print("Senha alterada com sucesso.")

                    elif menu == "4":

                        novo_limite = float(
                            input("Digite o novo limite: ")
                        )

                        limites[cliente_selecionado] = novo_limite

                        print("\n")
                        print("Limite alterado com sucesso.")
                        print(f"Limite atual: {limites[cliente_selecionado]:.2f}")

                    elif menu == "5":

                        break

                    elif menu == "6":

                        print("Sessão administrador encerrada.")
                        break

                    else:

                        print("Opção inválida.")

                if menu == "6":
                    break

    elif opcao == "3":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida.")