import re
# parse file
# 1. initial state into dictionary
# {1: ["A", "B", "C"}, ..}
# 2. instructions into list [[1,2,1], [3,1,3]]

from common.utils import read_file_to_list

sample_stack = { 1: ["Z", "N"],
                 2: ["M", "C", "D"],
                 3: ["P"]}

stack = {1: ["R", "N", "F", "V", "L", "J", "S", "M"],
         2: ["P", "N", "D", "Z", "F", "J", "W", "H"],
         3: ["W", "R", "C", "D", "G"],
         4: ["N", "B", "S"],
         5: ["M", "Z", "W", "P", "C", "B", "F", 'N'],
         6: ["P", "R", "M", "W"],
         7: ["R", "T", "N", "G", "L", "S", 'W'],
         8: ["Q", "T", "H", "F", "N", "B", "V"],
         9: ["L", "M", "H", "Z", "N", "F"]
}


def parse_data():
    d = read_file_to_list("data.txt")
    instructions = d[d.index("")+1:]
    instructions_short = [re.findall(r"\d+", instruction) for instruction in instructions]
    return instructions_short


def make_a_move(move):
    move = [int(i) for i in move]
    how_many, from_col, to_col = move
    for _ in range(how_many):
        container = stack[from_col].pop()
        stack[to_col].append(container)

def make_a_move_part2(move):
    move = [int(i) for i in move]
    how_many, from_col, to_col = move

    containers = stack[from_col][-how_many:]
    stack[from_col] = stack[from_col][:-how_many]
    stack[to_col] = stack[to_col] + containers



if __name__ == '__main__':
    parse_data()
    instructions = parse_data()
    for instruction in instructions:
        make_a_move(instruction)
        # make_a_move_part2(instruction)

    result = [i[-1] for i in stack.values()]
    print("".join(result))



