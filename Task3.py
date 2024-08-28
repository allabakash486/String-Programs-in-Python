string = input('Enter the string: ')
def subprinting(string):
    for val in range(len(string)):
        word = ''
        for i in range(val+1,len(string)+1):
            print(string[val:i])
subprinting(string)
