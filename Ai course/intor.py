print("Hello I am AI, What is ur name??")

name = input()

print("Nice to meet u",name)
print("How are you feeling??, (good/sad)")

mood = input().lower()

if mood == "good" :
    print("I AM GLAD TO HEAR THAT")
elif mood == "bad":
    print("I am sorry to hear that, hope things get better soon ;)")
else:
    print("I see it's hard for you")

print("Bye, It was nice chatting with you",name,"Bye")

