'''class MyClass1:
    a, b = 100, 200
    def __init__(self, name):
        print(self.a * self.b)
        print('Super Class constructer executed: ', name)
class MyClass2(MyClass1):
    def __init__(self):
        super().__init__('Akshay')
        print(self.a + self.b)

sum = MyClass2()'''


class MyClass1:
    a, b = 100, 200
    def __init__(self, name):
        print(self.a * self.b)
        print('Super Class constructer executed:',name)
class MyClass2(MyClass1):
    def __init__(self):
        # super().__init__('Akshay')
        MyClass1.__init__(self, 'Sehrawat')
        print(self.a + self.b)

sum = MyClass2()