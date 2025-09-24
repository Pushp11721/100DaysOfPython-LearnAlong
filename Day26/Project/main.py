import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
df=pandas.read_csv("nato_phonetic_alphabet.csv")
dict_alpha={row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input=list(input("Write your word : ").upper())
phonetic_words=[dict_alpha[char] for char in user_input]
# for char in user_input:
#     phonetic_words.append(dict_alpha[char])
print(phonetic_words)


