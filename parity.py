#! /usr/bin/env python3
# coding: utf-8
import argparse

import analysis.csv as c_an
import analysis.xml as x_an


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e", "--extension", help="""Type of file to analyse. Is it a CSV of an XML?""")
    return parser.parse_args()


def main():
    args = parse_arguments()
    if args.extension == 'csv':
        c_an.lauch_analysis('current_mps.csv')
    elif args.extension == 'xml':
        x_an.lauch_analysis('CRSANR5L15S2017E1N001.xml')


if __name__ == "__main__":
    main()
