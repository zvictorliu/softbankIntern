class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        self.nFacesDetected = -1

    def onUnload(self):
        #puts code for box cleanup here
        pass

    def onInput_onStart(self, p):
        if(len(p) > 0):
            if(self.nFacesDetected != len(p[1]) -1): # an additional array has been placed at the end for time
                self.nFacesDetected = len(p[1]) -1  # filtered info and has to be substracted when counting faces
                if(self.nFacesDetected != 0):
                    self.onFaceDetected( self.nFacesDetected )
                else:
                    self.onNoFace()
        else:
            if(self.nFacesDetected != 0):
                self.nFacesDetected = 0
                self.onNoFace()

    def onInput_onStop(self):
        pass