
def read_file_to_list(filename):
    result = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            result.append(line)
    return result