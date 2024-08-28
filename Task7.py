# Reversing the string in positive indexing
String_val = input('Enter the string:')
def Revers(String_val):
    Res = ''
    for val in range(len(String_val)-1,-1,-1):
        Res +=String_val[val]
    return Res
print(Revers(String_val))
