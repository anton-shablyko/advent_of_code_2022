import string

alphabet = string.ascii_lowercase + string.ascii_uppercase
ranges = [i for i in range(1, 53)]
rules = dict(zip(list(alphabet), ranges))

with open("data.txt", "r") as f:
    lines = [i.strip() for i in f.readlines()]
    result = 0
    n = 3

    sets = [lines[i * n:(i + 1) * n] for i in range((len(lines) + n - 1) // n)]

    for s in sets:
        set_a, set_b, set_c = s
        matches_a = set([i for i in set_a if i in set_b])
        matches = set([i for i in matches_a if i in set_c])

        for match in matches:
            result += rules[match]

    print(result)

