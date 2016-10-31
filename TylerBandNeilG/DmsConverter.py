def main():
    test_getEW()
    test_getNS()
    test_dms2dd()

## Q9
def getEW(dmsRecord):
    return dmsRecord[10].upper()

## Q10
def getNS(dmsRecord):
    return dmsRecord[21].upper()

## Q11
def dms2dd(dmsRecord):
    #DD for EW
    for i in dmsRecord[0:9]:
        latD = int(dmsRecord[0:3])
        latM = int(dmsRecord[4:6])
        latS = float(dmsRecord[7:9])
        latDD = latD + float(latM)/60 + float(latS)/3600
    if latD < 0 and latD>180:
        return None
    if latM <0 and latS<0 and latM>60 and latS>60:
        return None

    #DD for NS
    for i in dmsRecord[12:21]:
        lonD = int(dmsRecord[12:15])
        lonM = int(dmsRecord[16:18])
        lonS = float(dmsRecord[19:21])
        lonDD = lonD + float(lonM)/60 + float(lonS)/3600

    if lonD<0 and lonD>90:
        return None
    if lonM<0 and lonS<0 and lonM>60 and lonS>60:
        return None

    #long/lat slice
    lat = dmsRecord[0:9]
    lon= dmsRecord[12:21]
    EWdirection = getEW(dmsRecord)
    if EWdirection == 'W':
        EWsign = "-"
    else: EWsign = ""

    NSdirection = getNS(dmsRecord)
    if NSdirection == 'S':
        NSsign = "-"
    else: NSsign = ""

    return "Latitude Decimal Degrees: %0.2f \nLongitude Decimal Degrees: %0.2f \n\n %s %s,%s %s" %(latDD, lonDD, EWsign, lat, NSsign, lon)

##Testing functions

def test_getEW():
    print "Expect: W Actually: ", getEW("DDD MM SS W DD MM SS N")
    print "Expect: W Actually: ", getEW("DDD MM SS w DD MM SS N")

def test_getNS():
    print "Expect: N Actually: ", getNS("DDD MM SS W DD MM SS N")
    print "Expect: N Actually: ", getNS("DDD MM SS w DD MM SS n")

def test_dms2dd():
    print dms2dd("075 45 03 W 45 23 05 N")
    print dms2dd("075 45 03 E 45 23 05 S")
    print dms2dd("175 45 03 W 45 23 05 S")

if __name__ == '__main__':
    main()
