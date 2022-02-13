n = int(input())
cipher_message = input()
rotations = int(input())

encrypted_message = ''

for char in cipher_message:
    char_ascii_value = ord(char)
    if char.isalpha():

        if char.islower():
            for i in range(1, rotations + 1):
                char_ascii_value += 1
                if char_ascii_value > 122:
                    char_ascii_value = 97

        elif char.isupper():
            for i in range(1, rotations + 1):
                char_ascii_value += 1
                if char_ascii_value > 90:
                    char_ascii_value = 65

    encrypted_message += chr(char_ascii_value)

print(encrypted_message)
