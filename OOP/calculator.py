class Calculate:
    
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def subtract(self):
        return f"the result of {self.num1} and {self.num2} is {self.num1 - self.num2}"
    

calcu = Calculate(12,34)
pr = calcu.subtract()
print(pr)