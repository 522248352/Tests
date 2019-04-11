# coding=utf-8
import csv

csv_file = csv.reader(open("D:\eclipse-workspace\Tests\Api_TestCase\csv.csv", "r"))
# csv_file_dic = csv.DictReader(fieldnames="D:\csv.csv")

with open("D:\eclipse-workspace\Tests\Api_TestCase\csv.csv", "r") as filename:
    csv_re = csv.DictReader(filename)
    for row in csv_re:
        print(row)
        print(type(row))

