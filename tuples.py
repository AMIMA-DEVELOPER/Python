#Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple

TU = ("ben",12,"blue",[6.5,"red",4])

num = (1,1,2,2,3,3,3,3,4,4,5,6,7,7,7,8,8)
num1 = list(num)
num1.append(9)
print(num1)
num = tuple(num1)
print(num)
print(TU.count("blue"))

print(TU[0:3])

#Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.

def palind(r):
    e = len(r)-1
    s = 0

    while(s<e):
        if (r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True

r = (1,2,1)

if(palind(r)):
    print("This tuple is a flip-flop")
else:
    print("This tuple is not a flip-flop")







        
