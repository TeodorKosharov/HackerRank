if __name__ == '__main__':
    s = input()

    print(any([True if char.isalnum() else False for char in s]))
    print(any([True if char.isalpha() else False for char in s]))
    print(any([True if char.isdigit() else False for char in s]))
    print(any([True if char.islower() else False for char in s]))
    print(any([True if char.isupper() else False for char in s]))
