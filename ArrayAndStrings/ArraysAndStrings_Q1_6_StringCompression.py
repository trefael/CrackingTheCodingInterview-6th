'''
1.6 String Compression
Implement a method to perform basic string compression using the counts of replaced chars.
i.e- aabbcccccaaa will become --> a2b1c5a3
If the new string wouldn't become smaller- method will return the original string.
Assumptions:
1. Not case sensetive.
2. Strings in ASCII
3. input between a-z
'''

def StringCompression(myString1):

    mydic = {}

    for k in range(myString1):
        {
          mydic[k] = y
        }



    return x

if __name__ == '__main__':
    #Test 1.5:
    print(IsOneAway('pale', 'ple'))   # True
    print(IsOneAway('pales', 'pale')) # True
    print(IsOneAway('pales', 'paale')) # False
    print(IsOneAway('pale', 'bale'))  # True
    print(IsOneAway('pale', 'bake'))  # False
    print(IsOneAway('Tact','Coa'))   # False