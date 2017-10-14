import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/gui")
#sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/database")
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_batteryDetectorPopup_dialog


class BatteryDetectorPopupController(Ui_batteryDetectorPopup_dialog):
	imagePath = 'image/low-battery-warning2.jpg'                     # Path to te image.

	"""
	Contructor(batteryLevel)
	@param batteryLevel [int , 4]
	@return void
	------------------
	on initialization, it received battery level from the main GUI to show it in the popup
	"""
	def __init__(self, batteryLevel):
		self.batteryLevel = batteryLevel
		
		
		
	"""########################################################################################################################
												OVERIDE METHODS
										these  methods overide method from the inherited GUI ...
	########################################################################################################################
	"""
	
	"""
	setupUi(batteryDetectorPopup_dialog)
	@param batteryDetectorPopup_dialog [object]
	@return void
	------------------
	it adds the close event. and also calls the side_image to display the image at the left of the frame
	"""
	def setupUi(self, batteryDetectorPopup_dialog):
		Ui_batteryDetectorPopup_dialog.setupUi(self, batteryDetectorPopup_dialog)
		self.batteryDetectorPopup_dialog = batteryDetectorPopup_dialog
		self.setClickClosedEvent()
		self.side_image()

	"""
	retranslateUi(batteryDetectorPopup_dialog)
	@param batteryDetectorPopup_dialog [object]
	@return void
	------------------
	it set the text value to the alert label. ie it displays the current battery level on the popup GUI
	"""	
	def retranslateUi(self, batteryDetectorPopup_dialog):
		Ui_batteryDetectorPopup_dialog.retranslateUi(self, batteryDetectorPopup_dialog)
		self.alert_text.setText("Your battery is running low("+ str(self.batteryLevel) + "%)")
		
		
		
		
	"""########################################################################################################################
												OTHER METHODS
										these  methods perform particular operations in this application. ...
	########################################################################################################################
	"""
	"""
	side_image()
	@param void
	@return void
	-----------------------
	this get the image from it path and position it at the left side of the frame
	"""
	def side_image(self):
		self.imageLabel = QtWidgets.QLabel(self.batteryDetectorPopup_dialog)
		self.imageLabel.setGeometry(QtCore.QRect(10, 10, 91, 91))
		leftPixelMap = QtGui.QPixmap(self.imagePath)
		self.imageLabel.setPixmap(leftPixelMap)

		
	"""########################################################################################################################
												EVENT METHODS
										these  methods set event ...
	########################################################################################################################
	"""
	
	"""
	setClickClosedEvent()
	@param void
	@return void
	-------------------------
	set close event to the close button
	"""
	def setClickClosedEvent(self):
		self.close_btn.clicked.connect(self.closedEvent_Helper)
 


	"""########################################################################################################################
												HELPER METHODS
										  these  are helper methods  ...
	########################################################################################################################
	"""
	def closedEvent_Helper(self):
		QtCore.QCoreApplication.instance().quit()	

		
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	batteryDetectorPopup_dialog = QtWidgets.QDialog()        
	ui = BatteryDetectorPopupController(sys.argv[1])
	ui.setupUi(batteryDetectorPopup_dialog)
	batteryDetectorPopup_dialog.show()
	sys.exit(app.exec_())