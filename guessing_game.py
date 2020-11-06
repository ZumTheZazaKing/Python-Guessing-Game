import random
import time

print("\n-----------------------------------------------------------")
print("       Welcome to ZumTheZazaKing's Number Guessing Game!     ")
print("-----------------------------------------------------------\n")


def main():

 time.sleep(3)

 num = random.randint(1, 100000)

 guess = int(input("\nGuess a number from 1 to 100,000:"))

 while num != guess:
	 print("")

	 if guess < num:
		 print("Your guess was low. Try again.")
		 time.sleep(1)
		 guess = int(input("Guess a number from 1 to 100,000:"))

	 elif guess > num:
		 print("Your guess was high. Try again.")
		 time.sleep(1)
		 guess = int(input("Guess a number from 1 to 100,000:"))

	 else:
          print("An error occured.")

 else:
    time.sleep(0.5)
    print("\nCongratulations! You guessed it!\n")


while True:
    main()
    time.sleep(2)
    if str(input("""Would you like to play again?
(Type Y(Yes) or N(No))\n
""")).strip().upper() != "Y":
      print("\nGoodbye!\n")
      time.sleep(1)
      break
