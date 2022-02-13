import re

regex_integer_in_range = r'^\d{6}$'
regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'
number = input()

print(bool(re.match(regex_integer_in_range, number)) and len(
    re.findall(regex_alternating_repetitive_digit_pair, number)) < 2)
