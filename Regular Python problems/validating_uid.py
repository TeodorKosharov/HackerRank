for _ in range(int(input())):
    given_uid = input()
    if len(given_uid) != len(set(given_uid)) or len(given_uid) != 10:
        print('Invalid')
    else:
        uppers = 0
        digits = 0
        for char in given_uid:
            if not char.isalnum():
                print('Invalid')
                continue
            if char.isupper():
                uppers += 1
            elif char.isdigit():
                digits += 1
        if uppers >= 2 and digits >= 3:
            print('Valid')
        else:
            print('Invalid')
