# Leer el archivo de entrada
with open("input.txt", "r") as file:
    lines = file.readlines()

# Obtener el número de rondas
num_rounds = int(lines[0])

# Inicializar las puntuaciones de los jugadores y la ventaja máxima
max_lead = 0
winner = 0

# Iterar a través de las rondas y calcular la ventaja
for i in range(1, num_rounds + 1):
    round_scores = lines[i].split()
    score_player1 = int(round_scores[0])
    score_player2 = int(round_scores[1])
    
    # Calcular la ventaja en esta ronda
    lead = abs(score_player1 - score_player2)
    
    # Si la ventaja actual es mayor que la máxima, actualizar la ventaja máxima
    if lead > max_lead:
        max_lead = lead
        if score_player1 > score_player2:
            winner = 1
        else:
            winner = 2

# Escribir el resultado en el archivo de salida
with open("output.txt", "w") as file:
    file.write(f"{winner} {max_lead}\n")
