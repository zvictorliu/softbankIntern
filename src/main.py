import naoqi

tts = naoqi.ALProxy('ALTextToSpeech',"192.168.115.110",9559)
tts.say("Hello")