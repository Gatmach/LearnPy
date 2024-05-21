''' Welcoming to our guess game
The game prompts the user to enter the number of guess limit.
Guess_count is initialized to 0 in the beginning of the game and continue incrementing as the user continues guessing the secret password.
Initially, the out_of_guess is set to false and once the user enters the correct guess it turns to true...
'''

secret_pasword = "biljok"
guess = ' '
guess_limit = int(input("Enter a guess limit: "))
guess_count = 0
out_of_guesses = False
while guess != secret_pasword and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter a guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("out of Guesses, YOU LOSE!")
else:
    print("You win!")
