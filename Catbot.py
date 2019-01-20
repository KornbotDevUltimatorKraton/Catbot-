'''
  Author: Mr.Chanapai Chuadchum 
  Projectname: Catbot and hydraulic actuator 
  Describetion: This projectpurpose is to testing the hydraulic actuator 
  Date built: 15/1/2019 
'''
import microgear.client as microgear # IoT function to connect with the main system or other device wirelessly via the internet 
import pandas as pd   # Data set of pressure / Angle timing speed 
import sklearn  
from sklearn.linear_model import LinearRegression # Linear regression for the learning actuator data analysis 
import time # timing contorl for the actuator 
import scipy # For the formulars on the calculation 
from nanpy import(ArduinoApi,SerialManager) # Serial Manager to connecting the 8 bit MCU on board 
from nanpy import Servo  # Servo actuator control 
import numpy as np  # For the array control  
import cv2 # image processing for the vision system and the object detector  
   # Atmega 2560 
try: 
   connection = SerialManager() # SerialManager connection estrabrished 
   hydraulicunit = ArduinoApi(connection=connection) # connection connected 
except: 
   print("Hardware hydraulic error please reconnect")
'''
  Servo Shoulder leg 
''' 
   # Servo actuator setup for leg of the robot 
Servo1 = Servo(3)
Servo2 = Servo(4)
Servo3 = Servo(5) 
Servo4 = Servo(6)
 
   # Analog Sensors Reader sensing  
Sensing1 = 0 
Sensing2 = 0
Sensing3 = 0
Sensing4 = 0   
   # Angle Read potentiometer
AnglefrontLeft = 0 
AngleBackLeft  = 0
AnglefrontRight = 0 
AngleBackRight = 0 

   # Hydraulic poer setup for the pump control  DC/BLDC motor either able to use  
def Pumpcontrol(pressure):
    hydraulicunit.analogWrite(2,pressure) # Pressure control on the motor pump to drve actuator 
'''
    Front Leg 
'''
     # Left leg control code function 
def hydraulicLegFLeft(goal,pressure,Angle): #Angle function
     if Angle >= goal: 
          Pumpcontrol(pressure) # Pressure control function for the robotics actuators 
             # Outlet control 
          hydraulicunit.digitalWrite(23,hydraulicunit.HIGH) 
             # inlet open tank oil sucker
          hydraulicunit.digitalWrite(24,hydraulicunit.HIGH)
             # Inlet control 
          hydraulicunit.digitalWrite(25,hydraulicunit.LOW) 
             # Outlet open tank oil maintain level 
          hydraulicunit.digitalWrite(26,hydraulicunit.LOW)    
        
     if Angle <= goal: 
          Pumpcontrol(pressure)
             # Outlet control  
          hydraulicunit.digitalWrite(23,hydraulicunit.HIGH) 
             # inlet open tank oil sucker
          hydraulicunit.digitalWrite(24,hydraulicunit.HIGH)
             # Inlet control 
          hydraulicunit.digitalWrite(25,hydraulicunit.LOW) 
             # Outlet open tank oil maintain level 
          hydraulicunit.digitalWrite(26,hydraulicunit.LOW)  
     if Angle == goal:   
          Pumpcontrol(0)  # stop the pump to control the proposional angle desire 
          hydraulicunit.digitalWrite(23,hydraulicunit.LOW) 
             # inlet open tank oil sucker
          hydraulicunit.digitalWrite(24,hydraulicunit.LOW)  
             # Inlet control 
          hydraulicunit.digitalWrite(25,hydraulicunit.LOW) 
             # Outlet open tank oil maintain level 
          hydraulicunit.digitalWrite(26,hydraulicunit.LOW)
    #Right leg   
def hydraulicLegFRight(goal,pressure,Angle):
    if Angle >= goal: 
          Pumpcontrol(pressure) # Pressure control function for the robotics actuators 
             # Outlet control 
          hydraulicunit.digitalWrite(27,hydraulicunit.HIGH) 
             # inlet open tank oil sucker
          hydraulicunit.digitalWrite(28,hydraulicunit.HIGH)
             # Inlet control 
          hydraulicunit.digitalWrite(29,hydraulicunit.LOW) 
             # Outlet open tank oil maintain level 
          hydraulicunit.digitalWrite(30,hydraulicunit.LOW)    
        
    if Angle <= goal: 
          Pumpcontrol(pressure)
             # Outlet control  
          hydraulicunit.digitalWrite(27,hydraulicunit.HIGH) 
             # inlet open tank oil sucker
          hydraulicunit.digitalWrite(28,hydraulicunit.HIGH)
             # Inlet control 
          hydraulicunit.digitalWrite(29,hydraulicunit.LOW) 
             # Outlet open tank oil maintain level 
          hydraulicunit.digitalWrite(30,hydraulicunit.LOW)  
    if Angle == goal:   
          Pumpcontrol(0)  # stop the pump to control the proposional angle desire 
          hydraulicunit.digitalWrite(27,hydraulicunit.LOW) 
             # inlet open tank oil sucker
          hydraulicunit.digitalWrite(28,hydraulicunit.LOW)  
             # Inlet control 
          hydraulicunit.digitalWrite(29,hydraulicunit.LOW) 
             # Outlet open tank oil maintain level 
          hydraulicunit.digitalWrite(30,hydraulicunit.LOW)
'''
   Back Leg 
'''
        # Left leg control code function 
