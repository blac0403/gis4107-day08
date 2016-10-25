def main():
    test_hasXcode()
    test_getXcodePosition()
    test_getPatternPosition()
##count function will return an integer when present. Otherwise False.
def hasXcode(inText):
    if inText.count("Tx6op3"):
        return "Yes"
    else:
        return "No"

def getXcodePosition(inText):
    if inText.count("Tx6op3"):
        return inText.find("Tx6op3") +1
    else:
        return -1

def getPatterPosition(pattern, inText):
     if inText.count(pattern):
        return inText.find(pattern) +1
     else:
        return -1

def test_hasXcode():
    print "Expect Yes. Actually: ", hasXcode("Tx6op3")
    print "Expect No. Actually: ", hasXcode("Python")
    print "Expect Yes. Actually: ", hasXcode("String Tx6op3 of nonaeronaskdnfs")
    print "Expect Yes. Actually: ", hasXcode("dsklgajjgTx6op3dsf9890")
    print "Expect No. Actually: ", hasXcode("Doesn't have code")

def test_getXcodePosition():
    print "Expect 1. Actually ", getXcodePosition("Tx6op3")
    print "Expect 8. Actually ", getXcodePosition("String Tx6op3 of nonaeronaskdnfs")
    print "Expect -1. Actually ", getXcodePosition("Python")

def test_getPatternPosition():
    print "Expect 1. Actually ",getPatterPosition("Tx6op3","Tx6op3")
    print "Expect 8. Actually ",getPatterPosition("Tx6op3","String Tx6op3 of nonaeronaskdnfs")
    print "Expect -1. Actually ",getPatterPosition("Tx6op3","Python")

if __name__ == '__main__':
    main()