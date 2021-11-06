import random
import time

rps_positions = {
    0: 'Rock',
    1: 'Paper',
    2: 'Scissors'
}


def rock_paper_scissors(bot_selected_position=None, bot_position=None):
    name = input("What's your name?")
    player_name = name
    print(f"Hello, {player_name}!")
    start = input("Start a game?")
    if start == "Yes":
        position = input("Rock, Paper, or Scissors?")
        if position == "Rock":
            print("Position set to Rock.")
            set_position = rps_positions[0]
            player_position = set_position
            player_selected_position = True
        elif position == "Paper":
            print("Position set to Paper.")
            set_position = rps_positions[1]
            player_position = set_position
            player_selected_position = True
        elif position == "Scissors":
            print("Position set to Scissors.")
            set_position = rps_positions[2]
            player_position = set_position
            player_selected_position = True
    bot_selection = random.choice(rps_positions)
    bot_position = bot_selection
    print(f"Bot has chosen {bot_selection}.")
    time.sleep(1)
    if player_position == "Rock" and bot_position == "Paper":
        print("Bot wins!")
        return
    if player_position == "Paper" and bot_position == "Scissors":
        print("Bot wins!")
        return
    if player_position == "Scissors" and bot_position == "Rock":
        print("Bot wins!")
        return
    if player_position == "Paper" and bot_position == "Rock":
        print("Player wins!")
        return
    if player_position == "Rock" and bot_position == "Scissors":
        print("Player wins!")
        return
    if player_position == "Scissors" and bot_position == "Paper":
        print("Player wins!")
        return
    elif start != "Yes":
        print("Game start cancelled.")
        return


rock_paper_scissors()
