class MyClass(GeneratedClass):

    def __init__(self):
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        import threading
        self.motion = ALProxy("ALMotion")
        self.x = 0
        self.y = 0
        self.theta = 0
        self.ptask = qi.PeriodicTask()
        self.lock = threading.RLock()

    def onUnload(self):
        with self.lock:
            self.ptask.stop()
            self.x = 0
            self.y = 0
            self.theta = 0
            self.motion.moveToward(0, 0, 0)
            self.motion.waitUntilMoveIsFinished()

    def onInput_onStop(self):
        with self.lock:
            self.onUnload()
            self.onStopped()

    def onInput_onStart(self):
        with self.lock:
            period = self.getParameter("Period of direction update (s)")
            us_period = int(period*1000000)

            self.ptask.compensateCallbackTime(True)
            self.ptask.setCallback(self.updateMovement)
            self.ptask.setUsPeriod(us_period)
            self.ptask.start(True)

    def moveFailed(self):
        self.onUnload()
        self.onMoveFailed()

    def updateMovement(self):
        import math
        with self.lock:
            enableArms = self.getParameter("Arms movement enabled")
            self.motion.setMoveArmsEnabled(enableArms, enableArms)
            x = self.getParameter("X")
            y = self.getParameter("Y")
            theta = self.getParameter("Theta")
            period = self.getParameter("Period of direction update (s)")
            epsilon = 0.0001
            dx = math.fabs(x - self.x)
            dy = math.fabs(y - self.y)
            dt = math.fabs(theta - self.theta)

            # Update moveToward parameters
            if(dx > epsilon or dy > epsilon or dt > epsilon):
                self.x=x
                self.y=y
                self.theta=theta
                self.motion.moveToward(self.x, self.y, self.theta)

            # Check if the move has been canceled
            if (not self.motion.moveIsActive()):
                self.moveFailed()

            us_period = int(period*1000000)
            self.ptask.setUsPeriod(us_period)