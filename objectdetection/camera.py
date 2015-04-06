try:
    from imageparameters import ImageParameters
    from imagecamera import ImageCamera
    from webcam import Webcam
    from picamera2 import PiCamera2
    import picamera
    import picamera.array
    pimode = True
except:
    pimode = False

webcam = True

class Camera(object):
    """Camera object for getting pictures."""

    def __init__(self):
        """Initialize camera, either from Pi or webcam or image"""    
        self.width = ImageParameters.width
        self.height = ImageParameters.height
        self.__initialize()

    def __initialize(self):
        if pimode:
            self.camera = PiCamera2(self.width, self.height)
        else:
            if webcam:
                self.camera = Webcam(self.width, self.height)
            else:
                self.camera = ImageCamera(self.width, self.height)

    def capture(self):
        """Return image from camera / pi / picture"""
        return self.camera.capture()
