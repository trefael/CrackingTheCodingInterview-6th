'''
1.5 One Away
Given two strings, write a function to check if they are one edit (or zero edits) away.
Allowed edits: insert char, remove char, replace char
Assumptions:
1. Not case sensetive.
2. Strings in ASCII
Examples: 
'pale', 'ple' --> True
'pales', 'pale' --> True
'pale', 'bale' --> True
'pale', 'bake' --> False
'''
def IsOneAway(myString1, myString2):

    lenMyString1 = len(myString1)
    lenMyString2 = len(myString2)

    if  lenMyString1 > lenMyString2 :
        isDiff = CheckDiffOf(myString2, myString1, lenMyString2, lenMyString1)
    else: 
        isDiff = CheckDiffOf(myString1, myString2, lenMyString1, lenMyString2)
    
    return isDiff


def CheckDiffOf(shortStr, longStr, shortLen, longLen):
    diffCounter=0
    j=0  
    
    #case difrence between two string is larger then 1
    if ((longLen-shortLen > 1) and (shortLen-longLen < -1)):
        return False
        
    for i in range(0, shortLen):
        
        if diffCounter >=2 :
            return False 

        #case identical chars
        if (shortStr[i]==longStr[j]):
            j+=1
            continue      
        #case remove char
        elif (shortStr[i+1]==longStr[j] ):            
            i+=1   
        #case insert new char --> handeled in else: .....'j+=1'
        #elif (shortStr[i]==longStr[j+1] ):            
        #    j+=1  
        #case replaced char  --> handeled in else: .....'j+=1'
        #elif (shortStr[i]!=longStr[j]):
        #    j+=1  
        else:
            j+=1

        diffCounter += 1
    return True  


if __name__ == '__main__':
    #Test 1.5:
    print(IsOneAway('pale', 'ple'))   # True
    print(IsOneAway('pales', 'pale')) # True
    print(IsOneAway('pales', 'paale')) # False
    print(IsOneAway('pale', 'bale'))  # True
    print(IsOneAway('pale', 'bake'))  # False
    print(IsOneAway('Tact','Coa'))   # False

