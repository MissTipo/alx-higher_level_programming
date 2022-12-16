#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""
# Divide and conquer
# find length of list and divide by 2
# find peak of the first part of the list and compare with the peak of the second list
# id peak1 > peak2 return peak1

def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    list_len = len(list_of_integers)
    if list_len == 1:
        return list_of_integers[0]
    elif list_len == 2:
        return max(list_of_integers)
    mid_val = int(list_len / 2)
    peak = list_of_integers[mid_val]
    if peak > list_of_integers[mid_val - 1] and peak > list_of_integers[mid_val + 1]:
        return peak
    elif peak < list_of_integers[mid_val - 1]:
        return find_peak(list_of_integers[:mid_val])
    else:
        return find_peak(list_of_integers[mid_val + 1:])

