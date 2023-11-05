# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
import pandas

#with open("nato_phonetic_alphabet.csv") as data:
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

table = pandas.DataFrame(alphabet)

print(table)

nato_alphabet = {row.letter:row.code for (index, row) in table.iterrows()}
print(nato_alphabet)
#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
#    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

