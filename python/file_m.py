def gener(array):
    for i in array:
        yield i

a = [12,34,56,77]

p = gener(a)
print(p)