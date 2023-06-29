# -*- encoding: UTF-8 -*-
"""
    进博会 pepper 同步舞蹈动作，初始化设定；
    关闭pepper的自主生活模式；
    唤醒机器人；
    初始化站立姿势

"""

import naoqi
from naoqi import ALProxy
import time
import threading

# 定义三个函数，分别是6个机器人

def robot_1():

    Robot_IP = "192.168.1.2"
    robot_1.AutonomousLife = ALProxy("ALAutonomousLife",Robot_IP,9559)
    robot_1.AutonomousLife.setState("disabled")
    time.sleep(5)
    robot_1.Motion = ALProxy("ALMotion",Robot_IP,9559)
    robot_1.Motion.wakeUp()
    time.sleep(5)
    robot_1.AudioDevice = ALProxy("ALAudioDevice",Robot_IP,9559)
    robot_1.AudioDevice.setOutputVolume(80)
    robot_1.RobotPosture = ALProxy("ALRobotPosture",Robot_IP,9559)
    robot_1.RobotPosture.goToPosture("StandInit",0.5)


def robot_2():

    Robot_IP = "192.168.1.3"
    robot_2.AutonomousLife = ALProxy("ALAutonomousLife",Robot_IP,9559)
    robot_2.AutonomousLife.setState("disabled")
    time.sleep(5)
    robot_2.Motion = ALProxy("ALMotion",Robot_IP,9559)
    robot_2.Motion.wakeUp()
    time.sleep(5)
    robot_2.AudioDevice = ALProxy("ALAudioDevice",Robot_IP,9559)
    robot_2.AudioDevice.setOutputVolume(80)
    robot_2.RobotPosture = ALProxy("ALRobotPosture",Robot_IP,9559)
    robot_2.RobotPosture.goToPosture("StandInit",0.5)

def robot_3():
    
    Robot_IP = "192.168.1.4"
    robot_3.AutonomousLife = ALProxy("ALAutonomousLife",Robot_IP,9559)
    robot_3.AutonomousLife.setState("disabled")
    time.sleep(5)
    robot_3.Motion = ALProxy("ALMotion",Robot_IP,9559)
    robot_3.Motion.wakeUp()
    time.sleep(5)
    robot_3.AudioDevice = ALProxy("ALAudioDevice",Robot_IP,9559)
    robot_3.AudioDevice.setOutputVolume(80)
    robot_3.RobotPosture = ALProxy("ALRobotPosture",Robot_IP,9559)
    robot_3.RobotPosture.goToPosture("StandInit",0.5)


def robot_4():
    
    Robot_IP = "192.168.1.5"
    robot_4.AutonomousLife = ALProxy("ALAutonomousLife",Robot_IP,9559)
    robot_4.AutonomousLife.setState("disabled")
    time.sleep(5)
    robot_4.Motion = ALProxy("ALMotion",Robot_IP,9559)
    robot_4.Motion.wakeUp()
    time.sleep(5)
    robot_4.AudioDevice = ALProxy("ALAudioDevice",Robot_IP,9559)
    robot_4.AudioDevice.setOutputVolume(80)
    robot_4.RobotPosture = ALProxy("ALRobotPosture",Robot_IP,9559)
    robot_4.RobotPosture.goToPosture("StandInit",0.5)

def robot_5():
    
    Robot_IP = "192.168.1.7"
    robot_5.AutonomousLife = ALProxy("ALAutonomousLife",Robot_IP,9559)
    robot_5.AutonomousLife.setState("disabled")
    time.sleep(5)
    robot_5.Motion = ALProxy("ALMotion",Robot_IP,9559)
    robot_5.Motion.wakeUp()
    time.sleep(5)
    robot_5.AudioDevice = ALProxy("ALAudioDevice",Robot_IP,9559)
    robot_5.AudioDevice.setOutputVolume(80)
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

