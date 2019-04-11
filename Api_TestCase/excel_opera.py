# coding=utf-8
import xlrd
import os
print(os.path.abspath("."))
excle_file = xlrd.open_workbook("./test.xls")

# 获取sheet数量
print(excle_file.nsheets)

# 获取sheet列表
print(excle_file.sheets())

# 获取每个sheet列表的名字
print(excle_file.sheet_names())

# 获取sheet名是Sheet1的名字
print(excle_file.sheet_by_name("Sheet1"))

# 获取Sheet1的列数和行数
print(excle_file.sheet_by_name("Sheet1").ncols)
print(excle_file.sheet_by_name("Sheet1").nrows)

# 获取Sheet1的第一行/列的值，包含每列值得类型
print(excle_file.sheet_by_name("Sheet1").row(0))
print(excle_file.sheet_by_name("Sheet1").col(0))


# 获取Sheet1的第一行/列的值，不包含类型
print(excle_file.sheet_by_name("Sheet1").row_values(1))
print(excle_file.sheet_by_name("Sheet1").col_values(0))

# 获取Sheet1的索引 0行0列的值，包含类型
print(excle_file.sheet_by_name("Sheet1").cell(0,0))
# print(excle_file.sheet_by_name("Sheet1").cell(0,0).value)
print(excle_file.sheet_by_name("Sheet1").cell(1,1))
print(excle_file.sheet_by_name("Sheet1").cell(3,0))
