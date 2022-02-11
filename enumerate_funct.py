
'''class shubham:
    def __init__(self,x,y,z):
        self.name = x
        self.rollno = y
        self.marks = z
    def kalyani(self):
        print("Student name: {}\nRoll no: {}\nMarks: {}".format(self.name, self.rollno, self.marks))
abcd = shubham('Akshay', 78, 299)
abcd.kalyani()
s1 = shubham('Pandit', 898, 368)
s1.kalyani()'''

# class shubam:
#     a,b = 100, 200
#     def __init__(self, c,d):
#         print(self.a + self.b)
#         print(c // d)
#         print('Constructor Executed')
#     def majit(self, a, b):
#         print(self.a + self.b)
#         print(a+b)
#     def __str__(self):
#         return 'Learning Python is vey easy'
#     def __del__(self):
#         print('Object Destroyed')
# abcd = shubam(40, 8)
# abcd.majit(100,433)
# print(abcd)
# del abcd
# abcd = None
# print(abcd)

'''import time
class Test:
    def __init__(self):
        print("Object Initialization...")
    def __del__(self):
        print("Fulfil")
t1 = Test()
t1 = None
time.sleep(10)
print('end')'''

class Employee:
    def __init__(self, a,b,c):
        self.EmpNo = a
        self.Name = b
        self.Salary = c
    def employeeDetails(self):
        print("Details of employee are \nempno {} \nname {} \nsalary {}".format(self.EmpNo, self.Name,self.Salary))
talk = Employee(345, 'Akshay', 70000)
talk.employeeDetails()
Himanshu = Employee(675, 'Himanshu', 76920)
Himanshu.employeeDetails()

class Outer:
    def __init__(self):
        print('This is an outer class')
    def __str__(self):
        return 'This Language is awesome'
    class Inner:
        def __init__(self):
            print('This is an inner class')
        def m1(self):
            print("inner class method")
o = Outer()
print(o)
o.Inner()
i = o.Inner()
i.m1()
print(o)




