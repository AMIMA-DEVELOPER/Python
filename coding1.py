#f= open('CODING.TXT',"a")
#f.write("\nI am 13 years old")
#f.close()

f= open('CODING.TXT','r')
print("Looping through the lines....")
for line in f:
    print(line)
f.close()