import pandas

#get CSV and create a dataframe
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
table = pandas.DataFrame(alphabet)
nato_alphabet = {row.letter:row.code for (index, row) in table.iterrows()}

# Ask the user for their name
name = input("Enter your Name ").upper()

#search list for letters in the name
word = [nato_alphabet[n] for n in name if n in nato_alphabet]

#print the Nato words
print(word)
