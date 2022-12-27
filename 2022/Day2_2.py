opponent_shapes = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
outcomes = {'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}

total_score = 0

with open('input_Day2.txt', 'r') as f:
  for line in f:
    opponent_shape, outcome = line.strip().split()
    opponent_shape = opponent_shapes[opponent_shape]
    outcome = outcomes[outcome]
    
    if outcome == 'Win':
      if opponent_shape == 'Scissors':
        total_score += 6 + 3  
      elif opponent_shape == 'Rock':
        total_score += 6 + 1  
      else:
        total_score += 6 + 2  
    elif outcome == 'Draw':
        
      if opponent_shape == 'Scissors':
        total_score += 3+ 3
        
      elif opponent_shape == 'Rock':
        total_score += 3 + 1
        
      else:
        total_score += 3 + 2
        
    else:
      if opponent_shape == 'Scissors':
        total_score += 2
        
      elif opponent_shape == 'Rock':
        total_score += 3
        
      else:
        total_score += 1
        
print(total_score)
