# Description: This file demonstrates the use of Union in Python.
#   Union is used to specify the type of the input parameter.
#   In this example, the input parameter can be either a string, int, or float.

# Reference: careful to use Union
# https://qiita.com/sergicalsix/items/6480902f0f0e0d5bf782

from typing import Union


def PrintChar(txt: Union[str, int, float]) -> None:
    if isinstance(txt, int):
        print("Converted int to string")
        txt = str(txt)
    elif isinstance(txt, float):
        print("Converted float to string")
        txt = str(txt)
    for character in txt:
        print(character, end="\n")

    return txt


if __name__ == "__main__":
    txt = ""
    PrintChar(341)
    print("\n")
    PrintChar("Hello")
    print("\n")
    PrintChar(3.14)

    print(txt)
    print(type(txt))
