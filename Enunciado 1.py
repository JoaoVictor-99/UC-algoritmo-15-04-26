def calcular_media():
    notas = []
    
    try:
        for i in range(3):
            nota = float(input(f"nota {i+1}: "))
            entrada = input(f"Digite a nota {i}: ")
            nota = float(entrada)
            notas.append(nota)

        media = sum(notas) / 3
        print(f"Média final: {media:.2f}")

    except ValueError:
        print("Digite algum valor.")

calcular_media()