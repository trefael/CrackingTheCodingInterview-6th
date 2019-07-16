'''
1.3 URLify
Write a method to replace all white spaces in a string with '%20'.
Assumptions:
1. String has sufficient space to hold the additional characters
2. You are given the "true" string's length.
'''
def URLify(myString):
    
    replacedString=''
    for char in myString:
        if char==' ':
            char='%20'
        replacedString+=char
    return replacedString

if __name__ == '__main__':
    #Test 1.3:
    print(URLify("Hello world!"))
    print(URLify("Mr John Smith"))
