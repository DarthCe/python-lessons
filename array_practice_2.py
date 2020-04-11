import time
from random import randint

print("Let's practice arrays with a random grid of 1s and 0s!\n")
time.sleep(1.5)


#build 10x10 array
for i in range(10):
    listRow = [randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1)]
    print(listRow)

#add 5 to every odd column and every even row
time.sleep(2)
print("\nOK that was easy...let's switch it up and add 5 to every odd column in every even row!\n")
time.sleep(3)

#build 10x10 array
for i in range(10):
    #even rows
    if i % 2 == 0:
        listRow = [randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1)]
        print(listRow)
    #odd rows
    elif i % 2 == 1:
        listRow = [(randint(0,1)+5),randint(0,1),(randint(0,1)+5),randint(0,1),(randint(0,1)+5),randint(0,1),(randint(0,1)+5),randint(0,1),(randint(0,1)+5),randint(0,1)]
        print(listRow)
