import os


def path():
    p = os.getcwd()
    for (root, dirs, files) in os.walk(p):
        print(root)
        print(dirs)
        print(files)


path()
