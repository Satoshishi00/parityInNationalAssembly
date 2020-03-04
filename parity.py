#! /usr/bin/env python3
# coding: utf-8

import csv_analysis as c_an
import xml_analysis as x_an


def main():
    c_an.lauch_analysis('current_mps.csv')
    x_an.lauch_analysis('CRSANR5L15S2017E1N001.xml')


if __name__ == "__main__":
    main()
