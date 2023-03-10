import pandas as pd
import random

print("""Wordle is a single player game 
A player has to guess a five letter hidden word
You have six attempts 
Your Progress Guide "^XX^+"
"^" Indicates that the letter at that position was guessed correctly 
"+" indicates that the letter at that position is in the hidden word, but in a different position 
"X" indicates that the letter at that position is wrong, and isn't in the hidden word   """)

df = pd.read_csv("MonsterHunterdle.csv")

def check_word(ind, mon_name, game_name, ele_name, class_name):
  attempt = 6
  while attempt > 0:
    guess = str(input("Guess the monster: "))
    if guess == mon_name:
      print("You guessed the monster correctly! WIN")
      break
    else:
      attempt = attempt - 1
      print(f"you have {attempt} attempt(s) \n ")
      print(guess + "\U000026AB")
      guess_row = (df[df['Monster'] == guess].index[0])
      guess_element = (df['Element'][(df[df['Monster'] == guess].index[0])])
      guess_game = (df['Intro Game'][(df[df['Monster'] == guess].index[0])])
      guess_class = (df['Class'][(df[df['Monster'] == guess].index[0])])

      if guess_game == game_name: # Game Appearance
        print(guess_game + "  \U0001F7E2")
      else:
        print(guess_game + "  \U000026AB")


      if guess_element == ele_name: # Blights and statuses they inflict MORE TO DO HERE
        print(guess_element + "  \U0001F7E2")
      else:
        print(guess_element + "  \U000026AB")


      if guess_class == class_name:
        print(guess_class + "  \U0001F7E2")
      else:
        print(guess_class + "  \U000026AB")
      #for char, word in zip(mon_name, guess):
      #      if word in mon_name and word in char:
      #          print(word + " ^ ")
      #
      #      elif word in mon_name:
      #          print(word + " + ")
      #      else:
      #          print(word + " X ")
      if attempt == 0:
        print(" Game over !!!! ")

def choose_monster():
   rando = random.randint(0,len(df)-1)
   monster = df['Monster'][rando]
   game = df['Intro Game'][rando]
   element = df['Element'][rando]
   classif = df['Class'][rando]
   print(str(rando)+monster+game+element+classif)
   check_word(rando, monster, game, element, classif)


choose_monster()
#print("\U0001F7E2") # green
#print("\U0001F7E1") # yellow
#print("\U000026AB") # grey

