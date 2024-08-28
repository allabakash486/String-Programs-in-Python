# Reversing the string in Negitive indexing
String_val = input('Enter the string:')
def Revers1(String_val):
    Res = ''
    for val in range(-1,-(len(String_val)+1),-1):
        Res +=String_val[val]
    return Res
print(Revers1(String_val))
