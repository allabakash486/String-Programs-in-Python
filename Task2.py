# Reversing the string in Negitive indexing
String_val = input('Enter the string:')
def Revers1(String_val):
    Res = ''
    for val in String_val:
        Res =val+Res
    return Res
print(Revers1(String_val))
