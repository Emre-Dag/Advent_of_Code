# Open the file in read mode
with open('aoc_input_day2.txt', 'r') as f:
  # Read all the lines of the file into a list
  lines = f.readlines()
  horizontal=0
  depth=0
  aim=0
  # Iterate through the list of lines
  for i,line in enumerate(lines):
    # Get the first letter of the line
    first_letter = line[0]
    
    if i == len(lines)-1:
        if first_letter=='f':
            horizontal += int(line[-1])
            depth+=(int(line[-1])*aim)
        elif first_letter=='d':
            aim+=int(line[-1])
        elif first_letter=='u':
            aim-=int(line[-1])
    else:
        if first_letter=='f':
            horizontal += int(line[-2])
            depth+=(int(line[-2])*aim)
        elif first_letter=='d':
            aim+=int(line[-2])
        elif first_letter=='u':
            aim-=int(line[-2])
    
# Print the first letter
print("h="+str(horizontal))
print("d="+str(depth))
print("Mult="+str(horizontal*depth))
