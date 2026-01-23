#First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest

student_data = {'id1':
     {'name': ['sara'],
     'class' : ['v'],
     'subject': ['english,math,science']
     },
                 
    
    'id2':
     {'name': ['David'],
     'class' : ['v'],
     'subject': ['english,math,science']
     },

    'id3':
     {'name': ['Surya'],
     'class' : ['v'],
     'subject': ['english,math,science']
     },

    'id4':
     {'name': ['sara'],
     'class' : ['v'],
     'subject': ['english,math,science']
     },
                }

result = {}

for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)


#Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.

country_codes = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}

print("Country code for India:")
print(country_codes.get('India','not found'))

print("Country code for China:")
print(country_codes.get('China','not found'))
