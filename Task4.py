# Program to check the substrings are palindromes are not and print only subpalindromes
var = input('Enter the string: ')
def Syubstring(var):
    res = []
    for val in range(len(var)):
        for i in range(val+1,len(var)+1):
            sub = ''
            for ind in range(val,i):
                sub+=var[ind]
            word = ''
            for i in range(-1,-len(sub)-1,-1):
                word +=sub[i]
            if sub == word:
                res.append(sub)
    print('\n'.join(res))
Syubstring(var)