
def get_data():
    with open("data.txt", "r") as f:
        lines = f.readlines()
        data = [l.strip() for l in lines]
    return data


class Chip:
    def __init__(self):
        self.history = []
        self.register = 1

    def process_instructions(self, instruction):
        instruction = instruction.split()
        command = instruction[0]
        if command == "noop":
            self.history.append(self.register)

        elif command == "addx":
            argument = int(instruction[-1])
            for i in range(2):
                self.history.append(self.register)
            self.register += argument


if __name__ == '__main__':
    data = get_data()

    c = Chip()
    for d in data:
        c.process_instructions(d)

    result = 0
    cycles = [20, 60, 100, 140, 180, 220]
    for cycle in cycles:
        x = c.history[cycle - 1]
        result += x * cycle

    print(result)






