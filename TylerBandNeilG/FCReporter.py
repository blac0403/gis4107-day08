def main():
    test_getFeatureTypeFromName()

def getFeatureTypeFromName(fcName):
    if fcName.upper().endswith('_PNT'):
        return "Point"
    if fcName.upper().endswith('_LIN'):
        return "Line"
    if fcName.upper().endswith('_PLY'):
        return "Polygon"
    return "Unknown"

def test_getFeatureTypeFromName():
    print "Expect Point. Actually: ", getFeatureTypeFromName("adc_PNT")
    print "Expect Line. Actually: ", getFeatureTypeFromName("adasdc_LIN")
    print "Expect Polygon. Actually: ", getFeatureTypeFromName("adasdasdasdc_PLY")
    print "Expect Point. Actually: ", getFeatureTypeFromName("adc_pnt")
    print "Expect Line. Actually: ", getFeatureTypeFromName("adasdc_lin")
    print "Expect Polygon. Actually: ", getFeatureTypeFromName("adasdasdasdc_ply")
    print "Expect Unknown. Actually: ", getFeatureTypeFromName("adasd.ply")
    print "Expect Unknown. Actually: ", getFeatureTypeFromName("adasdasdasdc_y")

if __name__ == '__main__':
    main()
