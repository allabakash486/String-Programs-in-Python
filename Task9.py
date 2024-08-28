# Reversing the sentence and without reversing the wrds in sentence
value = input('enter the string: ')
word = value.split()
result = []
def reverse_word(word):
    for val in range(-1,-len(word)-1,-1):
        result.append(word[val])
    print(' '.join(result))
reverse_word(word)       

        
