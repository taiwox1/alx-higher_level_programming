#!/urs/bin/python3
# 5-text_indentation.py

"""Difining function"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char_num = 0
    while char_num < len(text) and text[char_num] == ' ':
        char_num += 1
    while char_num < len(text):
        print(text[char_num], end="")
        if text[char_num] == "\n" or text[char_num] in ".?:":
            if text[char_num] in ".?:":
                print("\n")
            char_num += 1
            while char_num < len(text) and text[char_num] == ' ':
                char_num += 1
            continue
        char_num += 1
