'''class MyClass1:
    a, b = 34, 43
class MyClass2(MyClass1):
    x, y = 90, 80
    def funct(self, i, j):
        print(i + j)
        print(self.a + self.b)
        print(self.x + self.y)
sum = MyClass2()
sum.funct(78, 98)'''

'''class MyClass1:
    a, b = 34, 43
class MyClass2(MyClass1):
    a, b = 90, 80
    def funct(self, i, j):
        print(i + j)
        print(self.a + self.b)
        print(super().a + super().b)
sum = MyClass2()
sum.funct(78, 98)'''


'''a, b, abhi = 9, 5, 'amit'
class MyClass1:
    a, b = 34, 43
class MyClass2(MyClass1):
    a, b = 90, 80
    def funct(self, i, j):
        print(i + j)
        print(self.a + self.b)
        print(super().a + super().b)
        print(globals()['a'] + globals()['b'])
        print(globals()['abhi'])
sum = MyClass2()
sum.funct(78, 98)'''

class MyClass1:
    a, b = 30, 40
class MyClass2(MyClass1):
    a, b = 90, 80
    def funct(self, i, j):
        print(i + j)
        print(self.a + self.b)
        print(super().a + super().b)
class MyClass3(MyClass2):
    a, b = 4, 5
    def patil(self):
        print(self.a + self.b)
        print(MyClass2.a + MyClass2.b)
sum = MyClass2()
sum.funct(500, 200)
mek = MyClass3()
mek.patil()