class Calculate:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def subtract(self):
        return f"the result of {self.num1} and {self.num2} is {self.num1 - self.num2}"

class Sub(Calculate):

    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def add(self):
        return f"the result of {self.num1} and {self.num2} is {self.num1 + self.num2}"

class Calci(Sub):

    def __init__(self, num1, num2):
        super().__init__(num1, num2)


obj = Calci(12,14)
pr1 = obj.add()

obj1 = Calci(49,4)
pr2 = obj1.subtract()

print(pr1)
print(pr2)

