#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except (NameError,IndexError, TypeError, ValueError, ZeroDivisionError, OSError, RuntimeError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
