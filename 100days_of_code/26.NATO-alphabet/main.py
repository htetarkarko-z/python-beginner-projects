import pandas
data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dic = {row.letter: row.code for (index, row) in data_frame.iterrows()}
user = input('Enter your word: ').upper()
result_list = [nato_dic[letter] for letter in user]
print(result_list)
