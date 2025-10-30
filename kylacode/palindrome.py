def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

    
def reverse(s):
    result = ''
    for c in s:
        result = c + result
        print(c) 
        print(result)
    return result 
word = input('word? ') 

reverse(word)

# if word == word[::-1]: 
if word == reverse(word):
    
    print('yes')
else: 
    print('no')

