class Person:
    def __init__(self, name, age, identify):
        self.name = name
        self.age = age
        self.__identify = identify

    def run(self):
        print(f'{self.name} está running!')

    def __show_identify(self):
        return self.__identify

    def drinking(self, drink):
        if drink == "Beer":
            self.__show_identify()
        print(f'Drinking the {drink}')


regular = Person('Bob', '34', '89343ohio')
print(regular.name)
print(regular.drinking('Beer'))

