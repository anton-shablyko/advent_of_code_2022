data = {"/": {"size":0, "parent": None, "children": ["a", "d"], "files": [(14848514, "b.txt"), (8504156, "c.dat")]},
        "a": {"size":0, "parent": "/", "children": ["e"], "files": [(29116, "f"), (2557, "g"), (62596, "h.lst")]},
        "e": {"size":0, "parent": "a", "children": None, "files": [(584, "i")]},
        "d": {"size":0, "parent": "/", "children": None, "files": [(4060174, "j"),
                                                         (8033020, "d.log"),
                                                         (5626152, "d.ext"),
                                                         (7214296, "k")]}}

chains = []

result = {}

temp_data = data

while temp_data:
    for d, val in data.items():
        if not val["children"]:
            data[d]["size"] += sum([f[0] for f in data[d]["files"]])
            parent = val["parent"]
            if parent:
                data[parent]["size"] += sum([f[0] for f in data[d]["files"]])
                temp_data[parent]["children"].remove(d)
                result[d] = data[d]["size"]

    print(data)

print(result)






# {'/': {'size': 24933642, 'parent': None, 'children': ['a', 'd'], 'files': [(14848514, 'b.txt'), (8504156, 'c.dat')]},
#  'a': {'size': 584, 'parent': '/', 'children': ['e'], 'files': [(29116, 'f'), (2557, 'g'), (62596, 'h.lst')]},
#  'e': {'size': 584, 'parent': 'a', 'children': None, 'files': [(584, 'i')]},
#  'd': {'size': 24933642, 'parent': '/', 'children': None, 'files': [(4060174, 'j'), (8033020, 'd.log'), (5626152, 'd.ext'), (7214296, 'k')]}}
#
#
# {'/': {'size': 24933642, 'parent': None, 'children': ['a'],
#        'files': [(14848514, 'b.txt'), (8504156, 'c.dat')]},
#  'a': {'size': 584, 'parent': '/', 'children': [], 'files': [(29116, 'f'), (2557, 'g'), (62596, 'h.lst')]},
#  'e': {'size': 584, 'parent': 'a', 'children': None, 'files': [(584, 'i')]},
#  'd': {'size': 24933642, 'parent': '/', 'children': None, 'files': [(4060174, 'j'), (8033020, 'd.log'), (5626152, 'd.ext'), (7214296, 'k')]}}
