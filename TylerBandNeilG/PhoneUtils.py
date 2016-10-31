def main():
    test_isValidPhoneNumber()
    test_phoneNumberHasLetters()

def isValidPhoneNumber(phoneNumber):
    "Is each chunk around - a number?"
    if len(phoneNumber) == 12:
        if phoneNumber[0:3].isdigit():
            if phoneNumber[4:7].isdigit():
                if phoneNumber[8:12].isdigit():
                    if phoneNumber[3] =='-':
                        if phoneNumber[7]== '-':
                            return True
    return False

##def isValidPhoneNumber(phoneNumber):
##    if len(phoneNumber) ==12:
##        if phoneNumber[0:3:7].isdigit() and phoneNumber[8:12].isdigit():
##            pass
##        if phoneNumber[3] and phoneNumber[7] =='-':
##            return True
##    return False

def test_isValidPhoneNumber():
    print "Expect isValidPhoneNumber True: is actually: ", isValidPhoneNumber("999-999-9999")
    print "Expect isValidPhoneNumber False: is actually: ", isValidPhoneNumber("g990999-9999")
    print "Expect isValidPhoneNumber False: is actually: ", isValidPhoneNumber("999-9t9-9999")
    print "Expect isValidPhoneNumber False: is actually: ", isValidPhoneNumber("999-99909he9")


def phoneNumberHasLetters(phoneNumber):
    if len(phoneNumber) == 12:
        if phoneNumber [3] and phoneNumber[7] == '-':
            pass
        if phoneNumber[0:3].isdigit():
            pass
        if (phoneNumber[4:7:12].isalpha()) == 1:
            return True
    return False

def test_phoneNumberHasLetters():
    print "Expect phoneNumberHasLetters True: is actually: ", phoneNumberHasLetters("999-A99-9999")
    print "Expect phoneNumberHasLetters False: is actually: ", phoneNumberHasLetters("999-A99-BB99")
    print "Expect phoneNumberHasLetters False: is actually: ", phoneNumberHasLetters("999-999-9999")
    print "Expect phoneNumberHasLetters False: is actually: ", phoneNumberHasLetters("9A9-999-9999")

if __name__ == '__main__':
    main()