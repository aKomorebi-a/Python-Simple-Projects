import random

word_bank = ['skibidi', 'goku', 'balatro', 'oblivion', 'game']

word = random.choice(word_bank)

guessedWord = ["_"] * len(word)

attempts = 5

while attempts > 0:
    print('\nPalabra actual: ' + ''.join(guessedWord))
    guess = input("Introduce una letra: ")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('muy buena bro')
    else:
        attempts -= 1
        print("No adivinaste, te quedan: " + str(attempts))
    if '_' not in guessedWord:
        print("\nFelicitaciones adivinaste!, la palabra es: " + word)
        break
else:
    print("\nTe\"quedaste sin intentos, la palabra es: " + word)
