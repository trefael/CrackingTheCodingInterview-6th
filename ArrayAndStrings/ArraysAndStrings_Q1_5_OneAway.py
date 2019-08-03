"""
1.5 Is One Away
Given two strings, write a function to check if they are one edit (or zero edits) away.
Allowed edits: insert char, remove char, replace char
Assumptions:
1. Not case sensitive.
2. Strings in ASCII
Examples:
'pale', 'ple' --> True
'pales', 'pale' --> True
'pale', 'bale' --> True
'pale', 'bake' --> False
"""


def checkSingleReplace(myString1, myString2):

    isIdentical = True
    for i in range(0, len(myString1)):
        if myString1[i] != myString2[i]:
            if isIdentical is False:
                return False
            isIdentical = False
    return True


def checkSingleInsert(longString, shortString):

    indexLongString = 0
    indexShortString = 0

    # case len larger than 1 - more than single insert
    if len(longString)-len(shortString) > 1:
        return False

    while indexLongString < len(longString) and indexShortString < len(shortString):
        if longString[indexLongString] != shortString[indexShortString]:
            if indexShortString != indexLongString:
                return False
            indexLongString += 1
        else:
            indexLongString += 1
            indexShortString += 1
    return True


def IsOneAway(myString1, myString2):

    myString1 = myString1.lower()
    myString2 = myString2.lower()
    lenMyString1 = len(myString1)
    lenMyString2 = len(myString2)

    # One replacement was done
    if lenMyString1 == lenMyString2:
        return checkSingleReplace(myString1, myString2)
    # One insertion was done
    elif lenMyString1 > lenMyString2:
        return checkSingleInsert(myString1, myString2)
    # One insertion was done (removal of 1 char)
    elif lenMyString2 > lenMyString1:
        return checkSingleInsert(myString2, myString1)
    return True


if __name__ == '__main__':
    # Test 1.5:
    print(IsOneAway('pale', 'ple'))     # True
    print(IsOneAway('pale', 'paleeee'))   # False
    print(IsOneAway('pales', 'pale'))   # True
    print(IsOneAway('pales', 'paale'))  # False
    print(IsOneAway('pale', 'bale'))    # True
    print(IsOneAway('pale', 'bake'))    # False
    print(IsOneAway('Tact', 'Coa'))     # False
    print(IsOneAway('Tact', 'Toctf'))   # False
