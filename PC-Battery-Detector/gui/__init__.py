'''
The primary use of __init__.py is to initialize Python package.
Any directory with an __init__.py file is considered a Python package. 
The different modules in the package are imported in a similar manner as plain modules, 
but with a special behavior for the __init__.py file, which is used to gather all package-wide definitions.
--------------
With the modules imported as below, any file which import a module from this folder(containing this __init__.py) will 
first look in this init file and access the respected imported module.
---------------
IF this file is empty. then any file can import from this folder by 
					'from folderName.file import moduleName'
-----------
Also, with this init.py file, you can import a group of modules from this folder by 'from folderName import *'
For this fxn to work, we use '__all__.' to gatther all the modules we will like to import when the user imports all.
                    __all__ = ['submodule1', 'submodule2']
			
----------------
Using init.py is beneficial since if you are structuring your project in various directories, 
from the import(from fileName import..), one can easily know from which folder the module comes from.
'''
from BatteryDetectorPopupGUI import Ui_batteryDetectorPopup_dialog
from ConfigGUI import Ui_MainWindow
from Confirmation_Dialog import Ui_Confirmation_Dialog
from mainWindow import Ui_MainWindow_frame