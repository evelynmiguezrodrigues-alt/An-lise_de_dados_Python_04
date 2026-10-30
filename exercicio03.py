
esporte = int(input("Escolha o esporte (1-Natação, 2-Corrida, 3-Ciclismo): "))
idade = int(input("Digite sua idade: "))

match esporte:
    case 1:
        if idade < 10:
            print("Categoria: Mirim")
        elif idade <= 14:
            print("Categoria: Infantil")
        else:
            print("Categoria: Juvenil")

    case 2:
        if idade < 16:
            print("Categoria: Junior")
        else:
            print("Categoria: Adulto")

    case 3:
        if idade >= 18:
            print("Categoria: Profissional")
        else:
            print("Categoria: Amador")

    case _:
        print("Esporte inválido! Escolha 1, 2 ou 3.")
