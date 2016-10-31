def main():
    test_getEW()
    test_getNS()

def getEW(dmsRecord):
    return dmsRecord[10].upper()

def test_getEW():
    print "Expect: W Actually: ", getEW("DDD MM SS W DD MM SS N")
    print "Expect: W Actually: ", getEW("DDD MM SS w DD MM SS N")

def getNS(dmsRecord):
    return dmsRecord[21].upper()

def test_getNS():
    print "Expect: N Actually: ", getNS("DDD MM SS W DD MM SS N")
    print "Expect: N Actually: ", getNS("DDD MM SS w DD MM SS n")
if __name__ == '__main__':
    main()
