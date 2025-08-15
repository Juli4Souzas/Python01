# Lista de compras em Python

lista_compras = []

while True:
    print("\n--- Lista de Compras ---")
    print("1 - Adicionar item")
    print("2 - Ver lista")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o nome do item: ")
        lista_compras.append(item)
        print(f"✅ {item} foi adicionado à lista.")

    elif opcao == "2":
        if len(lista_compras) == 0:
            print("A lista está vazia.")
        else:
            print("\n🛍️ Sua lista de compras:")
            for i, item in enumerate(lista_compras, 1):
                print(f"{i}. {item}")

    elif opcao == "3":
        print("Finalizando o programa... Até mais <3")
        break

    else:
        print("Opção inválida. Tente novamente.")
