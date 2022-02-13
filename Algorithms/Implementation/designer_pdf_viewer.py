import string

letter_heights = list(map(int, input().split()))
word = input()

alphabet_letters_heights = dict(zip(list(string.ascii_lowercase), letter_heights))
filtered_letters = {k: v for k, v in alphabet_letters_heights.items() if k in word}

max_height = max(filtered_letters.values())
print(max_height * len(word))
