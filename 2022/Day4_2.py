with open('input_Day4.txt', 'r') as f:
    pairs = f.readlines()

count = 0

for pair in pairs:
    a, b = pair.split(',')

    range_a = range(int(a.split('-')[0]), int(a.split('-')[1]) + 1)
    range_b = range(int(b.split('-')[0]), int(b.split('-')[1]) + 1)

    if any(i in range_b for i in range_a):
        count += 1

print(count)