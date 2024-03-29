with open('input.txt', encoding='utf-8') as file:
    k = int(file.readline())
    data = file.readlines()

with open('output.txt', encoding='utf-8', mode='w') as f:
    count = 0
    for i in data:
        name, age, breed = i.split()
        if int(age) < k:
            f.write(f'{name} {age} {breed}\n')
            count += 1
    f.write(f'{count}')
