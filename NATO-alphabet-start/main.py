import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(f'{index} ---> {row.student} scored {row.score}')

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

phonoetic = pandas.read_csv('nato_phonetic_alphabet.csv')
phonoetic_dict = {row.letter:row.code for (index, row) in phonoetic.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter a word to return its phonetic ')
word_list = [phonoetic_dict[letter.upper()] for letter in list(word)]

print(f'The phonetics for the entered word is {word_list}')

