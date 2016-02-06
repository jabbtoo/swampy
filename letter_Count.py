from sys import exit

def letter_count(letter, str):
    count = 0
    for c in str:
        if c == letter:
            count += 1
    print count

while True:
    print "Enter character or quit to exit:"
    letter = raw_input('-->')
    if letter == 'quit':
        exit()
    print letter  
    print "Enter string"
    str = raw_input('-->')

    letter_count(letter, str)
    

