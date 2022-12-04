import string

alphabet = string.ascii_lowercase + string.ascii_uppercase
ranges = [i for i in range(1, 53)]
rules = dict(zip(list(alphabet), ranges))

with open("data.txt", "r") as f:
    lines = f.readlines()
    result = 0
    for line in lines:
        line = line.strip()
        half_point = int(len(line)/2)
        compartment_a, compartment_b = line[:half_point], line[half_point:]
        matches = set([i for i in compartment_a if i in compartment_b])

        for match in matches:
            result += rules[match]

    print(result)
