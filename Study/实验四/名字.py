class Name:
    def __init__(self, name):
        self.__name = name

    def set_name(self, new_name):
        if len(new_name) < 10:
            self.__name = new_name
        else:
            print("新名称长度必须小于10！")

    def get_name(self):
        return self.__name

    def __str__(self):
        return self.__name
name=Name('RinaHayashi')
print(name)
name.set_name('12345678910')
print(name)