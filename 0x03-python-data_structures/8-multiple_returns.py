#!/usr/bin/python3
def multiple_returns(sentence):
#    Y = len(sentence)
#    X = sentence[0]
#    tup = Y, X
#    if Y > 0:
#        return(tup)
#    else:
#        return(None)
return (len(sentence), sentence[0] if len(sentence) > 0 else None)