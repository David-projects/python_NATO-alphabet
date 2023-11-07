import pandas

#get CSV and create a dataframe
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
table = pandas.DataFrame(alphabet)
nato_alphabet = {row.letter:row.code for (index, row) in table.iterrows()}

try_input = True
while try_input:
    try:
        # Ask the user for their name
        name = input("Enter your Name ").upper()
        if len(name) == 0 or not name.isalpha():
            raise ValueError("Please input a string")

    except ValueError as massage:
        print(massage)
    else:
        #search list for letters in the name
        word = [nato_alphabet[n] for n in name if n in nato_alphabet]
        try_input = False
        #print the Nato words
        print(word)
