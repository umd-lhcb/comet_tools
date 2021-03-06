#!/usr/bin/env python3
'''
@author: Jorge Ramirez
@license: BSD 2-clause
'''

import csv
import sys


class GbtxMemParser(object):
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        '''Parse the supplied filename and return a list of dictionary.

        Parameters: None

        Returns:
            parsed_data (list): A list of dictionary. Each dictionary has the
                following form:
                    {'elink0': <1-byte int>,
                     'elink1': <1-byte int>,
                     'elink2': <1-byte int>,
                     'elink3': <1-byte int>,
                     'elink4': <1-byte int>,
                     'elink5': <1-byte int>,
                     'elink6': <1-byte int>,
                     'elink7': <1-byte int>,
                     'elink8': <1-byte int>,
                     'elink9': <1-byte int>,
                     'elink10': <1-byte int>,
                     'elink11': <1-byte int>}
                Note that the header is removed from the final result.
        '''
        parsed_data = []

        with open(self.filename) as f:  # open txt file
            for line in f:
                parsed_data.append(self.dissect_str_to_dict(line.strip()))

        return parsed_data

    @classmethod
    def dissect_str_to_dict(cls, raw_line):
        '''Take a list of string, dissecting them to list of dictionary.

        Parameters:
            raw_line (str): A single line in the input data file

        Returns:
            parsed_line (dict): Same form as defined in 'parse' method.
                This is the normal output of the parser.
        '''
        elink_idx_map = cls.elink_channel_idx_mapping()
        parsed_line = {}

        for elink, idx in elink_idx_map.items():
            idx = len(raw_line) - idx
            parsed_line[elink] = int(raw_line[idx-2:idx], 16)

        return parsed_line

    @staticmethod
    def elink_channel_idx_mapping():
        '''Define the mapping between elink channel name to its byte index in
        the GBTx frame.

        Counting from right: idx 0 -> rightmost. Each index indicates the right
        boundary of the elink. Also assume the width of each elink is 2.
        '''
        return {
            'elink0': 0,
            'elink1': 2,
            'elink2': 4,
            'elink3': 6,
            'elink4': 8,
            'elink5': 10,
            'elink6': 12,
            'elink7': 14,
            'elink8': 16,
            'elink9': 18,
            'elink10': 20,
            'elink11': 22
        }

    def output_to_csv(self, filename="gen/parsed_elinks.csv"):
        '''Write parsed memory data to a CSV file.

        Parameters:
            self (object): Default class variable.
            filename (str): Output CSV filename, full path or relative path.

        Returns: None
        '''
        parsed_data = self.parse()
        csv_headers = list(parsed_data[0].keys())  # get keys for csv headers

        with open(filename, 'w', newline='') as csvfile:  # open csv file
            # use csv.DictWriter to convert Dict to CSV
            writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
            writer.writeheader()  # write headers

            for elink_dict in parsed_data:   # work on a dict by dict basis
                writer.writerow(elink_dict)  # write each dict onto a single row


if __name__ == '__main__':
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    parser = GbtxMemParser(input_filename)
    parser.output_to_csv(output_filename)
