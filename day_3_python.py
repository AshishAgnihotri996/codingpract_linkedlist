import sys

# index 2 types - > positive and negative
#
# immutabe - > int, float, string, tuple
#
# 2024352345 ->block address

#----------------------------- oops------------------------------

#constructor
# 1. non para 2. para 3 default constr
# # self- it contains the self variable of the current object
# 1.memoray allocation for object
# 2. memory reference returned to the object
# 3. memory reference automatically passed inside constructor
# 4. construct creates variable ar that memory reference

# class Solution:
#     def __init__(self,sal,age):
#         self.salary = sal
#         self.age = age
#
#     def display(self):
#         print(f'the salary is {self.salary} and the age  is {self.age} ')
#
# e1 = Solution(27000,23)
# e2 = Solution(28000,22)
# print(e1.__dict__)
# print(e2.display())

#built in class modules

# class Solution:
#     ''' this is class statement and thus its a empty class'''
#
# e1 = Solution()
# e2 = Solution()
#
# print(e1.__class__)
# print(e1.__doc__)
# print(e1.__module__)
#
# # isinstance() to check wheater this object belongs to this class or not
# print(isinstance(e1,Solution))

# c-2
#instance varaible and instance method

# class Solution:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#
#     def display(self):
#         print(f'the name is {self.name} and his marks is {self.marks}')
#
#     def change_data(self):
#         self.name = input('enter the name')
#         self.marks = input('enter the marks')
#
# e1 = Solution('ashish',99)
# e2 = Solution('manav',99)
#
# e1.change_data()
# print(e1.__dict__)

#chaging the value outside the class