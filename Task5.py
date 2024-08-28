#Printing only substrings also subpalindromes 
string = input('Enter the string: ')
def subprinting(string):
    for val in range(len(string)):
        for i in range(val+1,len(string)+1):
           if string[val:i] == string[val:i][::-1]:
               print(string[val:i])
subprinting(string)
