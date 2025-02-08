#Hangman in Python
import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

#dictionary of key:()
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "/| ",
                  "   "),
               4:(" o ",
                  "/|\\ "
                  "   "),
               5:(" o ",
                  "/|\\ ",
                  "/  "),
               6:(" o ",
                  "/|\\ ",
                  "/ \\")}


def display_man(wrong_guesses):
   print("----------")
   for line in hangman_art[wrong_guesses]:
      print(line)
   print("----------")

def display_hint(hint:str):
   print("Here's a hint:", " ".join(hint))

def display_answer(answer:str):
   print("Here's the answer:", " ".join(answer))

def main():
   answer = random.choice(words)
   hint = ["_"] *len(answer)
   wrong_guesses = 0
   guessed_letters = set()
   is_running = True

   while is_running:
      display_man(wrong_guesses)
      display_hint(hint)
      guess = input("Enter a letter: ").lower()

if __name__ == "__main__":
   main()