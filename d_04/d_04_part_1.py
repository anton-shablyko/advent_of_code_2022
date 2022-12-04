from common.utils import read_file_to_list

data = read_file_to_list("data_sample.txt")
print(data)


def get_list_from_range(section: str) -> list:
    begin, end = section.split("-")
    new_range = list(range(int(begin), int(end) + 1))
    return new_range


def get_sorted_list_from_range(section: str) -> list:
    sections = d.split(",")
    section_a = get_list_from_range(sections[0])
    section_b = get_list_from_range(sections[1])
    sorted_sections = sorted([section_a, section_b], key=len)
    return sorted_sections

def is_fully_intersected(sections):
    section_a, section_b = sections
    r = [i for i in section_a if i in section_b]
    if section_a == r:
        return True


result = 0
for d in data:
    sections = get_sorted_list_from_range(d)
    result += 1 if is_fully_intersected(sections) else 0
    print(f"{d} - {result}")
print(result)
