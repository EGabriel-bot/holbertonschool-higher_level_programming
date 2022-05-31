#!/usr/bin/python3
"""My list"""


class MyList(list):
    """Class MyList"""

    def print_sorted(self):
        new = self.copy()
        new.sort()
        print(new)
