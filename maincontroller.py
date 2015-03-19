from objectdetection.contourdetection import ContourDetection

def main():
    """Main Controller application for PREN2"""
    objDetection = ContourDetection()
    print "Distanz zur Mitte: " + `objDetection.getDistanceFromMiddle()` + " Drehwinkel: " + `objDetection.getPosition()`

if __name__ == '__main__':
    main()

