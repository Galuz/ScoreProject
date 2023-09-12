def calculate_winner(input_data):
    rounds = []
    winner = None
    error_message = ""

    # Check if the input data is empty.
    if not input_data.strip():
        error_message = "Ingresa los datos antes de calcular."
        return rounds, winner, error_message

    lines = input_data.strip().split('\n')
    num_rounds = int(lines[0])
    rounds_data = lines[1:]

    player1_total = 0
    player2_total = 0
    leader_margin = 0

    # Clear error messages when starting the calculation.
    error_message = ""

    if num_rounds != len(rounds_data):
        # Check if the specified number of rounds does not match the actual quantity of rounds.
        error_message = f"El número de rondas especificado ({num_rounds}) no coincide con la cantidad de rondas proporcionadas ({len(rounds_data)})."
        return rounds, winner, error_message

    for i, line in enumerate(rounds_data):
        # Use an updated regular expression to validate the format of the line.
        values = line.strip().split()
        
        if len(values) != 2:
            # Check if the line does not contain exactly 2 values.
            error_message = "Deben de ser exactamente 2 jugadores."
            return rounds, winner, error_message

        if any(int(value) < 0 for value in values):
            # Check if any of the values is negative.
            error_message = f"Los números negativos no están permitidos en la línea {i + 2}."
            return rounds, winner, error_message

        player1_str, player2_str = values
        player1 = int(player1_str)
        player2 = int(player2_str)

        if not (isinstance(player1, int) and isinstance(player2, int)):
            # Check if any of the values is not a valid number.
            error_message = "Los valores deben ser numéricos."
            return rounds, winner, error_message

        player1_total += player1
        player2_total += player2
        leader = player1_total - player2_total
        current_leader = 1 if leader > 0 else 2
        margin = abs(leader)

        rounds.append({
            "player1": player1_total,
            "player2": player2_total,
            "leader": f"Jugador {current_leader}",
            "margin": margin,
        })

        if margin > leader_margin:
            leader_margin = margin
            winner = {"player": current_leader, "margin": margin}

    return rounds, winner, error_message


def generate_results_file_content(winner):
    if winner is None:
        return "No hay ganador."

    return f"{winner['player']} {winner['margin']}"


def main():
     # Try to read the contents of the file 'input.txt' in the same directory.
    try:
        with open("input.txt", "r") as input_file:
            input_data = input_file.read()
    except FileNotFoundError:
        print("El archivo 'input.txt' no se encontró en el directorio del proyecto.")
        return

    rounds, winner, error_message = calculate_winner(input_data)
    print("Rounds Data:")
    for round_data in rounds:
        print(round_data)

    print("\nWinner:")
    print(generate_results_file_content(winner))

    # Generate and write the results to a file
    results_file_content = generate_results_file_content(winner)
    with open("output.txt", "w") as results_file:
        results_file.write(results_file_content)


if __name__ == "__main__":
    main()
