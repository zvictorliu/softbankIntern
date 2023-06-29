# -*- encoding: UTF-8 -*-
"""
    进博会 pepper 同步舞蹈动作，初始化设定；
    pepper 的开场介绍

"""

import naoqi
from naoqi import ALProxy
import time
import threading

# 定义三个函数，分别是6个机器人

def robot_1():

    Robot_IP = "192.168.1.2"
    robot_1.TextToSpeech = ALProxy("ALTextToSpeech",Robot_IP,9559)
    robot_1.TextToSpeech.setLanguage("Chinese")
    robot_1.TextToSpeech.say("欢迎大家来到进博会人工智能体验区，我是智能机器人 Pepper，接下来，请欣赏我为大家带来的舞蹈表演吧！")

def robot_2():

    Robot_IP = "192.168.1.3"
    robot_2.TextToSpeech = ALProxy("ALTextToSpeech",Robot_IP,9559)
    robot_2.TextToSpeech.setLanguage("Chinese")
    robot_1.TextToSpeech.say("欢迎大家来到进博会人工智能体验区，我是智能机器人 Pepper，接下来，请欣赏我为大家带来的舞蹈表演吧！")

def robot_3():
    
    Robot_IP = "192.168.1.4"
    robot_3.TextToSpeech = ALProxy("ALTextToSpeech",Robot_IP,9559)
    robot_3.TextToSpeech.setLanguage("Chinese")
    robot_1.TextToSpeech.say("欢迎大家来到进博会人工智能体验区，我是智能机器人 Pepper，接下来，请欣赏我为大家带来的舞蹈表演吧！")

def robot_4():
    
    Robot_IP = "192.168.1.5"
    robot_4.TextToSpeech = ALProxy("ALTextToSpeech",Robot_IP,9559)
    robot_4.TextToSpeech.setLanguage("Chinese")
    robot_1.TextToSpeech.say("欢迎大家来到进博会人工智能体验区，我是智能机器人 Pepper，接下来，请欣赏我为大家带来的舞蹈表演吧！")

def robot_5():
    
    Robot_IP = "192.168.1.7"
    robot_5.TextToSpeech = ALProxy("ALTextToSpeech",Robot_IP,9559)
    robot_5.TextToSpeech.setLanguage("Chinese")
    robot_1.TextToSpeech.say("欢迎大家来到进博会人工智能体验区，我是智能机器人 Pepper，接下来，请欣赏我为大家带来的舞蹈表演吧！")

if __name__ == "__main__":

    Thread_1 = threading.Thread(target = robot_1)
    Thread_2 = threading.Thread(target = robot_2)
    Thread_3 = threading.Thread(target = robot_3)
    Thread_4 = threading.Thread(target = robot_4)
    Thread_5 = threading.Thread(target = robot_5)

    Thread_1.start()
    Thread_2.start()
    Thread_3.start()
    Thread_4.start()
    Thread_5.start()
