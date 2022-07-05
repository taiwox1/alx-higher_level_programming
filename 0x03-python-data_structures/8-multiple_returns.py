#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) <= 0:
        return None
    Y = len(sentence)
    X = sentence[0]
    tup = Y, X
    return(tup)
