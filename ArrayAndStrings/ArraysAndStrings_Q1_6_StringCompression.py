"""
1.6 String Compression
Implement a method to perform basic string compression using the counts of replaced chars.
i.e- aabbcccccaaa will become --> a2b1c5a3
If the new string wouldn't become smaller- method will return the original string.
Assumptions:
1. Case sensitive.
2. Strings in ASCII
3. input between a-z
"""


def StringCompression(myString):

    compressedString = ''
    charSequence = 0
    for i in range(0, len(myString)):
        # myString[i] = myString[i].lower()
        charSequence += 1
        if i+1 >= len(myString) or myString[i] != myString[i+1]:
            compressedString += myString[i] + str(charSequence)
            charSequence = 0
    if len(myString) > len(compressedString):
        return compressedString
    return myString


if __name__ == '__main__':
    print(StringCompression("aabbcccccaaa"))
    print(StringCompression("aAbBcCcCccaA"))

