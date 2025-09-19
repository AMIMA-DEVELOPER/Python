# with open('Coding12.TXT','w') as Fl:
#     Fl.write("My name is Amima.")
#     Fl.write("\nI am 12 year old.")
# Fl.close()
#     #spliting contents

# with open('Coding12.TXT','r') as Fl:
#     Data = Fl.readlines()
#     print("Words in this file are.......")
#     for line in Data:
 #       word= line.split()
#        print(word)
#Fl.close()        

# import os
# print("check if CODING.TXT exists or not....")
# if os.path.exists("CODING.TXT"):
#     os.remove("CODING.TXT")
# else:
#     print("The file doesnot exists.")

# import os
# os.remove("New file.TXT")

import os 
os.rename("Coding12.TXT","NEW.TXT")