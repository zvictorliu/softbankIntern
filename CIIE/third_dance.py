# -*- encoding: UTF-8 -*-
"""
    pepper 同步舞蹈动作测试；
    获取舞蹈动作APP执行的behavior；
    通过runbehavior()执行动作；
    threading 多线程实现同步。
    "bz10004_hungarian_dance_v" 匈牙利舞曲
    "sbr_71130_pepper-ondo" 日本舞蹈
    "bz10003_dance_of_the_knights_v" 骑士之舞
    "bz10002_nutcracker_v" 胡桃夹子舞蹈  ----没有装
    'arcadia/body', 'arcadia/body_launcher', 'arcadia/full_launcher' 阿卡迪亚舞
    tai_chi-515d6a/behavior_1
    sbrc_10001/behavior_1

    sbrc10001-fe268e  画面 softbank group
    dhldzg-eb08aa 灯火里的中国


"""

import naoqi
from naoqi import ALProxy
import time
import threading

# 定义三个函数，分别是3个机器人

def robot_1():

    Robot_IP = "192.168.111.94"
    robot_1.BehaviorManager = ALProxy("ALBehaviorManager",Robot_IP,9559)
    robot_1.BehaviorManager.runBehavior("mika_relax")

def robot_2():

    Robot_IP = "192.168.111.95"
    robot_2.BehaviorManager = ALProxy("ALBehaviorManager",Robot_IP,9559)
    robot_2.BehaviorManager.runBehavior("mika_relax")

if __name__ == "__main__":

    Thread_1 = threading.Thread(target = robot_1)
    Thread_2 = threading.Thread(target = robot_2)

    Thread_1.start()
    Thread_2.start()
