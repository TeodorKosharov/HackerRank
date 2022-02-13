for query in range(int(input())):
    word = input()

    deletions = 0
    for index in range(len(word) - 1):
        if word[index] == word[index + 1]:
            deletions += 1

    print(deletions)
