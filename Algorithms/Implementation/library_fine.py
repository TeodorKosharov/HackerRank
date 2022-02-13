d1, m1, y1 = map(int, input().split())  # day, month, year on which the book was returned
d2, m2, y2 = map(int, input().split())  # day, month, year on which the book was due to be returned

if y1 == y2:
    if m1 < m2:
        print(0)
    elif m1 > m2:
        print((m1 - m2) * 500)
    elif m1 == m2:
        if d1 <= d2:
            print(0)
        else:
            print((d1 - d2) * 15)
elif y1 < y2:
    print(0)
else:
    print(abs(y1 - y2) * 10_000)
