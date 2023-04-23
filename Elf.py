# Prompt the user to enter two words and remove leading/trailing whitespace
firstWord = input("Please enter the first word: ").strip()
secondWord = input("Please enter the second word: ").strip()

# Create an empty dictionary to store common letters and their counts
commonLetters = {}

# Loop over the letters in the first word
for letter in firstWord:
    # If the letter is also in the second word, add it to the commonLetters dictionary
    if letter in secondWord:
        commonLetters[letter] = commonLetters.get(letter, 0) + 1

# Calculate and print the result
result = len(firstWord) + len(secondWord) - 2 * sum(commonLetters.values())
print(f'Result: {result}')
