lowercase_priorities = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
uppercase_priorities = {chr(i): i - ord('A') + 1 + 26 for i in range(ord('A'), ord('Z') + 1)}

total_sum = 0

with open('input_Day3.txt', 'r') as f:
  for line in f:
    compartment1 = set(line[:len(line)//2])
    compartment2 = set(line[len(line)//2:])

    common_items = compartment1 & compartment2

    for item in common_items:
      if item.islower():
        total_sum += lowercase_priorities[item]
      else:
        total_sum += uppercase_priorities[item]

print(total_sum)