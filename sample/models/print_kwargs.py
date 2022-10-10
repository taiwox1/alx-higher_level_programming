
def print_values(**kwargs):
    mydic = []
    for key, value in kwargs.items():
        mydic.append(value)
    print(mydic)
    return(kwargs)
