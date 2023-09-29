#!/usr/bin/python3
""" finds peak """

def search(lo, h, ints):
    """
    search for the peak of integers.
    """

    mid = (lo + h) // 2
    if lo == h:
        return ints[h]
    if ints[mid] < ints[mid + 1]:
        return(search(mid + 1, h, ints))
    return(search(lo, mid, ints))


def find_peak(list_of_integers):
    """
    find the peak of the integers
    using the search option above.
    """

    if not list_of_integers:
        return
    return(search(0, len(list_of_integers) - 1, list_of_integers))

