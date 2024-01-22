#!/usr/bin/python3
"""Creates class MyList with inheritances from 'list'. """


class MyList(list):
    """ class to hold print sorted function """
    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
