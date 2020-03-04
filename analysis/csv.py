import os
import logging as lg

lg.basicConfig(level=lg.DEBUG)


def lauch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "data", data_file)

    try:
        with open(path_to_file, 'r') as file:
            preview = file.readline()
            lg.debug("It works !\n {}".format(preview))
    except FileNotFoundError as e:
        lg.critical('File not found !!! : {}'.format(e))


def main():
    lauch_analysis('current_mps.csv')


if __name__ == "__main__":
    main()
