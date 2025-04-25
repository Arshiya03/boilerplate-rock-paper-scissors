import random

def player(prev_play, opponent_history=[]):
    """
    This function plays Rock Paper Scissors against four different opponent bots.
    It employs a combination of strategies to adapt to each bot's behavior.

    Args:
        prev_play (str): The opponent's previous move ('R', 'P', or 'S').
        opponent_history (list): A list of the opponent's moves so far.
            This list is used to store the opponent's history between rounds.
            It's initialized as an empty list and persists across calls to the function.

    Returns:
        str: The player's next move ('R', 'P', or 'S').
    """
    opponent_history.append(prev_play)
    guess = "R"  # Default guess (Rock)

    # Strategies to defeat different bots:

    # 1. Quincy:  Plays in a predictable cycle (R, P, S, R, P, S, ...)
    if len(opponent_history) > 0:
        if opponent_history[-1] == "R":
            guess = "P"  # Beat Rock
        elif opponent_history[-1] == "P":
            guess = "S"  # Beat Paper
        else:
            guess = "R"  # Beat Scissors

    # 2. Abbey:   Copies the player's last move.
    if len(opponent_history) > 1:
        if opponent_history[-2] == "R":
            guess = "P"
        elif opponent_history[-2] == "P":
            guess = "S"
        else:
            guess = "R"

    # 3. Kris:    Favors a particular move in a cycle.
    if len(opponent_history) > 5:
        # Analyze the frequency of opponent moves
        r_freq = opponent_history.count("R")
        p_freq = opponent_history.count("P")
        s_freq = opponent_history.count("S")

        if r_freq >= p_freq and r_freq >= s_freq:
            guess = "P" #beat rock
        elif p_freq >= r_freq and p_freq >= s_freq:
            guess = "S" # beat paper
        else:
            guess = "R" # beat scissor

    # 4. Mrugesh: Predicts the player's next move based on a longer cycle.
    if len(opponent_history) > 10:
        # Predict opponent's next move and play accordingly
        player_moves = "".join(opponent_history[:-1])
        predicted_move = ""
        if player_moves[-3:] in player_moves[:-3]:
            predicted_move = player_moves[player_moves.rfind(player_moves[-3:])+3]

        if predicted_move == "R":
            guess = "P"
        elif predicted_move == "P":
            guess = "S"
        elif predicted_move == "S":
            guess = "R"
        else:
            #if the pattern is not found
             guess = "P"

    return guess
