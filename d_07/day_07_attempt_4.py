from collections import defaultdict


class Filesystem():
    def __init__(self):
        self.filesystem = defaultdict()
        self.pwd = []
        self.work_dir = ""

        self.folder_sizes = {}

    def cd(self, location):
        if location == "..":
            self.pwd.pop()
            self.work_dir = self.pwd[-1]
        else:
            if not self.filesystem.get(location):
                self.filesystem[location] = {"size": 0, "objects": []}
            self.work_dir = location
            self.pwd.append(location)

    def ls(self, objects):
        for object in objects:
            f_size, f_name = object.split()
            f_size = f_size if f_size == "dir" else int(f_size)
            self.filesystem[self.work_dir]["objects"].append((f_size, f_name))

    def generate_file_structure(self, blocks):
        for block in blocks:
            lines = block.split("\n")
            print(lines)
            if lines[0].startswith("cd"):
                location = lines[0].split()[-1]
                self.cd(location)
            elif lines[0].startswith("ls"):
                objects = lines[1:]
                self.ls(objects)
        return self.filesystem

    def get_folder_size(self, main_folder, temp_folder):
        """
        Iterate over the objects associated with the folder.
        If object is a file: - add the size of the file to the main folder
        If the object is another directory : - navigate into this directory
            and re-run the same function but with the new directory as a temp_folder argument
        Continue until all objects and subdirectories for the main_folder are exhausted.
        (after this function ends -> main function will trigger the same function for the next main_folder)

        :param main_folder: Main folder that supplied from the main function <- the one we are calculating size right now
        :param temp_folder: temporary folder that allows us to iterate
        """
        dir_objects = self.filesystem[temp_folder]["objects"]
        for f_size, f_name in dir_objects:
            if isinstance(f_size, int):  # if first part of the object is int -> it's a file
                self.filesystem[main_folder]["size"] += f_size  # add this file size to the folder size
            else:  # if it's not a file it's a directory! cd to it and repeat the process
                self.cd(f_name)
                temp_folder = self.work_dir
                self.get_folder_size(main_folder, temp_folder)



def parse_data():
    with open("data.txt", "r") as f:
        blocks = ("\n" + f.read().strip()).split("\n$ ")[1:]
        print(blocks)
    return blocks


if __name__ == '__main__':

    blocks = parse_data()
    fs = Filesystem()

    filestruct = fs.generate_file_structure(blocks)
    print(filestruct)
    for folder in filestruct.copy():
        fs.get_folder_size(folder, folder)
    print(fs.filesystem)

