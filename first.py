# num= 17
# for  i in range(1,11):
#     print(num,"X",i,"=", num*i) 
# sum=0

# for i in range(1,11):
   
#     sum=sum+i 
       
# print(sum)  
numbers=[25,2,43,85,86,19]
even=0
odd=0
for num in numbers:
    if num%2==0:
        even=even+1
    else:
        odd=odd+1 
print("Count of even",even)
print("Count of odd",odd)

