sample = input()
letters = {}

while len(sample) > 0:
    letters.update({sample[0]: sample.count(sample[0])})
    sample = sample.replace(sample[0], '')

letters = dict(sorted(letters.items(), key=lambda x: (-x[1], x[0])))

step = 0
for key, value in letters.items():
    if step == 3:
        break
    print(f'{key} {value}')
    step += 1
