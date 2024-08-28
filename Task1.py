# Printing substring of the given  string 
var = input('Enter the string: ')
def Syubstring(var):
    res = []
    for val in range(len(var)):
        sub = ''
        for ind in range(val+1):
            sub+=var[ind]
        res.append(sub)
    print('\n'.join(res))
Syubstring(var)
