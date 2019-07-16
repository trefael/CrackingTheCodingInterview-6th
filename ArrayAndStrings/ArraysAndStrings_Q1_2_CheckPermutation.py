'''
1.2 Check Permutation:
Given two strings, write a method to decide if one is a permutation of the other
Assumptions:
1. Ignoring white spaces
2. Not case sensetive.
3. Strings could be in diffrent length
4. Strings in ASCII
'''
def IsPermutation(myString1, myString2):

    #Check which string is the longest. Only the shorter one can have permutations in the longer one.
    string1Len = len(myString1)
    string2Len = len(myString2)
    if string1Len > string2Len :
        return CheckPermutation(string1Len, string2Len, myString1, myString2)
    else:
        return CheckPermutation(string2Len, string1Len, myString2, myString1)


def CheckPermutation(longerLen, shorterLen, longerStr, shorterStr):
   #Create dictionary
    AlphabetShorterStr = {'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0, 'g': 0, 'f': 0, 'i': 0, 'h': 0, 'k': 0, 'j': 0, 'm': 0, 'l': 0, 'o': 0, 'n': 0, 'q': 0, 'p': 0, 's': 0, 'r': 0, 'u': 0, 't': 0, 'w': 0, 'v': 0,
     'y': 0, 'x': 0, 'z': 0}
    AlphabetLongerStr = {'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0, 'g': 0, 'f': 0, 'i': 0, 'h': 0, 'k': 0, 'j': 0, 'm': 0, 'l': 0, 'o': 0, 'n': 0, 'q': 0, 'p': 0, 's': 0, 'r': 0, 'u': 0, 't': 0, 'w': 0, 'v': 0,
     'y': 0, 'x': 0, 'z': 0}

    #Init dictionary with str contant
    AddToDic(shorterStr, AlphabetShorterStr)
    AddToDic(longerStr, AlphabetLongerStr)
 
    for item in longerStr:
        if AlphabetLongerStr[item] != AlphabetShorterStr[item]:
            return False
    return True

#Init dictionary with str contant
def AddToDic(myString, dict):
    #lower all chars in string
    myString= myString.lower()

    for char in myString:
        dict[char] += 1

if __name__ == '__main__':
    print(IsPermutation('zebra','arbezx'))
    print(IsPermutation('gjtrswaxbjgt','jkhul'))
    print(IsPermutation('zebra','arbez'))
    print(IsPermutation('ac','arbez'))