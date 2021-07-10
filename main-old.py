import os


def main():
    directory = str(input("Enter the directory:\t"))
    print("Directory: ", directory)
    files = os.listdir(directory)
    for file in files:
        if "-" not in file:
            print("Removed ", file)
            files.remove(file)
            continue
        else:
            print("File: ", directory, file)
            new_file = directory + "\\" + file.split("-")[2]
            file = directory + "\\" + file

            print("Renaming ", file, " -> ", new_file)
            os.rename(file, new_file)



if __name__ == "__main__":
    main()
