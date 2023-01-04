import itertools

sample_data = [("R", 4),
               ("U", 4),
               ("L", 3),
               ("D", 1),
               ("R", 4),
               ("D", 1),
               ("L", 5),
               ("R", 2)
               ]


# so we need to create a system of coordinates
# let's start at x:0 and y:0

class Rope:
    def __init__(self):
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0
        self.visited = []

    def is_tail_nearby(self):
        rows = [self.head_x - 1, self.head_x, self.head_x + 1]
        cols = [self.head_y - 1, self.head_y, self.head_y + 1]
        nearby_coordinates = []

        for r in itertools.product(rows, cols):
            nearby_coordinates.append(r)

        tail_coordinates = (self.tail_x, self.tail_y)

        return tail_coordinates in nearby_coordinates

    def make_move(self, step):
        direction, distance = step
        for _ in range(distance):
            if direction == "R":
                self.head_x += 1
                if not self.is_tail_nearby():
                    self.tail_x += 1
                    self.tail_y = self.head_y
                    self.visited.append((self.tail_x, self.tail_y))

            elif direction == "L":
                self.head_x += -1
                if not self.is_tail_nearby():
                    self.tail_x += -1
                    self.tail_y = self.head_y
                    self.visited.append((self.tail_x, self.tail_y))

            elif direction == "U":
                self.head_y += 1
                if not self.is_tail_nearby():
                    self.tail_y += 1
                    self.tail_x = self.head_x
                    self.visited.append((self.tail_x, self.tail_y))

            elif direction == "D":
                self.head_y += -1
                if not self.is_tail_nearby():
                    self.tail_y += -1
                    self.tail_x = self.head_x
                    self.visited.append((self.tail_x, self.tail_y))



def get_data():
    moves = []
    with open("data.txt", "r") as f:
        for move in f.readlines():
            direction, distance = move.strip().split()
            moves.append((direction, int(distance)))
    return moves

if __name__ == '__main__':
    r = Rope()
    # data = sample_data
    data = get_data()
    for step in data:
        r.make_move(step)

    print(set(r.visited))
    print(len(set(r.visited)))