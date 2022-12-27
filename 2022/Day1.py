# Read the input from a file
with open('Input_Day1.txt', 'r') as f:
  input_data = f.read()

# Split the input data into a list of integers
listos = [x for x in input_data.split('\n\n') if x]


sums=[]
# Iterate over the list of integers
for stri in listos:
  # Add the current number to the result
  numbers = [int(x) for x in stri.split('\n') if x]
  
  total= sum(numbers)
  sums.append(total)

sums.sort(reverse=True)

top_sums = sums[:3]
res=sum(top_sums)
# Print the top 3 highest sums
print(res)