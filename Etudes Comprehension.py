"""
Created on Thu Apr 19 19:28:53 2018

for Python 3.5
"""

number_list = list(range(1, 6))
print(number_list)

number_list2 = [number for number in range(1, 6)]
print(number_list2)

even_list = [number for number in range(1, 6) if number % 2 == 0]
print(even_list)

# Tuple comprehension
cell = [(row, col) for row in range(1, 3) for col in range(5, 8)]
print(cell)

# Use tuple unpacking
for row, col in cell:
    print(row, col)

# Dictionnary comprehension
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
