
data_sample = [[3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0]
        ]


def get_data():
    forest = []
    with open("forest.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            row = [i for i in line.strip()]
            forest.append(row)
    return forest



def is_tree_visible(x, y, tree):
    """
    :param x: x coordinate
    :param y: y coordinate
    :param tree: tree value
    :return: True if visible false if not
    """
    print(f"tree: {tree}, x: {x}, y: {y}")
    # check_left_right
    # based on y select row
    row = data[y]
    #  get the highest tree on the left and on the right
    max_left, max_right = max(row[:x]), max(row[x+1:])

    if tree > max_left or tree > max_right:
        return True

    #  check up and down:
    column = [d[x] for d in data]
    max_up, max_down = max(column[:y]), max(column[y+1:])

    if tree > max_up or tree > max_down:
        return True


if __name__ == '__main__':
    visible_trees = 0
    data = get_data()
    for enum_row, row in enumerate(data):
        for enum_col, col in enumerate(row):
            if enum_row in (0, len(data) - 1) or enum_col in (0, len(row) - 1):
                visible_trees += 1
            else:
                visible_trees += 1 if is_tree_visible(enum_col, enum_row, col) else 0

    print(visible_trees)










