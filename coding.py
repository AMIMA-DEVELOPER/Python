#f= open('CODING.TXT','r')
#print(f.read())
#f.close()


#f1= open('CODING.TXT','a')
#f1.write('  this website helps syudents to learn coding.')
#f1.close()

#f= open('CODING.TXT','r')
#print(f.read())
#f.close()

#f2= open('CODING.TXT','w')
#f2.write('My name is Amima. I study in Grade 7.')
#f2.close()

f= open('CODING.TXT','r')
counter = 0

Content = f.read()
colist = Content.split("\n")

for i in colist:
        if i:
                counter+=1
print("this is the number of lines:")
print(counter)



f.close()