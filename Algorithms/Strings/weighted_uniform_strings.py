from string import ascii_lowercase

given_string = input()

letters_values = {}
letter_value = 1

for char in ascii_lowercase:
    letters_values[char] = letter_value
    letter_value += 1

results = set()

last_char = ''
for char in given_string:
    if char != last_char:
        char_value = letters_values[char]
    else:
        char_value += letters_values[char]

    results.add(char_value)
    last_char = char

for query in range(int(input())):
    print('Yes' if int(input()) in results else 'No')
