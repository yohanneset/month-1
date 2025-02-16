n = int(input('Enter the range of nums: '))
print(f'the list of all even numbers less or equal than {n}: ')
for i in range(2, n + 1):
    if i % 2 == 0:
        print(i, end=' ')