from common.utils import read_file_to_list

class Dir:
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.parent = None
        self.children = None
        self.files = None
        self.dir_size = 0
        self.total_dir_size = 0

    def __repr__(self):
        return (f"dir_name: {self.dir_name}\n"
                f"parent: {self.parent}\n"
                f"children: {self.children}\n"
                f"files: {self.files}\n"
                f"dir_size: {self.dir_size}\n"
                f"total_dir_size: {self.total_dir_size}\n")

    def add_child(self, child):
        if not self.children:
            self.children = [child]
        else:
            self.children.append(child)


    def add_file(self, f_name, f_size):
        if not self.files:
            self.files = [(f_name, f_size)]
        else:
            self.files.append((f_name, f_size))

    def calculate_dir_size(self):
        for f in self.files:
            self.dir_size += int(f[1])


class Filesystem:
    def __init__(self):
        self.current_directory = None
        self.current_path = []
        self.fs_structure = {}

    def __repr__(self):
        return (f"current_directory: {self.current_directory}\n"
                f"current_path: {self.current_path}\n"
                f"current_fs_structure: {self.fs_structure}")


    def navigate_to_location(self, location):
        if location == "..":
            self.current_directory = self.current_path[-1]
            self.current_path = self.current_path[:-1]

        elif location not in self.fs_structure:
            self.fs_structure.update({location: Dir(location)})
            self.current_directory = location
            self.current_path.append(location)

            # add parent
            parent = self.current_path[-2] if len(self.current_path) > 1 else None
            self.fs_structure[location].parent = parent

    def process_object(self, command):
        if command.startswith("dir"):
            folder = command.split()[-1]
            self.fs_structure[self.current_directory].add_child(folder)
        else:
            f_size, f_name = command.split()
            self.fs_structure[self.current_directory].add_file(f_name, int(f_size))

    def process_command(self, command):
        if command.startswith("$ cd"):
            location = command.split()[-1]
            self.navigate_to_location(location)
        elif command.startswith("$ ls"):
            pass
        else:
            self.process_object(command)

    def get_total_dir_size(self):
        for i, val in self.fs_structure.items():
            if not val.children:
                files_size = sum([f[1] for f in val.files])
                self.fs_structure[self.current_directory].total_dir_size = files_size

        pass


def main():
    fs = Filesystem()
    for command in data:
        fs.process_command(command)
    fs.get_total_dir_size()
    for f in fs.fs_structure.values():
        f.calculate_dir_size()
        print(f)

if __name__ == '__main__':
    data = read_file_to_list("data_sample.txt")
    main()


# x = {"/": Dir("/"),
#      "y": Dir("y")
#      }
# print(x["/"].dir_name)
# x["/"].dir_name = "abc"
# x["/"].children =
#
# print(x["y"].dir_name)
# print(x["/"].dir_name)


