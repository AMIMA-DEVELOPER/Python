#Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary

# s1 = {1,2,3}
# s2 = {'x','y','z'}
# s3 = list(zip(s1,s2))

# print(s3,"/n")

# list1 = [10,20,30,40]
# list2 = [100,200,300,400]

# for x ,y in zip(list1, list2[::-1]):
    #print(x,y)

#stocks = ['reliance','infosys','tcs']
#prices = [2175 , 1127, 2750]

#new_dict = {stocks: prices for stocks,
#            price in zip(stocks,prices)}

#print('/n{}'.format(new_dict))

#Write a program where the value of i begins from 1 and goes to 10. When the value of i becomes 5, force the interpreter to exit the program.

#for i in range(10):
    #if i == 5:
        #print(exit)
        #exit()
    #print(i)


#Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.

s1 = [1,2,3]
s2 = [4,5,6]

result =  map(lambda x,y: x +y , s1,s2)
print("Addition of two list")
print(list(result))

#using map

num = [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq, num))

print("square of nmbers")
print(square)




