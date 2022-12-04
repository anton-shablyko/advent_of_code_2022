# a,x rock
# b,y paper
# c,z scissors

rules = {"win": ["AY", "BZ", "CX"],
         "lost": ["AZ", "BX", "CY"],
         "draw": ["AX", "BY", "CZ"]}

class Game:
    def __init__(self):
        self.result = 0

    def round_status(self, player_a, player_b):
        # update result based on the round outcome
        round_combo = player_a + player_b
        round_score = 0
        if round_combo in rules["win"]:
            round_score = 6
        elif round_combo in rules["draw"]:
            round_score = 3
        self.result += round_score

    def play_round(self, player_a, player_b):
        # update result based on the hand choice
        hand_weight = {"X": 1, "Y": 2, "Z": 3}
        self.result += hand_weight[player_b]
        self.round_status(player_a, player_b)  # update result based on the round outcome

    def update_player_b(self, player_a, player_b, desired_outcome):
        for i in rules[desired_outcome]:
            if player_a == i[0]:
                player_b = i[1]
        return player_b

    def new_player_b(self, player_a, player_b):
        if player_b == "Y":
            player_b = self.update_player_b(player_a, player_b, "draw")
        elif player_b == "Z":  # need to win
            player_b = self.update_player_b(player_a, player_b, "win")
        elif player_b == "X":  # need to lose
            player_b = self.update_player_b(player_a, player_b, "lost")
        return player_b

def run():
    game = Game()
    part_2 = False  # trigger between part 1 and 2
    with open("data.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            player_a, player_b = line[0], line[2]
            #  update player's b hand based on the desired outcome
            player_b = game.new_player_b(player_a, player_b) if part_2 else player_b
            game.play_round(player_a, player_b)
    print(game.result)

if __name__ == '__main__':
    run()