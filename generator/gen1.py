def simple_value():
    yield 1
    yield 2

p = simple_value()


for i in simple_value():
    print(next(p))



def print_letters(string):
    for val in string:
        yield val


# A Python program to show return statement
class Test:
	def __init__(self):
		self.str = "Software Engineer"
		self.x = "Rohan vishwakarma"
	
def fun():
	return Test()



p = fun()
print(p.str)
print(p.x)
