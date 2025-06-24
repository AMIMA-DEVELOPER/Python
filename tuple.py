#create an empty tupple
T=(1,3,5,7,9)
print(T)

TU= ("jack",5,"grade 5",20.8,"failed",)
print("The student has",TU[4])
list1= list(TU)
print(list1)
list1[4] = "passed"
TU = tuple(list1)
print("The student has",TU[4])

RU= ("Bye",)
