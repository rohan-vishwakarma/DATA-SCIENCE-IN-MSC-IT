class Company:
    count = 0

    def __init__(self, name, since):
        self.name = name
        self.since = since
    
    def __repr__(self):
        self.count+=1
        return f" Company {self.name} and {self.since} {self.count}"
    


obj = Company("vigo info tech", 2016)
obj2 = Company('KD SOFTECH', 1999)
print(obj)
print(obj2)