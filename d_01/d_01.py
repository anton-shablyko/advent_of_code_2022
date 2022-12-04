f = open("data.txt", "r")
data = f.read().split("\n")

elves = []

temp_elf = 0
for record in data:
    if record:
        temp_elf += int(record)
    else:
        elves.append(temp_elf)
        temp_elf = 0    
elves.sort(reverse=True)

print(f"Top 1 elf carries: {elves[0]} calories")
print(f"Top 3 elves carry {sum(elves[:3])} calories ")
