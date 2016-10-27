#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Neil
#
# Created:     25-10-2016
# Copyright:   (c) Neil 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##def hasXcode(inText):
##    if inText.count("Tx6op3"):
##        return True
##    else:
##        return False
##
##def test_hasXcode():
##    print hasXcode("Tx6op3")
##    print hasXcode("ccTx6op311aegaegasega")
##    print hasXcode("111gsaegasegasss")
##
###test_hasXcode()
##
##def getXcodePosition(inText):
##    if inText.count("Tx6op3"):
##        return inText.find("Tx6op3") +1
##    else:
##        return -1
##
##def test_getXcodePosition():
##    print getXcodePosition("ccTx6op311aegaegasega")
##    print getXcodePosition("aaaa")
##
###test_getXcodePosition()
##
##def getPatternPosition(pattern, inText):
##    if inText.count(pattern):
##        return inText.find(pattern) +1
##    else:
##        return -1
##
##def test_getPatternPosition():
##    print getPatternPosition("Tx6op3", "Tx6op3")
##    print getPatternPosition("aaa", "aaabbbccc")
##    print getPatternPosition("eee", "Tx6op3")
##    print getPatternPosition("eee", "asasebasgassgeee")
##
###test_getPatternPosition()
##
##
def getInitials(fullName):
##    name = fullName.split()
##    for letter in name:
##        print (letter[0] + "."),
##    print('')

    name = fullName.split()
    initials = ''
    for letter in name:
        initials += ''.join(letter[0]) + '.'
    return initials


def test_getInitials():
    print getInitials("John Samuel Wobbly")
    print getInitials("Dylan Mcdermott")
    print getInitials("Nora Young")

#test_getInitials()

def isValidPhoneNumber(phoneNumber):
##    "Is each chunk around - a number?"
##    if len(phoneNumber) == 12:
##        if phoneNumber[0:3].isdigit():
##            if phoneNumber[4:7].isdigit():
##                if phoneNumber[8:12].isdigit():
##                    if phoneNumber[3] =='-':
##                        if phoneNumber[7]== '-':
##                            return True
##
##    return False


    if len(phoneNumber) ==12:
        if phoneNumber[0:3:7].isdigit() and phoneNumber[8:12].isdigit():
            pass
        if phoneNumber[3] and phoneNumber[7] =='-':
            return True
    return False


def test_isValidPhoneNumber():
    print isValidPhoneNumber("999-999-9999")

test_isValidPhoneNumber()
