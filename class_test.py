"""
class Student:
    ID="a12"
    height=166
    weight=100
    ch_score=60
    math_score=60
    bmi=0.1
    def score():
        print("score")
    def BMI(bmi):
        print(bmi)

print(Student.math_score)
Student.score()
Student.bmi=Student.weight/((Student.height/100)**2)
Student.BMI(Student.bmi)
"""
# import math
# class Point:
#       def __init__(self,x,y):
#             self.x = x
#             self.y = y
# # 建立第一個實體物件
# p1 = Point(3,4)
# print(p1.x,p1.y)  # 3 4
# # 建立第二個實體物件
# p2 = Point(0,0)
# print(p2.x,p2.y)  # 5 6
# print((abs(p2.x-p1.x)**2+abs(p2.y-p1.y)**2)**0.5)

# class Student:
#     def __init__(self,ch_score,math_score,height,weight):
#         self.ch_score=ch_score
#         self.math_score=math_score
#         self.height=height
#         self.weight=weight
#     def __str__(self):
#         return f"i am {self.height}cm"
#     def score(self):
#         return((self.math_score+self.ch_score)/2)
#     def BMI(self):
#         return((self.weight/((self.height/100)**2)))
# s1=Student(70,60,170,100)
# print(s1.score())
# print(s1.BMI())
# s2=Student(80,60,160,80)
# print(s2.score())
# print(s2.BMI())
# print(s1)

# class file:
#       # 初始化函式
#       def __init__(self,name):
#             self.name = name
#             self.file = None # 尚未開啟檔案：初期是None 代表空的意思
#       # 實體方法
#       def open(self):
#             self.file =open(self.name,mode="r",encoding="utf-8")
#       def read(self):
#             return self.file.read()
# # 讀取第一個檔案
# f1 = file("data1.txt")
# f1.open()
# data = f1.read()
# print(data)  

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def print_name(self):
        print(self.name)
    def print_age(self):
        print(self.age)
class Student(Person):
    def __init__(self,name,age,school):
        self.name = name
        self.age=age
        self.school=school

    def print_school(self):
        print(self.school)
class Doctor(Person):
    def __init__(self,name,age,hostpital):
        self.name = name
        self.age=age
        self.hostpital=hostpital

    def print_hostpital(self):
        print(self.hostpital)
doctor1=Doctor("john",20,"NUU")
doctor1.print_name()
doctor1.print_age()
doctor1.print_hostpital()