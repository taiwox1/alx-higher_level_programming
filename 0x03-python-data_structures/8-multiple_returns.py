#!/usr/bin/python3
def multiple_returns(sentence):
    Y = len(sentence)
    X = sentence[0]
    tup = Y, X
    if sentence == (None):
        return(None)
    else:
        return (tup)
