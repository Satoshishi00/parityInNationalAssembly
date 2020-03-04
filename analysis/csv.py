import os


def lauch_analysis(data_file):
    directory = os.path.dirname(__file__)
    path_to_file = os.path.join(directory, "data", data_file)
    with open(path_to_file, 'r') as file:
        preview = file.readline()
    print("It works !\n {}".format(preview))


def main():
    lauch_analysis('current_mps.csv')


if __name__ == "__main__":
    main()
