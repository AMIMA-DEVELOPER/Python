#Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]

s1 = {1,2,2,2,3,4,5,5,6}
s2 = {"red",1.34,6,7,7,"blue",(1,2,3)}

s3 = {1, 2, 3, 4, 3, 2}
s4 = set([1, 2, 3, 2])

s5 = set([0, 1, 3, 4, 5])
print("original set",s5)

s5.pop()
print("after removing",s5)

#Write a program to find the intersection of two sets. Set1 = {green, blue} Set2 = {blue, yellow}

s1 = {"blue","green"}
s2 = {"yellow", "blue"}

s3 = s1.intersection(s2)
print(s3)

#union

s4= s1.union(s2)
print(s4)

#3. Write a program to create an array with the following elements - [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array. Also, print the reversed array.

# ARRAY

import array as arr

array_num = arr.array('i',[1,2,3,4,5,6,7])

print("original array"+str(array_num))

print("Number of occurences of 3 in the said array " +str(array_num.count(3)))

# reverse array

array_num.reverse()
print("The reverse array : ")
print(str(array_num))