#coding=utf-8
import json
import requests

def test_demo_1(a,*b):

    print(a)
    print(b)

def test_demo_2(a,b,c=12,*d,**e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

def test_json_dumps():
    dis = {"data1":1,"data2":2}

    str_json = json.dumps(dis)
    print(type(str_json))
    print(str_json)


def test_json_load():

    sfr = """{"data3":1,"data4":2}"""
    # sfr = 'python'

    # try
    # except
    # else  只有try块没有引发异常，才执行else子句
    # finally  不论是否有异常，都执行
    #

    try:
        dis = json.loads(sfr)
    except Exception as e:
        print(e)
    else:
        print("-----------------------------try块没异常，才执行else语句-------------------")
    finally:
        print("-----------finally-----------")


    print(type(dis))
    print(dis)

class Bird(object):
    def __init__(self):
        self.name = 0
        self.age = 0
    def setName(self, name):
            self.name = name
    def getName(self):
        return self.name

    def setAge(self, age):
            self.age = age
    def getAge(self):
        return self.age

if __name__ == '__main__':
    test_demo_1(1,1,2,3)
    test_demo_1([1,2],[3,4],{1:2,2:3})

    test_demo_2(1,2)
    print("------------------------————————————————————————————")
    b = Bird()
    b.setName("xiaohua")
    b.setAge("10")
    print(b.getAge()+b.getName())
