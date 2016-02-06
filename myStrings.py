
def myString(fruit):
    
    index = len(fruit) - 1
    while index >= 0:
        letter = fruit[index]
        print letter
        index  = index - 1

myString('banana')



prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)



