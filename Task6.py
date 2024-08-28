# Checking the given string is palindrome or not if it is palindrome then printing palindrome
def Palindrome(string):
    for val in range(len(string)//2+1):
        if string[val]!=string[-1-val]:
            return 'Not a palindrome'
    return 'Palindrome'
string = input('enter the palindrome: ')
print(Palindrome(string))
