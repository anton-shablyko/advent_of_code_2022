
class Monkey:
    def __init__(self,   items: list, test_value: int, conditions: tuple , operation: tuple):
        self.items = items
        self.test_value = test_value
        self.conditions = conditions
        self.operation = operation
        self.inspected = 0


    def get_worry_level(self, item):
        sign, number = self.operation
        if sign == "*":
            item *= number
        elif sign == "+":
            item += number
        else:
            item = item**2
        return item//3

    def check_conditions(self, worry_level):
        t, f = self.conditions
        if worry_level % self.test_value == 0:
            monkeys[t].items.append(worry_level)
        else:
            monkeys[f].items.append(worry_level)

    def monkey_run(self):
        for item in self.items:
            # self.inspected += 1
            worry_level = self.get_worry_level(item)
            self.check_conditions(worry_level)
        self.inspected += len(self.items)
        self.items = []

#  test monkeys
# m0 = Monkey(items=[79, 98], test_value=23, conditions=(2, 3), operation=("*", 19))
# m1 = Monkey(items=[54, 65, 75, 74], test_value=19, conditions=(2, 0), operation=("+", 6))
# m2 = Monkey(items=[79, 60, 97], test_value=13, conditions=(1, 3), operation=("**", 2))
# m3 = Monkey(items=[74], test_value=17, conditions=(0, 1), operation=("+", 3))
# monkeys = {0: m0, 1: m1, 2: m2, 3: m3}

#  real monkeys
m0 = Monkey(items=[85, 77, 77], test_value=19, conditions=(6, 7), operation=("*", 7))
m1 = Monkey(items=[80, 99], test_value=3, conditions=(3, 5), operation=("*", 11))
m2 = Monkey(items=[74, 60, 74, 63, 86, 92, 80], test_value=13, conditions=(0, 6), operation=("+", 8))
m3 = Monkey(items=[71, 58, 93, 65, 80, 68, 54, 71], test_value=7, conditions=(2, 4), operation=("+", 7))
m4 = Monkey(items=[97, 56, 79, 65, 58], test_value=5, conditions=(2, 0), operation=("+", 5))
m5 = Monkey(items=[77], test_value=11, conditions=(4, 3), operation=("+", 4))
m6 = Monkey(items=[99, 90, 84, 50], test_value=17, conditions=(7, 1), operation=("**", 2))
m7 = Monkey(items=[50, 66, 61, 92, 64, 78], test_value=2, conditions=(5, 1), operation=("+", 3))

monkeys = {0: m0, 1: m1, 2: m2, 3: m3, 4: m4, 5: m5, 6: m6, 7: m7}

for round in range(1, 21):
    print(f"Playing {round} round")
    for _, monkey in monkeys.items():
        monkey.monkey_run()
    # print(f"After round {round}:"
    #       f"\nMonkey_0 = {m0.items}, inspected: {m0.inspected}"
    #       f"\nMonkey_1 = {m1.items}, inspected: {m1.inspected}"
    #       f"\nMonkey_2 = {m2.items}, inspected: {m2.inspected}"
    #       f"\nMonkey_3 = {m3.items}, inspected: {m3.inspected}")

inspected = []
for _, monkey in monkeys.items():
    inspected.append(monkey.inspected)

result = sorted(inspected)[-2:]
print(result[0] * result[1])








