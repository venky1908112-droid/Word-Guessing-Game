import random

with open("words.txt", "r") as file:
    words = file.read().splitlines()

word = random.choice(words)
max_chances = 7
guessed_word = [word[0]] + ['-'] * (len(word)-2) + [word[-1]]

print("Guess The Below Word")
print(''.join(guessed_word))
print()

while max_chances > 0 and '-' in guessed_word:
    print("Enter the guess letter: ")
    letter = input().lower()
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed_word[i] = letter
        print("Correct Guess!")
    else:
        print("Wrong guess")
        max_chances -= 1
    print(''.join(guessed_word))
    print("Chances Remaining: ",max_chances)

if '-' not in guessed_word:
    print("Congratuklations You have Won ❤️🌹")
else:
    print("Game Over Best Of Luck Next Time 🐍")
print("The Correct Answer is: ",word)