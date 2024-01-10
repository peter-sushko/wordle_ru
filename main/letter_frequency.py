'''
For plotting frequency of each letter.
'''

import csv
from collections import Counter
import matplotlib.pyplot as plt

CSV_FILE = '../data_processing/five_letter_nouns.csv'
letter_counter = Counter()

with open(CSV_FILE, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        text = ' '.join(row)
        text = ''.join(filter(str.isalpha, text)).lower()
        letter_counter.update(text)

sorted_data = sorted(letter_counter.items(), key=lambda x: x[1], reverse=True)

letters = [item[0] for item in sorted_data]
frequencies = [item[1] for item in sorted_data]

plt.figure(figsize=(14, 6))
plt.bar(letters, frequencies)
plt.xlabel('Letters')
plt.ylabel('Occurrences')
plt.title('Letter Occurrences in Five-Letter Nouns (Descending Order)')
plt.show()

plt.savefig('letter_frequencies.png')  # Saving the plot.
