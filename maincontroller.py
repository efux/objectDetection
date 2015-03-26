from objectdetection.contourdetection import ContourDetection
from objectdetection.hsvdetection import HSVDetection

def main():
    """Main Controller application for PREN2"""
    detections = []
    detections.append(ContourDetection())
    detections.append(HSVDetection())

    for d in detections:
        # If you print the distanceFromMiddle it is getting calculated multiple times,
        # call either getDistanceFromMiddle() or getPosition()
        print "Distanz zur Mitte: " + `d.getDistanceFromMiddle()` + " Drehwinkel: " + `d.getPosition()`

if __name__ == '__main__':
    main()

