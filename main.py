import random
import hangman
import hangman_art


chosen_word = random.choice(hangman.word_list)

lives =6
print(hangman_art.logo)
display = []
for _ in range(len(chosen_word)):
    display+="_"


end_of_game = False
while not end_of_game:
    guess= input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. you lose a life")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose")

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("You Win")
    print(hangman_art.stages[lives])
