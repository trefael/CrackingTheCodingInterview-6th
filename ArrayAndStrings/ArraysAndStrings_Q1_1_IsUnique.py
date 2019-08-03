"""
1.1 Is unique:
Implement an algorithm to determine if a string has all unique charecters.
IsUnique--> Implement with additional data structures
IsUnique2--> Implement without additional data structures
Assumptions: using ASCII
"""


def IsUnique(myString):

    # Create dictionary
    Alphabet = {'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0, 'g': 0, 'f': 0, 'i': 0, 'h': 0, 'k': 0, 'j': 0, 'm': 0, 'l': 0,
                'o': 0, 'n': 0, 'q': 0, 'p': 0, 's': 0, 'r': 0, 'u': 0, 't': 0, 'w': 0, 'v': 0, 'y': 0, 'x': 0, 'z': 0}
    
    # Case string is larger then total alphabet
    if len(myString) > len(Alphabet):
        return False

    # lower all chars in string
    checkUnique= myString.lower()

    for char in checkUnique:
        Alphabet[char] += 1
        # Check if char unique
        if Alphabet[char] > 1:
            return False
    return True


# Implement without additional data structures
# Paying in run time..
def IsUnique2(myString):

    # lower all chars in string
    checkUnique = myString.lower()

    # Case string is larger then total alphabet
    if len(checkUnique) > 26:
        return False
    
    # total shows of char
    totalShows = 0

    for char in checkUnique:
        for item in checkUnique:
            if char == item:
                totalShows += 1
                if totalShows > 1:
                    return False
        totalShows=0
    return True
    

if __name__ == '__main__':
    myString = 'ADCCfdjg'
    myString2 = 'bADCfjg'
    print(IsUnique(myString2))
    print(IsUnique2(myString2))
