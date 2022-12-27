with open('input_Day.txt', 'r') as f:
    pairs = f.readlines()

count = 0

for pair in pairs:
    a, b = pair.split(',')

    range_a = range(int(a.split('-')[0]), int(a.split('-')[1]) + 1)
    range_b = range(int(b.split('-')[0]), int(b.split('-')[1]) + 1)

    if range_a.start <= range_b.start and range_a.stop >= range_b.stop:
        count += 1
    elif range_b.start <= range_a.start and range_b.stop >= range_a.stop:
        count += 1

print(count)