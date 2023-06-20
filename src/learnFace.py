class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)
        try:
            self.faceDetectionModule = ALProxy("ALFaceDetection")
        except Exception as e:
            self.faceDetectionModule = None
            self.logger.error(e)


    def onLoad(self):
        self.bIsRunning = False

    def onUnload(self):
        self.bIsRunning = False

    def onInput_onLearn(self, p):
        if( self.bIsRunning ):
            return
        self.bIsRunning = True
        if( self.faceDetectionModule and self.faceDetectionModule.learnFace( p ) ):
            self.onSuccess()
        else:
            self.onFailure()
        self.bIsRunning = False

    def onInput_onReLearn(self, p):
        if( self.bIsRunning ):
            return
        self.bIsRunning = True
        if( self.faceDetectionModule and self.faceDetectionModule.reLearnFace( p ) ):
            self.onSuccess()
        else:
            self.onFailure()
        self.bIsRunning = False