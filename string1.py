class StringReverse:

 
    def __init__(self, text):
        self.__text = text      

    # Method to reverse the string word by word
    def reverse_words(self):
        words = self.__text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)


# Main Program
sentence = input("Enter a sentence: ")

obj = StringReverse(sentence)

print("Original String :", sentence)
print("Reversed String :", obj.reverse_words())