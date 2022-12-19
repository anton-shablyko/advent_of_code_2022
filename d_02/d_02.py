"""rock paper scisors"""

result = 0   

def game(player_a, player_b):
    
       
                
with open("data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        player_a, player_b = line[0], line[2]
        game(player_a, player_b)