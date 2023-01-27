import pickle

f1 =open('data.dat','rb')

while True:
    try:
        obj = pickle.load(f1)
        obj.display()
    except EOFError:
        print('all data unpickled')
        break

f1.close()