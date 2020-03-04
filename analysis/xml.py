import os
import logging as lg

lg.basicConfig(level=lg.DEBUG)


def lauch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "data/compteRendu", data_file)

    try:
        with open(path_to_file, 'r') as file:
            preview = file.readline()
            lg.debug("It works !\n {}".format(preview))
    except FileNotFoundError as e:
        lg.critical("File note found :( : {}".format(e))


def main():
    lauch_analysis('CRSANR5L15S2017E1N001.xml')


if __name__ == "__main__":
    main()
