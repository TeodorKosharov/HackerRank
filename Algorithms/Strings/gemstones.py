gems = 0
words = set()

for _ in range(int(input())):
    words.add(input())

longest_word = set(max(words, key=len))

for char in longest_word:
    for word in words:
        if char not in word:
            break
    else:
        gems += 1

print(gems)
