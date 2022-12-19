import pprint
from collections import defaultdict

class Filesystem:
    def __init__(self):
        self.filestruct = {"/": {"size": 0, "objects": [(14848514, "b.txt"), (8504156, "c.dat"), ("dir", "a"), ("dir", "d")]},
            "a": {"size": 0, "objects": [("dir","e"), (29116, "f"), (2557, "g"), (62596, "h.lst")]},
            "e": {"size": 0, "objects": [(584, "i")]},
            "d": {"size": 0, "objects": [(4060174, "j"),
                                         (8033020, "d.log"),
                                         (5626152, "d.ext"),
                                         (7214296, "k")]}}

        self.pwd = []
        self.working_dir = ""

    def cd(self, location):
        if location == "..":
            self.pwd.pop()
            self.working_dir = self.pwd[-1]
        else:
            self.working_dir = location
            self.pwd.append(location)

    def ls(self, objects):
        for object in objects:
            f_size, f_name = object.split()
            self.filestruct[self.working_dir]["objects"].append((f_size, f_name))


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
        dir_objects = self.filestruct[temp_folder]["objects"]  # all files in specified dir subfolders are also files
        for f_size, f_name in dir_objects:
            if isinstance(f_size, int):  # if filrst part of the object is int -> it's a file
                self.filestruct[main_folder]["size"] += f_size  # add this file size to the folder size
            else:  # if it's not a file it's a directory! cd to it and repeat the process
                self.cd(f_name)
                temp_folder = self.working_dir
                self.get_folder_size(main_folder, temp_folder)


def main(fs):
    for folder in fs.filestruct:
        fs.pwd.append(folder)
        fs.working_dir = folder
        temp_folder = folder
        fs.get_folder_size(folder, temp_folder)

    folders_under_100k = 0
    for folder_name, folder_stat in fs.filestruct.items():
        folder_size = folder_stat["size"]
        folders_under_100k += folder_size if folder_size < 100_000 else 0

    print(folders_under_100k)

    print(fs.filestruct)


if __name__ == '__main__':
    fs = Filesystem()
    main(fs)


