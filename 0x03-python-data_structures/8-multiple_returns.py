#!/usr/bin/python3
def multiple_returns(sentence):
    Y = len(sentence)
    X = sentence[0]
    if Y <= 0:
        X = None
    tup = Y, X
    return (tup)
