result = []
n = int(input())
for _ in range(n):
    command = input()
    if command == 'print':
        print(result)

    command_list = command.split()
    action = command_list[0]

    if action == 'insert':
        position = int(command_list[1])
        value = int(command_list[2])
        result.insert(position, value)

    elif action == 'remove':
        value = int(command_list[1])
        result.remove(value)

    elif action == 'append':
        value = int(command_list[1])
        result.append(value)

    elif action == 'sort':
        result.sort()

    elif action == 'pop':
        result.pop()

    elif action == 'reverse':
        result.reverse()
