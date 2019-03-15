# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:16:49 2019

@author: Nitzan Hirshberg, Raymond Su, Ben Flaggs
@license: BSD 2-clause
"""

from CsvGen import fixed_patten, cyclic_pattern


##############################
# Generate reference results #
##############################

def ref_fixed_pattern(mode, length):
    '''Generate a reference fixed pattern.

    Parameters:
        mode (list): A list of integers defining the fixed pattern for each
            egroup.
        length (list): A list of integers defining the total length of the
            returned list for each egroup.

    Returns:
        ref_data (list): A list of dictionary. Each dictionary has the following
            form:
                {'egroup0': <2-byte int data>,
                 'egroup1': <2-byte int data>,
                 'egroup2': <2-byte int data>,
                 'egroup3': <2-byte int data>,
                 'egroup4': <2-byte int data>,
                 'egroup5': <2-byte int data>,
                 'egroup6': <2-byte int data>}
    '''
    pass
    # Need to use imported fixed_patten to implement this.
    return ref_data


def ref_cyclic_pattern(head, length, offset):
    '''Generate a reference cyclic pattern.

    Parameters:
        head (list): A list of integers defining the initial pattern for each
            egroup.
        length (list): A list of integers indicating the cycle for each egroup.

    Returns:
        ref_data (list): Same form as defined in 'ref_fixed_pattern'.
    '''
    pass
    # Need to use imported cyclic_pattern to implement this.
    return ref_data


##############################################
# Check if the parsed data match expectation #
##############################################

def check_match(ref_data, parsed_data):
    '''Check if parsed data matches reference data (expected data).

    Parameters:
        ref_data (list): Same form as defined in 'ref_fixed_pattern'.
        parsed_data (list): Same form as defined in 'ref_fixed_pattern'.

    Returns:
        stats (dict): A dict of dict that summarizes the number of match and
            mismatch, and percentage of match and mismatch for each egroup. The
            return value should have the following form:
                {'egroup0': {'num_match': int, 'num_of_mismatch': int,
                             'percent_match': float, 'percent_mismatch': float}
                 'egroup1': ...
                }
    '''


########################################
# Check if the parsed data has shifted #
########################################

def check_shift(ref_data, parsed_data):
    '''Check if parsed data is shifted compared to reference data.

    Parameters:
        ref_data (list): Same form as defined in 'ref_fixed_pattern'.
        parsed_data (list): Same form as defined in 'ref_fixed_pattern'.

    Returns:
        shifts (dict): A dict of list of the following form:
                {'egroup0': [int, int, int, ...]
                 'egroup1': ...
                }
            each int represents number of bits shifted.

            If it is not a shift, rather a mismatch, the int should be set to an
            integer that is >= 8.
    '''
    pass
    return shifts


def plot_shift(shifts):
    '''Plot the shift value for all egroups.

    Parameters:
        shifts: Same form as defined in 'check_shift'.

    Returns: None
    '''
    pass
