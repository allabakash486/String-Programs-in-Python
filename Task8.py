# Printing the revese word without reversing sentences
Value = input('Enter the string: ')
def Reverse_word(value):
    value = value.split()
    res  =[]
    for val in value:
        word =''
        for i in range(-1,-len(val)-1,-1):
            word +=val[i]
        res.append(word)
    print(' '.join(res))
Reverse_word(Value)
        
