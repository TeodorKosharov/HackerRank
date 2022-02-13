given_time = input()

if 'PM' in given_time:
    given_time = (given_time.replace('PM', '')).split(':')
    if given_time[0] != '12':
        print(f'{int(given_time[0]) + 12}:{":".join(given_time[1:])}')
    else:
        print(':'.join(given_time))

elif 'AM' in given_time:
    given_time = (given_time.replace('AM', '')).split(':')
    if given_time[0] != '12':
        print(':'.join(given_time))
    else:
        print(f'00:{":".join(given_time[1:])}')
