import os


def lauch_analysis(data_file):
    directory = os.path.dirname(__file__)
    path_to_file = os.path.join(directory, "data/compteRendu", data_file)
    with open(path_to_file, 'r') as file:
        preview = file.readline()
    print("It works !\n {}".format(preview))


def main():
    lauch_analysis('CRSANR5L15S2017E1N001.xml')


if __name__ == "__main__":
    main()
