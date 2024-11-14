class Calculator:
    def calculate(self, op, num1, num2):
        if op == '+':
           return self.__add(num1, num2)
        elif op == '-':
           return self.__sub(num1, num2)
        else:
            print('Operation Error')

    def __add(self, num1, num2):
        return num1 + num2

    def __sub(self, num1, num2):
        return num1 - num2


result = Calculator()

print(result.calculate('-', 3, 5))


