
nota = input("Digite a letra da nota (A, B, C, D ou F): ").upper()

match nota:
    case "A":
        print("Excelente!")
    case "B":
        print("Bom!")
    case "C":
        print("Regular!")
    case "D":
        print("Ruim!")
    case "F":
        print("Reprovado!")
    case _:
        print("Nota inválida! Digite A, B, C, D ou F.")

