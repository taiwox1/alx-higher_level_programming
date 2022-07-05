#!/usr/bin/python3
def multiple_returns(sentence):
    Y = len(sentence)
    if Y == 0:
        X = None
    else :
        X = sentence[0]
    tup = Y, X
    return (tup)
