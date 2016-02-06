def any_lowercase1(s):
    c = ''
    for c in s:
        print c
        if c.islower():
            return 'True'
        
    return 'False'

print any_lowercase1('BANaNA')
