opponent_shapes = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
my_shapes = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}

total_score = 0

with open('input_Day2.txt', 'r') as f:
  for line in f:
    opponent_shape, my_shape = line.strip().split()
    opponent_shape = opponent_shapes[opponent_shape]
    my_shape = my_shapes[my_shape]
    
    if my_shape == 'Rock' and opponent_shape == 'Scissors':
      total_score += 6 + 1
      
    elif my_shape == 'Paper' and opponent_shape == 'Rock':
      total_score += 6 + 2
      
    elif my_shape == 'Scissors' and opponent_shape == 'Paper':
      total_score += 6 + 3
      
    elif my_shape == opponent_shape:
        
          if my_shape == 'Rock':
              total_score += 3 + 1
              
          elif my_shape == 'Paper':
              total_score += 3 + 2
              
          elif my_shape == 'Scissors':
              total_score += 3 + 3
    else:
          if my_shape == 'Rock':
              total_score += 1
              
          elif my_shape == 'Paper':
              total_score += 2
              
          elif my_shape == 'Scissors':
              total_score += 3


print(total_score)