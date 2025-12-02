# import random

def hangman():
    words = ["python", "coding", "hangman", "developer", "program"]
    chosen_word = random.choice(words)
    guessed = ["_"] * len(chosen_word)
    attempts = 6
    guessed_letters = []

    print("🎮 Welcome to Hangman Game!")
    print("Guess the word:")

    while attempts > 0:
        print("\nWord:", " ".join(guessed))
        print(f"Attempts left: {attempts}")
        print("Guessed letters:", guessed_letters)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("✔ Correct guess!")

            for i in range(len(chosen_word)):
                    guessed[i] = guess
        else:
            print("❌ Wrong guess!")
            attempts -= 1

        if "_" not in guessed:
            print("\n🎉 Congratulations! You guessed the word:", chosen_word)
            break

    if attempts == 0:
        print("\n💀 You lost! The word was:", chosen_word)

hangman()
