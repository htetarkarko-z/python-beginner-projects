import pandas
data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dic = {row.letter: row.code for (index, row) in data_frame.iterrows()}
is_on = True
while is_on:
    user = input('Enter your word: ').upper()
    try:
        result_list = [nato_dic[letter] for letter in user]
    except KeyError:
        print('Sorry only letter in the alphabet')
    else:
        print(result_list)
        is_on = False
