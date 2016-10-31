def main():
    test_getCoordsFromGpx()

def getCoordsFromGpx(gpx):
    if gpx.count("trkpt"): # and gpx.startswith("trkpt")
        start = gpx.find("lat=")
        middle = gpx.find("lon=")
        end = gpx.find('">')
        return gpx[start+5:middle-2], gpx[middle+5:end]
    return "None"

def test_getCoordsFromGpx():
    print "Expect: ('45.3888995', '-75.7472631') Actually: ", getCoordsFromGpx('<trkpt lat="45.3888995" lon="-75.7472631">')
    print "Expect: None Actually: ", getCoordsFromGpx(' lat="45.3888995" lon="-75.7472631">')

if __name__ == '__main__':
    main()
