# -*- encoding: UTF-8 -*-
"""
    进博会，CIIE pepper 群舞，停止所有行为，并恢复站立姿势。

"""

import naoqi
from naoqi import ALProxy
import time
import threading

# 定义三个函数，分别是6个机器人

def robot_1():

    Robot_IP = "192.168.1.2"
    robot_1.BehaviorManager = ALProxy("ALBehaviorManager",Robot_IP,9559)
    robot_1.ALBehaviorManager.stopAllBehaviors()
    time.sleep(2)
    robot_1.RobotPosture = ALProxy("ALRobotPosture",Robot_IP,9559)
    robot_1.RobotPosture.goToPosture("StandInit",0.5)

def robot_2():

    Robot_IP = "192.168.1.3"
    robot_2.BehaviorManager = ALProxy("ALBehaviorManager",Robot_IP,9559)
    robot_2.ALBehaviorManager.stopAllBehaviors()
    time.sleep(2)
    robot_2.RobotPosture = ALProxy("ALRobotPosture",Robot_IP,9559)
    robot_2.RobotPosture.goToPosture("StandInit",0.5)

def robot_3():
    
    Robot_IP = "192.168.1.4"
    robot_3.BehaviorManager = ALProxy("ALBehaviorManager",Robot_IP,9559)
    robot_3.ALBehaviorManager.stopAllBehaviors()
    time.sleep(2)
    robot_3.RobotPosture = ALProxy("ALRobotPosture",Robot_IP,9559)
    robot_3.RobotPosture.goToPosture("StandInit",0.5)

def robot_4():
    
    Robot_IP = "192.168.1.5"
    robot_4.BehaviorManager = ALProxy("ALBehaviorManager",Robot_IP,9559)
    robot_4.ALBehaviorManager.stopAllBehaviors()
    time.sleep(2)
    robot_4.RobotPosture = ALProxy("ALRobotPosture",Robot_IP,9559)
    robot_4.RobotPosture.goToPosture("StandInit",0.5)

def robot_5():
    
    Robot_IP = "192.168.1.7"
    robot_5.BehaviorManager = ALProxy("ALBehaviorManager",Robot_IP,9559)
    robot_5.ALBehaviorManager.stopAllBehaviors()
    time.sleep(2)
    robot_5.RobotPosture = ALProxy("ALRobotPosture",Robot_IP,9559)
    robot_5.RobotPosture.goToPosture("StandInit",0.5)

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


