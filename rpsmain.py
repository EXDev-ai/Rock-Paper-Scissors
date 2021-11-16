import random
import time

def decide_winner(choice1, choice2):  
  rps_win_positions = {
    'Rock':{
      'Rock': None,
      'Paper': 'Paper',
      'Scissors': 'Rock'
    },
    'Paper':{
      'Rock': 'Paper',
      'Paper': None,
      'Scissors': 'Scissors'
    },
    'Scissors':{
      'Rock': 'Rock',
      'Paper': 'Scissors',
      'Scissors': None
    }
}
  victor = rps_win_positions[choice1][choice2]
  # Howdy Partner! Might I say you look fit as a fiddle?
  return victor

def rock_paper_scissors(bot_selected_position=None, player_selected_position=None, bot_position=None):
    rps_win_positions = {
      'Rock':{
        'Rock', None,
        'Paper', 'Paper',
        'Scissors', 'Rock'
      },
      'Paper':{
        'Rock', 'Paper',
        'Paper', None,
        'Scissors', 'Scissors'
      },
      'Scissors':{
        'Rock', 'Rock',
        'Paper', 'Scissors',
        'Scissors', None
      }
  }

rps_positions = ['Rock', 'Paper', 'Scissors']
name = input("What's your name?")
print(f"Hello, {name}!")
start = input("Start a game?")
if start == "Yes":
    position = input("Rock, Paper, or Scissors?")
    if position == 'Rock' or 'Paper' or 'Scissors':
        print("Position set.")
        player_selected_position = True
bot_selection = random.choice(rps_positions)
bot_selected_position = True
print(f"Bot has chosen {bot_selection}.")
time.sleep(1)
if player_selected_position and bot_selected_position == True:
  win = decide_winner(position, bot_selection)
  if win:
    if win == position:
      print(f'{name} Wins! Good job.')
    elif win == bot_selection:
      print('Looks like the bot won. Try again to beat him!') 
  else:
    print("Its a tie! Better luck next time.")
elif start != "Yes":
    print("Game start cancelled.")

while True:
  rock_paper_scissors()