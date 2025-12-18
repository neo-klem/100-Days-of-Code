import random
from stickguyhangman import stickguy
from words import words
#words = ["midnajt", "ica", "sergej", "andjela", "nikola", "emilija", "mia"]
secret_word = random.choice(words).lower()
#secret_word = random.choice(words).lower()
lives = 6
blanks = []
wrong_guesses = []
for i in range(len(secret_word)):
    blanks += "_"
print("""                                           
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)
while lives > 0:
    print(stickguy[6 - lives])
    blanks_word = "".join(blanks)
    if len(wrong_guesses) > 0:
        print(f"Wrong letters: {wrong_guesses}") 
    if blanks_word == secret_word:
        print(f"The word is {secret_word}.\nYou WON!")
        break
    print(f"Word to guess: {blanks_word}")
    if lives < 6:
        print(f"*************** {lives}/6 LIVES LEFT ***************")
    input_letter = input("Guess a letter: ")
    if input_letter in secret_word:
        letter_index = 0
        count = 0
        for i in secret_word:
            if i == input_letter:
                letter_index = count
                blanks[letter_index] = input_letter
                count += 1
            else:
                count += 1
    elif input_letter in wrong_guesses:
        print(f"You already tried {input_letter}, try again. ")
    else:
        lives -= 1
        wrong_guesses.append(input_letter)
if lives <= 0:
    print(stickguy[6])
    print(f"The secret word is: {secret_word}")
    print("You LOSE!")
    
