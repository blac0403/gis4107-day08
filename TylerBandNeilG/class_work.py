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
##def getInitials(fullName):
##    name = fullName.split()
##    for letter in name:
##        print (letter[0] + "."),
##    print('')
##
##    name = fullName.split()
##    initials = ''
##    for letter in name:
##        initials += ''.join(letter[0]) + '.'
##    return initials
##
##
##def test_getInitials():
##    print getInitials("John Samuel Wobbly")
##    print getInitials("Dylan Mcdermott")
##    print getInitials("Nora Young")

###test_getInitials()
##
##
###Question 5
##def isValidPhoneNumber(phoneNumber):
##    if len(phoneNumber) ==12:
##        if phoneNumber[0:3:7].isdigit() and phoneNumber[8:12].isdigit():
##            pass
##        if phoneNumber[3] and phoneNumber[7] =='-':
##            return True
##    return False
##
##
##def test_isValidPhoneNumber():
##    print isValidPhoneNumber("999-999-9999")
##
###test_isValidPhoneNumber()
##
##
##Question 6
##def phoneNumberHasLetters(phoneNumber):
##    if len(phoneNumber) == 12:
##        if phoneNumber [3] and phoneNumber[7] == '-':
##            pass
##        if phoneNumber[0:3].isdigit():
##            pass
##        if (phoneNumber[4:7:12].isalpha()) == 1:
##            return True
##    return False
##
##def test_phoneNumberHasLetters():
##    print phoneNumberHasLetters("999-A99-9999")
##    print phoneNumberHasLetters("999-A99-BB99")
##    print phoneNumberHasLetters("999-999-9999")
##    print phoneNumberHasLetters("9A9-999-9999")
##
##test_phoneNumberHasLetters()
##
##
###Question 7
##def getFeatureTypeFromName(fcName):
##    if fcName.upper().endswith('_PNT'):
##        return "Point"
##    if fcName.upper().endswith('_LIN'):
##        return "Line"
##    if fcName.upper().endswith('_PLY'):
##        return "Polygon"
##    return "Unknown"
##
##def test_getFeatureTypeFromName():
##    print getFeatureTypeFromName("adc_PNT")
##    print getFeatureTypeFromName("adasdc_LIN")
##    print getFeatureTypeFromName("adasdasdasdc_PLY")
##    print getFeatureTypeFromName("adc_pnt")
##    print getFeatureTypeFromName("adasdc_lin")
##    print getFeatureTypeFromName("adasdasdasdc_ply")
##    print getFeatureTypeFromName("adasd.ply")
##    print getFeatureTypeFromName("adasdasdasdc_y")
##
##test_getFeatureTypeFromName()

###Question 8
##def getCoordsFromGpx(gpx):
##    if gpx.count("trkpt"): # and gpx.startswith("trkpt")
##        start = gpx.find("lat=")
##        middle = gpx.find("lon=")
##        end = gpx.find('">')
##        return gpx[start+5:middle-2], gpx[middle+5:end]
##    return "None"
##
##def test_getCoordsFromGpx():
##    print getCoordsFromGpx('<trkpt lat="45.3888995" lon="-75.7472631">')
##    print getCoordsFromGpx(' lat="45.3888995" lon="-75.7472631">')
##
##test_getCoordsFromGpx()

#Question 9
def getEW(dmsRecord):
    return dmsRecord[10].upper()

def test_getEW():
    print getEW("DDD MM SS W DD MM SS N")
    print getEW("DDD MM SS w DD MM SS N")

#test_getEW()


#Qestion 10
def getNS(dmsRecord):
    return dmsRecord[21].upper()

def test_getNS():
    print getNS("DDD MM SS W DD MM SS N")
    print getNS("DDD MM SS w DD MM SS n")

#test_getNS()

#Question 11
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

def test_dms2dd():
    print dms2dd("075 45 03 W 45 23 05 N")

test_dms2dd()
