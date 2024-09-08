# SpencerP3.py
# Programmer: Andrew Spencer
# Email: aspencer22@cnm.edu
# Date: 09/01/2024
# Purpose: Program will ask the user to type in a sentence that includes the name(s) of the fruit
# from the provided list. The program will then count the number of fruits in the sentence and
# display the list of fruits from the user's sentence. The program will then change the user's sentence by replacing
# one of the fruits with "Brussel Sprouts" and display the new sentence to the user.
# Python Version: 3.12.5
import string
import time

# Create list of 7 fruits
fruits = ['apple', 'banana', 'cherry', 'peach', 'watermelon', 'mango', 'grape']
print(' | '.join(fruits))

# Ask user to type in any sentence
sentence = input('Create a sentence using any of the fruits listed above: ').lower()

# Remove punctuation from the sentence, so it doesn't affect count
translator = str.maketrans('', '', string.punctuation)
# Apply the translation to the sentence with translate method
without_punct = sentence.translate(translator)


# Split the sentence into a list of words
sentence_list = without_punct.split()
# Print the sentence as a list of words, aka: elements --delete
# print(sentence_list)

# count each occurrence for the fruits in the sentence
fruits_in_sentence = list(filter(lambda x: x in fruits, sentence_list))

# Interim statement to make program more interactive
print('Evaluating your sentence...\n')
time.sleep(1.5)

# Tell the user how many fruits are in the sentence
print(f'I found {len(fruits_in_sentence)} fruit(s) in your sentence.')

# Tell the user which fruits were found in the sentence they provided
print('The following fruits were found in your sentence: \n' + ', '.join(fruits_in_sentence))
print('\n')

# Find and replace one instance of a fruit in the sentence with "Brussel Sprouts"
# Assign a variable to the first element of the list of fruits found in the sentence
find_word = fruits_in_sentence[0]
# Find the start index of the word found from the sentence
start_index = sentence.find(find_word)
# Find the end index of the word found from the sentence
end_index = start_index + len(find_word)
# Use the start and end indices to replace the word found with "Brussel Sprouts"
replace_word = sentence[:start_index] + 'Brussel Sprouts' + sentence[end_index:]

# Display the new sentence to the user
print('Here is your sentence changed with something more green:')
print(replace_word.capitalize())

# Thank the user for using the program
time.sleep(7)
print('\nThank you testing my fruit finder program!')
print('Please feel free to follow my progress on my Github page:')
print('https://github.com/trudruskii')