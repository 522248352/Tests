# coding=utf-8
import csv

csv_file = csv.reader(open("D:\csv.csv", "r"))
# csv_file_dic = csv.DictReader(fieldnames="D:\csv.csv")

with open("D:\csv.csv", "r") as filename:
    csv_re = csv.DictReader(filename)
    for row in csv_re:
        print(row)
        data ={}
        data["a"] =row["T1"]
        data["b"] =row["T2"]
        data["c"] =row["T3"]
        print(data)
