secret_word = "Jose"
guess_count = 0
guess_limit = 3
user_guess = ""
out_of_guesses = False

while user_guess != secret_word and not(out_of_guesses):
    if guess_count <= guess_limit:
        user_guess = input("Enter guess: ")
        guess_count += 1
        print("Incorrect guess")
    else:
        out_of_guesses = True
if out_of_guesses == True:
    print("You lose")
else:
    print("You win!")