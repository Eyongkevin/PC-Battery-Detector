### Main Image
**PC-Battery-Detector** is a desktop application(Windows) build in python with the following functionalities:
- Displays PC battery level(%)
- Alarms when battery level falls to a certain percentage(defaults to **20%**)

PC-Battery-Detector allows you to constantly monitor your computer's battery level and set a minimum value (%) which the application will triggers an alarm if  your computer's battery level falls below this value.

### How to run PC-Battery-Detector
- Clone/Download PC-Battery-Detector https://github.com/Eyongkevin/PC-Battery-Detector.git
- Set up your environment. The neccessary packages needed can be found in ```requirement.txt```.
    - python 2.7
    - certifi              
    - pip                    
    - PyMI                      
    - python-qt5              
    - pywin32                   
    - setuptools               
    - six                       
    - vs2008_runtime            
    - wheel                     
    - wincertstore              
    - WMI 
- Navigate to the project direcdtory and do one of these
    - Double-click on **main.pyw**.
    - Open a command line and run ```python main.pyw```.

### Usage
PC-Battery-Detector_labledImage
PC-Battery-Detector consist of 2 main sections

**A.** This section shows the computer's current battery level in real-time. This percentage value turns to red when it falls bellow the minimum battery level, which defaults to **20%**

**B.** This section contains the followings:
###### a) Setting
###### Setting Image
Here, you can do the following settings:
1. Disable/Enable alarm popup
2. Set minimum battery level which will trigger alarm
3. Disable/Enable notification when battery is fully charged.
4. Disable/Enable alarm sound
5. reset to default
6. Set sound for the alarm.
7. Set alarm to pupup after every defined minutes.

###### b) About
###### About image
Displays information about the application. To view license, click the **Show Details..** button

###### c) Exit
You an exit the application either by clicking on the **Exit** button or **X** button on the right-top of the application GUI.

### How to constribute
**PC-Battery-Detector** is an [open source](https://opensource.com/resources/what-open-source) project. I am open to suggestions and willing to extend it to a different level. Enyone willing to contribute is highly welcomed.
To contribute, go ahead and:
1. Fork it!
2. Create your feature branch: ```git checkout -b my-new-feature```
3. Commit your changes: ```git commit -am 'Add some feature```
4. Push to the branch: ```git push origin my-new-feature```
5. Submit a pull request :D

### History
The first PC I ever had was Fujutsu, and I installed Windows 7 in it. With time, the PC performance was diminishing up to an extend where it hardly indicate or notify me when my battery level is below a certain value. Sometimes I forget to put it on charge and I keep working and the battery will get low till the PC will go off. This situation was really anoying me and so, I decided to create this app so that I would be notified each time my battery goes below a certain value.





"# PC-Battery-Detector" 
"# PC-Battery-Detector" 
