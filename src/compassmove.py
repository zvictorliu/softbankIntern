class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)
        try :
            self.compass = ALProxy("ALVisualCompass")
        except Exception as e:
            self.compass = None
            self.logger.error(e)

    def onLoad(self):
        pass

    def onUnload(self):
        if self.compass:
            self.compass.moveTo(0.0, 0.0, 0.0)

    def onInput_onStart(self):
        if self.compass:
            self.compass.moveTo(self.getParameter("Distance X (m)"), self.getParameter("Distance Y (m)"), self.getParameter("Theta (rad)"))
        # The move is finished so output
        self.onStopped() #~ activate output of the box

    def onInput_onStop(self):
        self.onUnload()
        self.failure()