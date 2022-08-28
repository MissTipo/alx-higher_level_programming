#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if a > 0:
        word = sentence[0]
        new_tuple = [a, word]
        return new_tuple
    else:
        return(a,None)
