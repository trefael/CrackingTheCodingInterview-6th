"""
1.4 Palindrome Permutation:
Given a string, write a function to check if it is a permutation of a palindrome.
Assumptions:
1. Not case sensetive.
2. A permutation is a rearangment of letters.
3. A palindrome is a word or phrase that is the same backwords and forwards.
4. Strings in ASCII
5. The palindrome doesn't need to be a dictionary word
6. In order to be a permutation of a palindrome, a string  can have no more than one odd char.
"""


def IsPalindromePermutation(myString):

    countOdds = 0
    palindromeDic = {}

   # Initialize dictionary
    for char in myString:        
        char = char.lower()
        # case char is a-z letter
        if char >= 'a' and char <= 'z' :
            if char in palindromeDic.keys():
                palindromeDic[char] += 1                
            else:
                palindromeDic[char] = 1
 
    # Check if palindrome permutation
    for item in palindromeDic:
        if palindromeDic[item] % 2 != 0:
            countOdds += 1
            if countOdds > 1:
                return False
    return True


if __name__ == '__main__':
    print(IsPalindromePermutation('Tact Coa'))
    print(IsPalindromePermutation('Tacccfffff'))
