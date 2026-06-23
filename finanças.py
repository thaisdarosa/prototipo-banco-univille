import os

ARQ_CATEGORIAS = "categorias.txt"
ARQ_ENTRADAS = "entradas.txt"
ARQ_SAIDAS = "saidas.txt"

usuario = "Aluno"
senha = "1234"
tentativas = 3

while tentativas > 0:
    login = input("Digite o usuário: ")
    senha_inserida = input("Digite a senha: ")

    if login == usuario and senha_inserida == senha:
        print("Login realizado com sucesso!")
        break
    else:
        tentativas -= 1
        print(f"Usuário ou senha inválidos. Tentativas restantes: {tentativas}")
        if tentativas == 0:
            print("Número de tentativas excedido. Encerrando programa.")
            exit()

while True:
    print("\n--- Sistema de Finanças Pessoais ---")
    print("1. Adicionar Categoria")
    print("2. Registrar Entrada")
    print("3. Registrar Saída")
    print("4. Relatório do Mês")
    print("5. Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Adicionar categoria
        categorias = []
        if os.path.exists(ARQ_CATEGORIAS):
            with open(ARQ_CATEGORIAS, "r") as f:
                categorias = [linha.strip() for linha in f.readlines()]
        categoria = input("Digite o nome da nova categoria: ")
        if categoria not in categorias:
            categorias.append(categoria)
            with open(ARQ_CATEGORIAS, "w") as f:
                for item in categorias:
                    f.write(item + "\n")
            print(f"Categoria '{categoria}' adicionada com sucesso!")
        else:
            print("Essa categoria já existe.")

    elif opcao == "2":
        # Registrar entrada
        valor = float(input("Digite o valor da entrada: R$ "))
        descricao = input("Descrição da entrada: ")
        with open(ARQ_ENTRADAS, "a") as f:
            f.write(f"{valor};{descricao}\n")
        print("Entrada registrada com sucesso!")

    elif opcao == "3":
        # Registrar saída
        categorias = []
        if os.path.exists(ARQ_CATEGORIAS):
            with open(ARQ_CATEGORIAS, "r") as f:
                categorias = [linha.strip() for linha in f.readlines()]
        valor = float(input("Digite o valor da saída: R$ "))
        categoria = input("Digite a categoria da saída: ")
        if categoria not in categorias:
            print("Categoria não encontrada. Adicione primeiro.")
        else:
            descricao = input("Descrição da saída: ")
            with open(ARQ_SAIDAS, "a") as f:
                f.write(f"{valor};{categoria};{descricao}\n")
            print("Saída registrada com sucesso!")

    elif opcao == "4":
        # Relatório
        entradas = []
        saidas = []
        if os.path.exists(ARQ_ENTRADAS):
            with open(ARQ_ENTRADAS, "r") as f:
                entradas = [linha.strip() for linha in f.readlines()]
        if os.path.exists(ARQ_SAIDAS):
            with open(ARQ_SAIDAS, "r") as f:
                saidas = [linha.strip() for linha in f.readlines()]

        total_entradas = sum(float(e.split(";")[0]) for e in entradas if e)
        total_saidas = sum(float(s.split(";")[0]) for s in saidas if s)
        saldo = total_entradas - total_saidas

        print("\nRelatório Financeiro do Mês")
        print(f"Entradas: R$ {total_entradas:.2f}")
        print(f"Saídas:   R$ {total_saidas:.2f}")
        print(f"Saldo:    R$ {saldo:.2f}\n")

        categorias = []
        if os.path.exists(ARQ_CATEGORIAS):
            with open(ARQ_CATEGORIAS, "r") as f:
                categorias = [linha.strip() for linha in f.readlines()]
        print("Detalhes por categoria:")
        for cat in categorias:
            total_cat = sum(float(s.split(";")[0]) for s in saidas if s and s.split(";")[1] == cat)
            print(f" - {cat}: R$ {total_cat:.2f}")

    elif opcao == "5":
        print("Sessão encerrada. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
