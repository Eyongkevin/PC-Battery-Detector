from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QMessageBox,QDialog,QWidget
from main import Ui_MainWindow_frame
from database import Database
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread, Event
from select import select


class ConfigController(Ui_MainWindow, Database):
	serverHost = 'localhost'
	serverPort = 50007
	batteryLevel = 0
	notifyWhenFullyCharged = 0
	alarmDisable = 0
	disableSound = 0 
	alarmBatteryLevel = 2
	checked = False
	
	"""
	Contructor(batteryLevel)
	@param batteryLevel [int , 4]
	@return void
	------------------
	on initialization, it gets data from the database to initialize its variable, 
	it also stores the batteryLevel gotten from the calling object.
	And also it starts a thread event.
	"""
	def __init__(self, batteryLevel):
		self.getAndSetDataFromDatabase()
		self.batteryLevel = batteryLevel
		self._stopevent = Event()
		
		
			
	"""########################################################################################################################
												OVERIDE METHODS
										these  methods overide method from the inherited GUI ...
	########################################################################################################################
	"""
	"""
	setupUi(MainWindow)
	@param MainWindow [object]
	@return void
	------------------
	Here in addition, we disable some properties, set some values and regiester events to buttons like(Apply, close and reset)
	
	"""	
	def setupUi(self, MainWindow):
		Ui_MainWindow.setupUi(self,MainWindow)
		MainWindow.setFixedSize(543, 370)
		self.DisableAlarm_checkBox.setChecked(self.alarmDisable)                               
		self.AlarmPawerLevel_spinBox.setValue(self.alarmBatteryLevel)                                        #alarm 
		#----------------------------------Disable ------------------------------------------
		self.setDefaultBeep_checkBox.setEnabled(False)
		self.BrowseSound_btn.setEnabled(False)
		self.Repeat_spinBox.setEnabled(False)
		self.NotifyOnBatteryFull_checkBox.setEnabled(False)
		#--------------------------------------------------------------------------------------
		
		self.BatteryLevel_progressBar.setProperty("value", self.batteryLevel)
		self.DisableSound_checkBox.setChecked(self.disableSound)
		
		#------------------------ Register Events---------------------
		self.setClickApplyEvent()
		self.setClickClosedEvent()
		self.setClickResetEvent()

	"""
	retranslateUi(MainWindow)
	@param MainWindow [object]
	@return void
	------------------
	in addition, it set the batteryLevel gotten from the calling object so it can be displayed on its GUI
	"""
	def retranslateUi(self, MainWindow):
		Ui_MainWindow.retranslateUi(self, MainWindow)
		_translate = QtCore.QCoreApplication.translate
		self.powerLevel_label.setText(_translate("MainWindow", "Power Level "+str(self.batteryLevel)+" %"))
		


	"""
	def startThreadToWaitData(self,daemons = True):
		self.thread = Thread(target = self.waitDataFromMain_Helper, args =())                      #start a thread(which popup the alarm GUI), and make it daemons.
		self.thread.setDaemon(daemons)
		self.thread.start()
	"""
	
	
	
	"""########################################################################################################################
												SET and EVENT METHODS
								these methods set variables during runtime.
	########################################################################################################################
	"""
			
	def setClickApplyEvent(self):
		self.Apply_btn.clicked.connect(self.clickApplyEvent_Helper)      	  #apply btn
		
	def setClickClosedEvent(self):
		self.Cancel_btn.clicked.connect(self.closedEvent_Helper)			  # cancel btn
		
	def setClickResetEvent(self):
		self.Reset_btn.clicked.connect(self.resetEvent_Helper)                 # reset btn
	
	"""
	getDataFromGUI(self)
	@param void
	@return void
	-------------------------------
	after user has set his configuration, this method gets the respective values and set the variabhles.
	"""
	def getDataFromGUI(self):
		self.alarmBatteryLevel = self.AlarmPawerLevel_spinBox.value()
		if self.DisableAlarm_checkBox.isChecked():
			self.alarmDisable = 1
		else:
			self.alarmDisable = 0
		if self.DisableSound_checkBox.isChecked():
			self.disableSound = 1
		else:
			self.disableSound = 0
	
	"""
	setConfigToDefault()
	@param void
	@return void
	---------------------------
	this set alam, power level spinbox and sound to their default values.
	This method is called on reset 
	"""
	def setConfigToDefault(self):
		self.DisableAlarm_checkBox.setChecked(False)
		self.AlarmPawerLevel_spinBox.setValue(20)
		self.DisableSound_checkBox.setChecked(False)



		
	"""########################################################################################################################
												DATABASE METHODS
							these  methods communicate with the database module...
	########################################################################################################################
	"""
	
	"""
	getAndSetDataFromDatabase(self)
	@param void
	@return void
	-------------------------------
	On startup, this method gets either the default or already set values from the database to initialize the variables..
	"""
	def getAndSetDataFromDatabase(self):
		result = self.getData()
		self.alarmBatteryLevel = result[0]['alarmWhenDropTo']
		self.notifyWhenFullyCharged = result[0]['notifyWhenFullyCharged']
		
		if result[0]['alarmDisable'] == 1:
			self.alarmDisable = True
		else:
			self.alarmDisable = False
		if result[0]['disableSound'] == 1:
			self.disableSound = True
		else:
			self.disableSound = False


		

		
		
		
		
	"""########################################################################################################################
												HELPER to DATABASE METHODS
					these  methods are helper method called by other method to help them execute their operation.
	########################################################################################################################
	"""
	
	def updateBatteryPercentage_Helper(self,data):
		getPercentate = int(data.decode())
		_translate = QtCore.QCoreApplication.translate
		self.powerLevel_label.setText(_translate("MainWindow", "Power Level "+str(getPercentate)+" %"))
		self.BatteryLevel_progressBar.setProperty("value", getPercentate)
		print(getPercentate)
		
	def clickApplyEvent_Helper(self):
		self.setDataToSetTable_helper()
		lines =[b'apply']
		self.sentSignal(lines)
		
	def closedEvent_Helper(self):
		lines = [b'exit']
		self.sentSignal(lines)
		self.joinThread()
		QtCore.QCoreApplication.instance().quit()	
		
	def setDataToSetTable_helper(self):
		self.getDataFromGUI()
		self.setDataToSetTable(self.alarmBatteryLevel,self.notifyWhenFullyCharged,self.alarmDisable,self.disableSound)
	
	def resetEvent_Helper(self):
		#self.questionMessage()
		lines =[b'reset']
		self.setConfigToDefault() 
		self.sentSignal(lines)
		
	"""
	def waitDataFromMain_Helper(self):
		sockobj = socket(AF_INET, SOCK_STREAM)  		#create a socket object
		sockobj.connect((self.serverHost, self.serverPort))  		#connect to the server(specify the server name and port number)
		
		while not self._stopevent.isSet():
			r,_,_ = select([sockobj], [],[])
			if r:
				data = sockobj.recv(1024) #this reads at most 1024 bytes of message sent from the client.
				if not data: break
				self.updateBatteryPercentage_Helper(data)
		sockobj.close()
	"""
	
		
		
	"""########################################################################################################################
												OTHER METHODS
							these  methods do particular operation , not really specified.
	########################################################################################################################
	"""
	
	def sentSignal(self, lines):
		sockobj = socket(AF_INET, SOCK_STREAM)  		           #create a socket object
		sockobj.connect((self.serverHost, self.serverPort))  		#connect to the server(specify the server name and port number)
		
		for line in lines:
			sockobj.send(line)
		sockobj.close()
		
	def joinThread(self,timeout = None):
		self._stopevent.set()
	
	"""
	----------------------------------------------------------------------------------
							Dialog Box
	---------------------------------------------------------------------------------------
	"""
	"""
	def questionMessage(self):    
		reply = QMessageBox.question(self, "Do u",'Do you really want to reset?',QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.Cancel)
		if reply == QMessageBox.Yes:
			print('yes')
		elif reply == QMessageBox.No:
			print('no')
		else:
			print('cancel')
	"""
	
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = ConfigController(sys.argv[1])
	ui.setupUi(MainWindow)
	MainWindow.show()
	app.aboutToQuit.connect(ui.closedEvent_Helper)       #set event  to window main close 'X' button 
	sys.exit(app.exec_())

	
	
	