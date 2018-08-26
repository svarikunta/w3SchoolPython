class Person:
    x=5

p1=Person()
print(p1.x)

class MyClass:
    """docstring for myClass."""
    def __init__(self, name,age):
        self.name = name
        self.age=age

m1=MyClass("name1",11)
m2=MyClass("name2",12)


class MyClass2:
    def __init__(self,name,age):
        self.name=name
        self.age=age

m3=MyClass2("name3",13)
m4=MyClass2("name4",14)




print(m1.age)
print(m1.name)

print(m2.age)
print(m2.name)

print(m3.age)
print(m3.name)

print(m4.age)
print(m4.name)
