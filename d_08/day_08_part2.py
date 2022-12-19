import numpy as np


data_sample = [[3, 0, 3, 7, 3],
               [2, 5, 5, 1, 2],
               [6, 5, 3, 3, 2],
               [3, 3, 5, 4, 9],
               [3, 5, 3, 9, 0]
        ]


def get_data():
    """Parse the real input as sample data above"""
    forest = []
    with open("forest.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            forest.append([i for i in line.strip()])
    return forest


def get_direction_distance(direction, tree):
    distance = 0
    for i in direction:
        if i < tree:
            distance += 1
        else:
            distance += 1
            return distance
    return distance

def get_total_view_distance(x, y, tree):
    views = []
    row = data[y]
    left, right = row[:x][::-1], row[x + 1:]  # reverse left and up parts by [::-1]
    col = [d[x] for d in data]
    up, down = col[:y][::-1], col[y+1:]

    directions = [left, right, up, down]
    for d in directions:
        views.append(get_direction_distance(d, tree))
    return np.prod(views)


if __name__ == '__main__':
    best_view_distance = 0

    data = get_data()

    for enum_row, row in enumerate(data):
        for enum_col, col in enumerate(row):
            # if outer layer - view distance is 0
            if enum_row in (0, len(data) - 1) or enum_col in (0, len(row) - 1):
                view_distance = 0
            else:
                view_distance = get_total_view_distance(enum_col, enum_row, col)

            if view_distance > best_view_distance:
                best_view_distance = view_distance

    print(best_view_distance)









