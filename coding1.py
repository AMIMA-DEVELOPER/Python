#f= open('CODING.TXT',"a")
#f.write("\nI am 13 years old")
#f.close()


#Write a Python program to remove lines of a file starting with prefix - Coding and store the contents in a new file.


f= open('CODING.TXT','r')
f1= open('Coding12.TXT','w')

for lines in f.readlines():
    if not (lines.startswith("I am")):
        print(lines)
        f1.write(lines)

f1.close()
f.close()