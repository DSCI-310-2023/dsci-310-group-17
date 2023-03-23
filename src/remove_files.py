import argparse
import os

def main(file_name):
    if (os.path.isfile(file_name)):
        os.remove(file_name)
    else:
        print("File %s not found" % file_name)
    



if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Removes files")
    parse.add_argument("file_name", help = "Path to file to delete")
    arg = parse.parse_args()
    main(arg.file_name)




