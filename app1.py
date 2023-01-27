import student
import pickle
f = open('data.dat','wb')
n = int(input('enter the employees'))
for i in range(n):
    name = input('enter the name')
    roll = int(input('enter the roll'))
    marks = float(input('enter marks'))
    obj = student.student(name,roll,marks)
    pickle.load(obj,f)

print('object stored success')