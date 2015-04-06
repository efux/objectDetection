from objectdetection.candetection import CanDetection

def main():
    """Main Controller application for PREN2"""
    detection = CanDetection()

    # Start initialisation for the camera and take the first initial image without a camera
    detection.initialize()

    # Initialisation done, waiting for keypress to start
    raw_input("Press Enter to continue...")

    # Detect the can
    print "Turning the tellbot: " + `detection.getTurnAngleInDegree()`

if __name__ == '__main__':
    main()

