
def read_file_to_list(filename):
    result = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            result.append(line.strip())
    return result