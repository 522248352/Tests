import configparser

class Config_Py():

    def conf_read(self):
        cf = configparser.ConfigParser()
        paths = "D:\eclipse-workspace\Tests\Api_TestCase\config.ini"
        cf.read(paths)
        return cf


    def value_get(self, seon, opti):

        return self.conf_read().get(seon, opti)


        # return cf.get(seon, opti)


if __name__ == '__main__':
    a = Config_Py()
    b = a.value_get(seon="database_sandbox", opti="password")
    print(b)