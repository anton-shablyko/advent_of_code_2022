# a,x rock
# b,y paper
# c,z scissors

rules = {"win": ["AY", "BZ", "CX"],
         "lose": ["AZ", "BX", "CY"],
         "draw": ["AX", "BY", "CZ"]}

class Round:
    def __init__(self, hand_combo):
        self.hand_combo = hand_combo

    def round_outcome_score(self) -> int:
        """Get a score of the round outcome
        :return: 0 if round is lost
                 3 if round is draw
                 6 if round is won
        """
        round_score = 0
        if self.hand_combo in rules["win"]:
            round_score = 6
        elif self.hand_combo in rules["draw"]:
            round_score = 3
        return round_score

    def my_choice_score(self, my_move: str) -> int:
        """
        Get a score based on my move choice
        :param choice: X,Y or Z
        :return: corresponding score for each choice
        """
        hand_score = {"X": 1, "Y": 2, "Z": 3}
        return hand_score[my_move]

    def play_round(self):
        choice_score = self.my_choice_score(self.hand_combo[-1])
        round_outcome_score = self.round_outcome_score()
        return choice_score + round_outcome_score


class Hand:
    def __init__(self, hand_a, hand_b):
        self.hand_a = hand_a
        self.hand_b = hand_b


    def update_hand_b(self, desired_outcome):
        for i in rules[desired_outcome]:
            if self.hand_a == i[0]:
                self.hand_b = i[1]
        return self.hand_b

    def update_hand_combo(self, ):
        if self.hand_b == "Y":  # need to draw
            self.hand_b = self.update_hand_b("draw")
        elif self.hand_b == "Z":  # need to win
            self.hand_b = self.update_hand_b("win")
        elif self.hand_b == "X":  # need to lose
            self.hand_b = self.update_hand_b("lose")

    def get_hand_combo(self, part):
        if part == 2:
            self.update_hand_combo()
        return self.hand_a + self.hand_b


def run():
    game_score = 0
    challenge_part = 2
    with open("data.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            hand_a, hand_b = line[0], line[2]
            hand = Hand(hand_a, hand_b)
            combo = hand.get_hand_combo(challenge_part)

            round_score = Round(combo).play_round()
            game_score += round_score

    print(game_score)

if __name__ == '__main__':
    run()