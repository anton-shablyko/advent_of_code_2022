#  taken from https://www.youtube.com/watch?v=YLHPABNNgZU
from collections import defaultdict

with open("data.txt") as f:
    blocks = ("\n" + f.read().strip()).split("\n$ ")[1:]

path = []
dir_sizes = defaultdict(int)  # {"/":1, "/a": 2, /a/e: 8 }
children = defaultdict(list)



def parse(block):
    lines = block.split("\n")
    command = lines[0]
    outputs = lines[1:]
    print(outputs)

    parts = command.split()
    operation = parts[0]
    if operation == "cd":
        if parts[1] == "..":
            path.pop()
        else:
            path.append(parts[1])

        # stop parsing block if command is cd
        return
    abspath = "/".join(path)

    size = 0
    for line in outputs:
        f_size, f_name = line.split()
        if f_size == "dir":
            children[abspath].append(f"{abspath}/{f_name}")
        else:
            size += int(f_size)
    dir_sizes[abspath] = size


for block in blocks:
    parse(block)


def get_folder_size(abspath):
    size = dir_sizes[abspath]
    for child in children[abspath]:
        size += get_folder_size(child)
    return size

# part 1
# result = 0
# for abspath in dir_sizes:
#     folder_size = get_folder_size(abspath)
#     result += folder_size if folder_size <=100_000 else 0

# part 2
total_space = 70_000_000
required_free_space = 30_000_000

for abspath in dir_sizes:
    folder_size = get_folder_size(abspath)
    dir_sizes[abspath] = folder_size

current_size = dir_sizes["/"]  # size of the root directory
current_free_size = total_space - current_size   # how much of space we have currently
space_to_free = required_free_space - current_free_size  # how much more is needed

result = current_size
for abspath, dir_size in dir_sizes.items():
    if space_to_free < dir_size <= result:
        result = dir_size

print(result)