def hydraulicLegBLeft(goal,pressure,Angle): #Angle function
     if Angle >= goal: 
          Pumpcontrol(pressure) # Pressure control function for the robotics actuators 
             # Outlet control 
          hydraulicunit.digitalWrite(31,hydraulicunit.HIGH) 
             # inlet open tank oil sucker
          hydraulicunit.digitalWrite(32,hydraulicunit.HIGH)
             # Inlet control 
          hydraulicunit.digitalWrite(33,hydraulicunit.LOW) 
             # Outlet open tank oil maintain level 
          hydraulicunit.digitalWrite(34,hydraulicunit.LOW)    
        
     if Angle <= goal: 
          Pumpcontrol(pressure)
             # Outlet control  
          hydraulicunit.digitalWrite(31,hydraulicunit.HIGH) 
             # inlet open tank oil sucker
          hydraulicunit.digitalWrite(32,hydraulicunit.HIGH)
             # Inlet control 
          hydraulicunit.digitalWrite(33,hydraulicunit.LOW) 
             # Outlet open tank oil maintain level 
          hydraulicunit.digitalWrite(34,hydraulicunit.LOW)  
     if Angle == goal:   
          Pumpcontrol(0)  # stop the pump to control the proposional angle desire 
          hydraulicunit.digitalWrite(31,hydraulicunit.LOW) 
             # inlet open tank oil sucker
          hydraulicunit.digitalWrite(32,hydraulicunit.LOW)  
             # Inlet control 
          hydraulicunit.digitalWrite(33,hydraulicunit.LOW) 
             # Outlet open tank oil maintain level 
          hydraulicunit.digitalWrite(34,hydraulicunit.LOW)

def hydraulicLegBRight(goal,pressure,Angle):
     if Angle >= goal: 
          Pumpcontrol(pressure) # Pressure control function for the robotics actuators 
             # Outlet control 
          hydraulicunit.digitalWrite(31,hydraulicunit.HIGH) 
             # inlet open tank oil sucker
          hydraulicunit.digitalWrite(32,hydraulicunit.HIGH)
             # Inlet control 
          hydraulicunit.digitalWrite(33,hydraulicunit.LOW) 
             # Outlet open tank oil maintain level 
          hydraulicunit.digitalWrite(34,hydraulicunit.LOW)    
        
     if Angle <= goal: 
          Pumpcontrol(pressure)
             # Outlet control  
          hydraulicunit.digitalWrite(31,hydraulicunit.HIGH) 
             # inlet open tank oil sucker
          hydraulicunit.digitalWrite(32,hydraulicunit.HIGH)
             # Inlet control 
          hydraulicunit.digitalWrite(33,hydraulicunit.LOW) 
             # Outlet open tank oil maintain level 
          hydraulicunit.digitalWrite(34,hydraulicunit.LOW)  
     if Angle == goal:   
          Pumpcontrol(0)  # stop the pump to control the proposional angle desire 
          hydraulicunit.digitalWrite(31,hydraulicunit.LOW) 
             # inlet open tank oil sucker
          hydraulicunit.digitalWrite(32,hydraulicunit.LOW)  
             # Inlet control 
          hydraulicunit.digitalWrite(33,hydraulicunit.LOW) 
             # Outlet open tank oil maintain level 
          hydraulicunit.digitalWrite(34,hydraulicunit.LOW)
     # 4 Servos sequencetial actuator control function 
def Servosequential(angle1,angle2,angle3,angle4):  
       Servo1.write(angle1)
       Servo2.write(angle2)
       Servo3.write(angle3)
       Servo4.write(angle4) 
def Hydraulicsequential(goal1,goal2,goal3,goal4,H1angle,H2angle,H3angle,H4angle,pressure):
    '''
        Right leg sequential 
    '''
    hydraulicLegFRight(goal1,pressure,H1angle) #For the first Right leg  
    hydraulicLegBRight(goal2,pressure,H2angle) #For the back Right leg 
    '''
      Left leg sequential 
    '''
    hydraulicLegFLeft(goal3,pressure,H3angle) #For the first Left leg   
    hydraulicLegBLeft(goal4,pressure,H4angle) #For the back Left leg 

def Walkingsequence(timing,maxangle,minangle,H1angle,H2angle,H3angle,H4angle):  # Speed for the servo actuator 
    for fl in range(minangle,maxangle): 
        Servosequential(H1angle,(fl-H2angle),H3angle,(fl-H4angle))
        time.sleep(timing)
    for bl in range(maxangle,minangle,-1):
         Servosequential((bl-H1angle),H2angle,H3angle,(bl-H4angle))
         time.sleep(timing)
def Jumpingmode(angle1,angle2,angle3,angle4,timing,maxangle,goal,desireangle,distance,Anglefront,pressure): #Function from the distance and angle calculation 
    
    Servosequential(angle1,angle2,angle3,angle4) #the function of the servo actuator control 
    hydraulicLegBLeft(goal,pressure,maxangle) # Maxangle at the left 
    hydraulicLegBRight(goal,pressure,maxangle) # Maxangleat the right   
    if angle1 == 180: 
         if angle2 == 180: 
             hydraulicLegFLeft(goal,Anglefront,pressure) # Pressure and angle desire function 
             hydraulicLegFRight(goal,(desireangle-Anglefront),pressure)        
  
def Runningmode(Runtiming,angle1,angle2,angle3,angle4): # High speed running mode robot 
     Servosequential(angle1,angle2,angle3,angle4) # Servo angle control function sequential 
      
while True: 
          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # All analog read serial pins 
          AnglefrontLeft = hydraulicunit.analogRead(0) 
          AngleBackRight = hydraulicunit.analogRead(1) 
          AnglefrontRight = hydraulicunit.analogRead(2)
          AngleBackLeft = hydraulicunit.analogRead(3)   
          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
               # vision system and condition control camera  

