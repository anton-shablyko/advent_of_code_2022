"""rock paper scissors"""

result = 0   
# a,x rock
# b,y paper
# c,z scissors


hand_weight = {"X": 1, "Y": 2, "Z": 3}


class Game:
    def __init__(self):
        self.result = 0

    def round_status(self, player_a, player_b):
        # identify the round outcome (w, l, t)

        possible_combo = {
            "AX": 3, "BY": 3, "CZ": 3,  # draw
            "AZ": 0, "BX": 0, "CY": 0,  # lost
            "AY": 6, "BZ": 6, "CX": 6   # win
        }
        round_combo = player_a + player_b
        self.result += possible_combo[round_combo]

    def play_round(self, player_a, player_b):
        # update result based on the hand choice
        self.result += hand_weight[player_b]
        self.round_status(player_a, player_b)  # update result based on the round outcome

def run():
    game = Game()
    with open("data.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            game.play_round(line[0], line[2])
    print(game.result)


if __name__ == '__main__':
    run()