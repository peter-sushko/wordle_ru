'''
This module is for dealing with the raw data.

The original data_set of nouns came from here:

The purpose of this module is to filter the nouns to contain
only 5-letter ones. Additionally, I need to substitute the
'ё' letter with the 'е' as this is specified in the game.
Such substitution is common in most word games like
crosswords and such.

Lastly, I removed all duplicates associated with the 
'ё' to 'е' substitution and remove 'хи-хи' as it contained 
a special character.

Note to self:
Cite the data source.
Attached the code that identified duplicates.
'''

import csv

five_digit_strings = []
CSV_FILE = 'five_letter_nouns.csv'
TXT_FILE = 'five_letter_nouns.txt'

with open('all_nouns.txt', 'r', encoding='utf-8') as file:
    five_digit_strings = []
    for line in file:
        words = line.split()
        for word in words:
            word = word.replace('ё', 'е')
            if len(word) == 5:
                five_digit_strings.append(word)

# Removing duplicated words that arose during the ('ё', 'е') replacement.
words_to_remove = {'хи-хи', 'ведро', 'дрема', 'ерник', 'желчь',
                   'метка', 'падеж', 'пенье', 'чабер', 'шабер'}

five_digit_strings = [word for word in five_digit_strings if word not in words_to_remove]


with open(CSV_FILE, 'w', encoding = 'utf-8', newline = '') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(five_digit_strings)

print(f'List has been saved to {CSV_FILE}')

with open(TXT_FILE, 'w', encoding = 'utf-8') as file:
    for item in five_digit_strings:
        file.write(f"{item}\n")

print(f'List has been saved to {TXT_FILE}')
