#!/usr/bin/python3
def multiple_returns(sentence):
    Y = len(sentence)
    X = sentence[0]
    tup = Y, X
    if len(sentence) <= 0:
        return(None)
    else:
        return (tup)
