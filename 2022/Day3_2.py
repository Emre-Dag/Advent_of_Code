lowercase_priorities = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
uppercase_priorities = {chr(i): i - ord('A') + 1 + 26 for i in range(ord('A'), ord('Z') + 1)}

total_sum = 0

with open('input_Day3.txt', 'r') as f:
  lines = f.read().split('\n')
  for i in range(0, len(lines), 3):
    badge_items = set(lines[i])

    for j in range(i + 1, i + 3):
      badge_items &= set(lines[j])

    if badge_items:
      badge_item = list(badge_items)[0]
      if badge_item.islower():
        total_sum += lowercase_priorities[badge_item]
      else:
        total_sum += uppercase_priorities[badge_item]

print(total_sum)