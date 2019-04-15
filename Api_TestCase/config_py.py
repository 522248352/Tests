# coding=utf-8
import configparser


class Config_Py():

    # 操作ini配置文件方法

    def conf_read(self):

        cf = configparser.ConfigParser()
        paths = "D:\eclipse-workspace\Tests\Api_TestCase\config.ini"

        cf.read(paths)  # 读取配置文件，如果写文件的绝对路径，就可以不用os模块

        # secs = cf.sections()   # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，每个section由[]包裹，即[section])，并以列表的形式返回
        #
        # print(secs)
        #
        # options = cf.options("global_parameter")    # 获取某个section名为global_parameter所对应的键
        #
        # print(options)
        #
        # items = cf.items("global_parameter")  # 获取section名为global_parameter所对应的全部键值对
        #
        # print(items)
        #
        # host = cf.get("global_parameter", "HOSTS")   # 获取[global_parameter]中host对应的值
        #
        # print(host)

        return cf



    def value_get(self, seon, opti):

        return self.conf_read().get(seon, opti)


        # return cf.get(seon, opti)


if __name__ == '__main__':
    a = Config_Py()
    b = a.value_get(seon="database_sandbox", opti="password")
    print(b)
    print("我们的")