# Read the input file
with open("input.txt", "r") as file:
    lines = file.readlines()

# Get the number of rounds.
num_rounds = int(lines[0])

# Initialize player scores and the maximum advantage.
max_lead = 0
winner = 0

# Iterate through the rounds and calculate the advantage
for i in range(1, num_rounds + 1):
    round_scores = lines[i].split()
    score_player1 = int(round_scores[0])
    score_player2 = int(round_scores[1])
    
    # Calculate the advantage in this round.
    lead = abs(score_player1 - score_player2)
    
    # If the current advantage is greater than the maximum, update the maximum advantage.
    if lead > max_lead:
        max_lead = lead
        if score_player1 > score_player2:
            winner = 1
        else:
            winner = 2

# Write the result to the output file.
with open("output.txt", "w") as file:
    file.write(f"{winner} {max_lead}\n")
