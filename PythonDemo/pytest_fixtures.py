# coding=utf-8
import pytest
import os


if __name__ == '__main__':
    print(os.path.abspath("."))
    f = open("./test.txt", "w")
    f.write("new")
    f.write("year")
    f.close()
    f2 = open("./test.txt", "r")
    print(f2.read())

    f3 = open("./test.txt", "w")
    f3.write("new")
    f3.write("year")
    f3.close()

    f4 = open("./test.txt", "r")
    print(f4.read())

