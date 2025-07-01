TU= ("Jill",77.8,"failed","Grade 9")
print("The student",TU[0], "has",TU[2])
list2= list(TU)
print(list2)
list2[1] = 99
list2[2] = "passed"
TU = tuple(list2)
print ("The student",TU[0],"has",TU[2])

print ("The student",TU[0],"is in",TU[3], "and has", TU[2])


