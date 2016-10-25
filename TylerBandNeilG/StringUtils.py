def main():
    test_getInitials()

def getInitials(fullName):
    initials = ''
    names = fullName.split()
    for letter in names:
        initials += '.'.join(letter[0]) + '.'
    return initials
##    initials = fullName.split()
##    for letter in initials:
##        print (letter[0] + '.'),

def test_getInitials():
    print "John Samuel Woobly. Expect J.S.W. Actually: " , getInitials("John Samuel Wobbly")
    print "Dylan McDermott. Expect D.M. Actually: ", getInitials("Dylan McDermott")
    print "Nora Young. Expect: N.Y. Actually: ", getInitials("Nora Young")

if __name__ == '__main__':
    main()
