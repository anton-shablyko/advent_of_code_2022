from common.utils import read_file_to_list


"""sample
dirs = {"/":{"parent": None, "size": 0, "files": {"a": 123, "b": 321}},
        "a":{"parent": "/", "size": 0, "files": {"c": 133, "e": 323}}}
        
"""

class FileSystem():
    def __init__(self):
        self.dirs = {"/": {"parent": None, "files": {}}}
        self.work_path = ["/"]
        self.current_dir = self.work_path[-1]

    def navigate_to(self, command):
        print(command)
        location = command.split()[-1]
        # check if folder exist
        if location == "..":
            self.work_path = self.work_path[:-1]
            self.current_dir = self.work_path[-1]

        elif location not in self.dirs:
            self.dirs.update({location: {"parent": self.current_dir, "files": {}}})
            self.work_path.append(location)
            self.current_dir = location

        elif location in self.dirs:
            self.work_path.append(location)
            self.current_dir = location

        print(self.work_path)

    def ls(self, result):
        print(result)
        files = [r for r in result if r[0].isdigit()]
        for file in files:
            f_size, f_name = file.split()
            self.dirs[self.current_dir]["files"].update({f_name: int(f_size)})

    def get_folder_size(self, dirs):
        result = {}
        for d, v in self.dirs.items():
            s = sum(v["files"].values())
            result.update({d: {"sum": s, "parent": v["parent"]}})
        print(result)

        final_result = {}
        for r, v in result.items():
            final_result[r] = v["sum"]
            parent = v["parent"]
            if parent:
                final_result[r] += v["sum"]
        print(final_result)
        return result


    def get_part_1_answer(self, folder_sizes):
        x = 0
        new_order = {}
        for i, v in folder_sizes.items():
            dir_size = v["sum"]
            new_order[i] = v["sum"]
            if v["parent"]:
                new_order[v["parent"]] += v["sum"]

        for i, v in new_order.items():
            x += v if v <= 100000 else 0
        print("no", new_order)
        return x

    def main(self, data):
        ls_result = []
        print(data)
        for d in data:
            if d.startswith("$ cd"):
                if ls_result:
                    self.ls(ls_result)
                    ls_result = []
                self.navigate_to(d)
            else:
                ls_result.append(d)
        self.ls(ls_result)
        print(self.dirs)

        folder_sizes = self.get_folder_size(self.dirs)
        print(self.get_part_1_answer(folder_sizes))


if __name__ == '__main__':
    fs = FileSystem()
    data = read_file_to_list("data.txt")
    fs.main(data)





