import numpy as np

def get_data():
    with open("data.txt", "r") as f:
        lines = f.readlines()
        data = [l.strip() for l in lines]
    return data

#
class Chip:
    def __init__(self):
        self.register = 1
        self.cycle = 0
        self.screen = []
        self.sprite = [0, 1, 2]


    def draw(self):
        # print(f"\tcycle: {self.cycle}")
        # print(f"\tsprite: {self.sprite}")
        # print(f"\tregister: {self.register}")

        if self.cycle in self.sprite:
            self.screen.append("#")
        else:
            self.screen.append(" ")
        self.cycle = 0 if self.cycle == 39 else (self.cycle + 1)

        #
        # if self.cycle == 39:
        #     self.cycle = 0
        # else:
        #     self.cycle += 1


    def process_instructions(self, instruction):
        instruction = instruction.split()
        command = instruction[0]

        if command == "noop":
            self.draw()

        elif command == "addx":
            argument = int(instruction[-1])
            for i in range(2):
                self.draw()
            self.register += argument
            self.sprite = [self.register - 1, self.register, self.register + 1]


if __name__ == '__main__':
    data = get_data()

    c = Chip()
    for d in data:
        c.process_instructions(d)

    screen = list(np.array_split(c.screen, 6))

    for s in screen:
        print("".join(s))

