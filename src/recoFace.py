class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        self.timeFilteredResult = [];

    def onUnload(self):
        #puts code for box cleanup here
        pass

    def onInput_onStart(self, p):

        if(len(p) > 0):
            if(len(p[1]) > 0): # just in case of the ALValue is in the wrong format
                # get the ALValue returned by the time filtered recognition:
                #    - [] when nothing new.
                #    - [4] when a face has been detected but not recognized during the first 8s.
                #    - [2, [faceName]] when one face has been recognized.
                #    - [3, [faceName1, faceName2, ...]] when several faces have been recognized.
                self.timeFilteredResult = p[1][len(p[1]) -1]
                if( len(self.timeFilteredResult) == 1 ):
                    # If a face has been detected for more than 8s but not recognized
                    if(self.timeFilteredResult[0] == 4):
                        self.onDetectWithoutReco()
                elif( len(self.timeFilteredResult) == 2 ):
                    # If one or several faces have been recognized
                    if(self.timeFilteredResult[0] in [2, 3]):
                        for s in self.timeFilteredResult[1]:

                            self.onRecognizedFace( s )

    def onInput_onStop(self):
        pass