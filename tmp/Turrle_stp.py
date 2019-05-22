coords = [0, 0]
for i in range(int(input())):
    command = [i for i in input().split()]
    if command[0] == 'север':
        coords[1] += int(command[1])
    elif command[0] == 'юг':
        coords[1] -= int(command[1])
    elif command[0] == 'запад':
        coords[0] -= int(command[1])
    elif command[0] == 'восток':
        coords[0] += int(command[1])
print(' '.join(str(i) for i in coords))