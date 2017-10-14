# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys, os
#sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/gui")
#sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/database")



from wmi import WMI
from threading import Thread
from subprocess import Popen
from time import time, sleep
from winsound import Beep
from ctypes import windll
from BatteryDetectorPopupController import BatteryDetectorPopupController
from mainWindow import Ui_MainWindow_frame
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QAction, QMessageBox, QMainWindow)
from database import Database 
from socket import socket, AF_INET, SOCK_STREAM
from select import select
#from timeExecution import decoratorTimeExecution 
	
class Main(Ui_MainWindow_frame,BatteryDetectorPopupController,Database):
						
	myHost = ''  					#this is the machine server name, usually, in server program, this value is ('') meaning the maching that the script runs on.
	myPort = 50007    				#this is the server port through which the client can listen to.it should be a non-reserve port(outside the range 0-1023)

	def __init__(self):
		self.notifyWhenFullyCharged = 'N'
		self.alarmDisable = False          # 'N'
		self.displayFlag = False
		self.batteryDetectorPopup_dialogShow = False
		self.connection = None
		
		self.batteryLevel = 0 						 		#holds the extracted battery level from the pc system.
		self.alarmBatteryLevel = 20             	 		#battery level which will popup alarm, by default it is set to 20
		self.disableSound = 0
		self.batteryCaption = ''
		self.c = WMI()
		self.threads = []          					 		#holds all the thread created, so that they can be join and check for completion.	
		self.pipe = ''
		self.Availability = 2      						    #2 = on charge, 3 = not on charge
		self.resolutionXreduceNumber = 140
		self.checkPowerPeriod = 30000
		self.updateBatteryLevelPeriod = 40000
		self.Beepfrequency = 4000
		self.Beepduration = 7000
		
		self.setDefaultDatabase()                           #take care of database initialization.
		self.getDataFromDatabaseToSetUp()
		self.startThreadToWaitData()                        # start thread to wait data from it config panel
	

	
	
	
	"""########################################################################################################################
												SET and EVENT METHODS
								these methods set variables during runtime.
	########################################################################################################################
	"""
	
			
	"""
	setFlagToTrue()
	@param void
	@return void 
	--------------
	it set a flag to 'True' to indicate that the alarm popup has been displayed already 
	Hence the popup also depends on this flag, and it can only disply if it is 'False'
	"""
	def setFlagToTrue(self):
		self.displayFlag = True
		
	"""
	setFlagToFalse()
	@param void
	@return void 
	--------------
	it set a flag to 'False' to indicate that the alarm popup has not yet or it can be displayed 
	Hence the popup also depends on this flag, and it can only disply if it is 'False'
	"""
	def setFlagToFalse(self):
		self.displayFlag = False
		
	"""
	findScreenResolution()
	@param void
	@return void
	--------------
	this get the screen resolution which will be used to possition the GUI.
	we want to position a GUI at the top rght conner of all screen(idependent of its resolution). so we get the resolution,
	then we reduce its x-axis by 140 and will mentain y-axis to 0.
	.............................................................................................................................
	"""
	def findScreenResolution(self):
		user32 = windll.user32
		self.resolutionX,self.resolutionY = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
		self.resolutionX = self.resolutionX - self.resolutionXreduceNumber
		
	"""
	setClickClosedEvent()
	@param void
	@return void
	--------------
	this set a click_and_close event to the 'exit' button(its PyQt5)
	"""		
	def setClickClosedEvent(self):
		self.exit_btn.clicked.connect(self.closedAllProgram_Helper)
		
	def setSettingclickEvent(self):
		self.setting_btn.clicked.connect(self.openSettingGUI_Helper)
		
	def setAboutClickEvent(self):
		self.about_btn.clicked.connect(self.openAboutGUI_Helper)
	
	
	
	
	"""########################################################################################################################
												THREAD METHODS
					these  methods are been called in a thread or calls a thread to perform their respective operations..
	########################################################################################################################
	"""
		
	
	"""
	loop(daemons)
	@param daemons[type: bool(True)]
	@void void
	--------------
	this loop starts a thread which alarms the battery level of the system.
	these depends on many values: battery level, display flag and availability(if the system is charging or not)
	if batteryLevel < [specified battery level which defaults to 20]
	         it check if flag is False and if system is charging, 
			 if true, it starts a Daemon thread which popup a GUI to alarm the level of the battery.
	if batteryLevel >[specified battery level which defaults to 20]
		it check if display flag is true
		if yes, it set the flag to false, so that it won't blog when battery goes down. also, it terminates the alarm GUI if not yet closed.
	"""
	def loop(self, daemons = True):		
		startTime = time()
		while True:
			if self.batteryLevel < self.alarmBatteryLevel and not self.displayFlag and self.Availability == 3 and not self.alarmDisable:       #availability = 3 means the system is not charging(not plug) and 2 otherwise.
				self.setFlagToTrue()                                                             #set flag to True to indicate that the alarm GUI will be displayed.
				thread = Thread(target = self.runPopup, args =())                      			 #start a thread(which popup the alarm GUI), and make it daemons.
				thread.setDaemon(daemons)
				thread.start()
				self.threads.append(thread)
									
				for thread in self.threads:                                                      #check if thread has finished his job, and terminate it.
					thread.join 
					
			elif self.batteryLevel > self.alarmBatteryLevel and self.displayFlag:                                   #if battery level is >20, 
				self.setFlagToFalse()
				self.terminatePipe()	
			sleep(60.0 - ((time() - startTime) % 60.0))			
			
	"""
	runPopup()
	@param void
	@return void
	-------------
	this starts the alarm GUI through a pipe, and trigger an alarm.
	this method is called as a thread
	we use the pipe object 'shell=True' to silence the command line shell popup. since by default this also triggers the popup of a command line shell.
	"""
	def runPopup(self):
		self.batteryDetectorPopup_dialogShow = True
		self.pipe = Popen('python BatteryDetectorPopupController.pyw '+ str(self.batteryLevel), shell=True)
		if not self.disableSound:
			Beep(self.Beepfrequency,self.Beepduration)  #frequency, duration

	def waitData(self):
		sockobj = socket(AF_INET, SOCK_STREAM)       				# create a TCP socket object. AF_INET(means the IP address protocol) and SOCK_STREAM(means the TCP transfer protocol)
		sockobj.bind((self.myHost, self.myPort))					# this associate the socket object with the IP address and port number.(note how it is a tuple)
		sockobj.listen(5)							 				# this represent the numb of client request that can be queued before new request are denied.

		while True:
			self.connection, self.address = sockobj.accept()  		#here .accept() listern for client connection to server, once done, it return a 'connection' which is used to communicate with the client. and 'address' which is the internet address of the client.
			while True:
				r,_,_ = select([self.connection], [],[])  			#check if there is data waiting. it prevents us to step in a waiting stage created by '.recv()'
				if r:
					data = self.connection.recv(1024) 				#this reads at most 1024 bytes of message sent from the client.
					if not data: break
					self.workOnData(data)		
			self.connection.close()			
		
		
	def startThreadToWaitData(self,daemons = True):
		thread = Thread(target = self.waitData, args =())                      #start a thread(which popup the alarm GUI), and make it daemons.
		thread.setDaemon(daemons)
		thread.start()
		
	"""
	starts a thread which runs a loop to continouesly check if the level of battery is less than a specific value and popup an alarm GUI
	"""
	def startLoop(self, daemons = True):
		thread = Thread(target = self.loop, args =())
		thread.setDaemon(daemons)                                              #made daemons 
		thread.start()
		
	
	
	
	
	
	"""########################################################################################################################
												RECURSIVE METHODS
					these  methods are been executed recursively, after a gievn period of time..
	########################################################################################################################
	"""
	
	"""
	checkPower()
	@param void
	@return void
	----------------
	this check the system and gather info about battery status(if charging or not) and battery percentage.
	It repeats it self after every 3 min to update the global variables.
	............................................................................................................................
	"""
	def checkPower(self):		
		for battery in self.c.win32_Battery():
			self.batteryCaption = battery.Caption
			self.Availability = battery.Availability	
			self.batteryLevel = battery.EstimatedChargeRemaining
		QtCore.QTimer.singleShot(self.checkPowerPeriod, self.checkPower) 			# calls it self after every given miniut, so it is recursive.
		
	"""
	updateBatteryLevel()
	@param void
	@return void
	-------------------
	this set a label value. this is made as a seperate method and repeats every 4 min so that it updates the label value in time.
	It changes the text color base on the battery level.
	also it reduce the font size when 100%, bc the space for it is small.
	"""
	def updateBatteryLevel(self):
		_translate = QtCore.QCoreApplication.translate
		self.batteryLevel_label.setText(_translate("MainWindow_frame", str(self.batteryLevel)+"%"))
		if self.batteryLevel < self.alarmBatteryLevel:
			self.batteryLevel_label.setStyleSheet("color:red")
		else:
			self.batteryLevel_label.setStyleSheet("color:white")
		if self.batteryLevel == 100:
			font = QtGui.QFont()
			font.setPointSize(20)
			self.batteryLevel_label.setFont(font)
		else:
			font = QtGui.QFont()
			font.setPointSize(24)
			self.batteryLevel_label.setFont(font)
			
		QtCore.QTimer.singleShot(self.updateBatteryLevelPeriod, self.updateBatteryLevel)
	
	
	
	
	
	"""########################################################################################################################
												OTHER METHODS
							these  methods do particular operation , not really specified.
	########################################################################################################################
	"""

	"""
	terminatePipe()
	@param void
	@void void
	--------------
	this terminate the batteryDetectorPopup GUI which was displayed to alarm a low battery.
	"""
	def terminatePipe(self):
		if self.pipe != '':
			self.pipe.terminate()
			self.pipe = ''

	def enableDisableSetting_btn(self,bool = False):
		self.setting_btn.setEnabled(bool)
	
	
	
	
	
	"""########################################################################################################################
												OVERIDE FROM GUI METHODS
					these  methods are helper method called by other method to help them execute their operation.
	########################################################################################################################
	"""	
	"""
	setupUi(MainWindow_frame)
	@param MainWindow_frame[type: object]
	@return void
	------------------
	this starts the main GUI, which displays battery level, and 3 buttons(setting, about, exit) which is used to control the program.
	"""
	def setupUi(self, MainWindow_frame):
		self.checkPower()										 #check battery level and if it is charging.
		Ui_MainWindow_frame.setupUi(self, MainWindow_frame)
		
		MainWindow_frame.setFixedSize(122, 221)                  #will set a fix size(unresizable). otherwise use '.resize(..)'
		self.findScreenResolution()
		MainWindow_frame.move(self.resolutionX,0)
		
		                                                    
		self.setClickClosedEvent()                                #set a click_and_close event to the 'exit' button.
		self.setSettingclickEvent()
		self.setAboutClickEvent()
		self.startLoop()                                          #this will start a thread which will run a loop  which will continouesly check if battery is less than a specific value

	"""
	retranslateUi(MainWindow_frame)
	@param MainWindow_frame[type: object]
	@callMethod [updateBatteryLevel]
	@return void
	--------------------
	this sets all the labels in the main window GUI.
	note that the battery level label is updated by 'updateBatteryLevel' which runs every 4 minut to update the value.
	"""
	def retranslateUi(self, MainWindow_frame):
		Ui_MainWindow_frame.retranslateUi(self, MainWindow_frame)	
		self.updateBatteryLevel()
	

	
	
		
	"""########################################################################################################################
												HELPER METHODS
					these  methods are helper method called by other method to help them execute their operation.
	########################################################################################################################
	"""
	
	"""
	closedAllProgram_Helper()
	@param void
	@return void
	-------------
	this terminates the main GUI, hence terminate the entire programs since all threads are made daemons
	"""
	def closedAllProgram_Helper(self):
		QtCore.QCoreApplication.instance().quit()
		
	#@decoratorTimeExecution
	def openSettingGUI_Helper(self):
		self.pipeConfig = Popen('python ConfigController.pyw '+ str(self.batteryLevel), shell=True)
		self.enableDisableSetting_btn()
	
	def openAboutGUI_Helper(self):
		Developer = 'Eyong Kevin Enowanyo'
		gitHub = 'wwww'
		email = 'tonyparkerkenz@gmail.com'
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Information)
		msg.setTextFormat(QtCore.Qt.RichText)

		msg.setText("e~BD v1.0")
		txt ="<b>Author</b>:<span style = 'color:blue';> "+Developer+"</span><br />\
			 <b>Source Code</b>: "+gitHub+ "<br /><br />\
			<b>e~BD</b> is a Battery Detector which detects battery level, and if lower than a specific value(which can be set by yourself, default to 20%)\
			it immediately pops an alarm to signal you."
		detailText = "e~BD is a free software, you can distribute it and/or modify it under the terms of the GNU General Public License as published by the free software foundation.This program is distributed in the hope that it will be usefull but without any WARRANTY"	
		msg.setInformativeText(txt)
		msg.setWindowTitle("About e~BD")
		msg.setDetailedText(detailText)
		msg.setStandardButtons(QMessageBox.Ok)
		retval = msg.exec_()


	
	"""########################################################################################################################
												DATABASE METHODS
							these  methods communicate with the database module...
	########################################################################################################################
	"""
	
	def setDefaultDatabase(self):
		self.createDefaultTable()
	
	def workOnData(self,data = None):
		if data == b'exit':		
			self.enableDisableSetting_btn(True)
		else:
			self.getDataFromDatabaseToSetUp(data)
			

	def getDataFromDatabaseToSetUp(self, data=None):
		if data == b'reset':
			self.deleteConfigDataSetTable()
		result = self.getData()
		self.alarmBatteryLevel = result[0]['alarmWhenDropTo']
		self.notifyWhenFullyCharged = result[0]['notifyWhenFullyCharged']
		self.disableSound = result[0]['disableSound']
		self.alarmDisable = result[0]['alarmDisable']
		self.setFlagToFalse()

		


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow_frame = QtWidgets.QFrame()
	ui = Main()
	ui.setupUi(MainWindow_frame)
	MainWindow_frame.show()
	sys.exit(app.exec_())



