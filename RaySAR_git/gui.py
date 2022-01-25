'''
Created on 13 Dec 2021

@author: rasmus
'''




from PyQt5              import QtWidgets, QtCore, QtGui
from PyQt5.QtGui        import QDoubleValidator
from PyQt5.QtWidgets    import QWidget, QMenu, QAction, QProgressBar, QLineEdit, QLabel, QFileDialog, QTabWidget, QVBoxLayout, QFormLayout, QLineEdit, QCheckBox, QGroupBox, QGridLayout
from PyQt5.QtCore       import Qt, QThread, pyqtSignal
from PyQt5.Qt           import QDial, QSlider, QHBoxLayout, QPushButton, QFont, QMessageBox, QObject, QInputDialog

from application import Application
from numpy.ma.core import anomalies




class GUI(QtWidgets.QMainWindow):
    '''
    The class GUI handles the drawing of the Application-class 
    and lets user to interact with it
    '''
    def __init__(self):
        super().__init__()
        
        self.app = Application()
        self.init_window()
        self.init_actions()
        self.init_tool_bar()
        self.init_tab1()
        
    
    ###################### GUI INITS #########################    
        
    def init_window(self):
        '''
        Show main window and add central tab widget
        '''
        self.setGeometry(300, 100, 900, 600)
        self.setWindowTitle('GUI Template')
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
  
        # Add tabs
        self.tabs.addTab(self.tab1, "Parameters")
        self.tabs.addTab(self.tab2, " 2 ")
        self.tabs.addTab(self.tab3, " 3 ")
        
        self.setCentralWidget(self.tabs)
        self.show()
        
        
    def init_actions(self):
        '''
        Create actions for menu and tool bar
        '''
        # open file
        self.open_action = QAction("&Load file", self)
        self.open_action.triggered.connect(self.new_file) 

        
    def init_tool_bar(self):
        '''
        Adds created actions to tool bar
        '''
        tool_bar = self.addToolBar("File")
        tool_bar.addAction(self.open_action)
        
        
        
    def init_tab1(self):
        '''
        Adds controls and labels for tab1 
        and connects them to action handles
        '''
        # the main grid
        grid = QGridLayout() 
        
        '''
        Geometry settings
        '''
        group_box = QGroupBox("Geometry settings")
        vbox = QVBoxLayout()
        
        hbox = QHBoxLayout()
        vbox2 = QVBoxLayout()
        label = QLabel("Azimuth Pixel Spacing [m]")
        vbox2.addWidget(label)
        line = QLineEdit()
        line.setValidator(QDoubleValidator(1,100,1,self))
        line.textChanged.connect(self.set_azimuth_spacing)
        vbox2.addWidget(line)
        hbox.addLayout(vbox2)
        
        vbox2 = QVBoxLayout()
        label = QLabel("Range Pixel Spacing [m]")
        vbox2.addWidget(label)
        line = QLineEdit()
        line.setValidator(QDoubleValidator(1,100,1,self))
        line.textChanged.connect(self.set_range_spacing)
        vbox2.addWidget(line)
        hbox.addLayout(vbox2)
        vbox.addLayout(hbox)
        
        hbox = QHBoxLayout()
        label = QLabel("Azimuth Min [m]")
        hbox.addWidget(label)
        label = QLabel("Azimuth Max [m]")
        hbox.addWidget(label)
        vbox.addLayout(hbox)
        
        hbox = QHBoxLayout()
        line = QLineEdit()
        line.setValidator(QDoubleValidator(-1,100,1,self))
        line.textChanged.connect(self.set_azimuth_min)
        hbox.addWidget(line)
        line = QLineEdit()
        line.setValidator(QDoubleValidator(-1,100,1,self))
        line.textChanged.connect(self.set_azimuth_max)
        hbox.addWidget(line)
        vbox.addLayout(hbox)
        
        hbox = QHBoxLayout()
        label = QLabel("Range Min [m]")
        hbox.addWidget(label)
        label = QLabel("Range Max [m]")
        hbox.addWidget(label)
        vbox.addLayout(hbox)
        
        hbox = QHBoxLayout()
        line = QLineEdit()
        line.setValidator(QDoubleValidator(-1,100,1,self))
        line.textChanged.connect(self.set_range_min)
        hbox.addWidget(line)
        line = QLineEdit()
        line.setValidator(QDoubleValidator(-1,100,1,self))
        line.textChanged.connect(self.set_range_max)
        hbox.addWidget(line)
        vbox.addLayout(hbox)
        
        # adds coordinate controls to grid
        group_box.setLayout(vbox)  
        grid.addWidget(group_box, 0,0)
        grid.setColumnStretch(0, 1)
        
        hbox = QHBoxLayout()
        vbox2 = QVBoxLayout()
        label = QLabel("Azimuth resolution [m]")
        vbox2.addWidget(label)
        line = QLineEdit()
        line.setValidator(QDoubleValidator(-1,100,1,self))
        line.textChanged.connect(self.set_azimuth_res)
        vbox2.addWidget(line)
        hbox.addLayout(vbox2)
        vbox2 = QVBoxLayout()
        label = QLabel("Range resolution [m]")
        vbox2.addWidget(label)
        line = QLineEdit()
        line.setValidator(QDoubleValidator(-1,100,1,self))
        line.textChanged.connect(self.set_range_res)
        vbox2.addWidget(line)
        hbox.addLayout(vbox2) 
        vbox.addLayout(hbox)
        
        
        '''
        Simulation settings
        '''
        group_box = QGroupBox("Simulation settings")
        vbox = QVBoxLayout()
        # title of slider 1
        label = QLabel("Bounce level")
        vbox.addWidget(label)
        # horizontal box for slider and label
        hbox = QHBoxLayout()
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(1)
        slider.setMaximum(5)
        slider.setValue(5)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(1)
        label = QLabel()
        label.setMinimumWidth(25)
        label.setNum(slider.value())
        slider.valueChanged.connect(label.setNum)
        slider.valueChanged.connect(self.set_trace_level)  
        # add slider and label to vertical layout
        hbox.addWidget(slider)
        hbox.addWidget(label)
        vbox.addLayout(hbox)
        
        label = QLabel("dB clipping")
        vbox.addWidget(label)
        # horizontal box for slider and label
        hbox = QHBoxLayout()
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(9)
        slider.setMaximum(99)
        slider.setValue(55)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(9)
        label = QLabel()
        label.setMinimumWidth(25)
        label.setNum(slider.value())
        slider.valueChanged.connect(label.setNum)
        slider.valueChanged.connect(self.set_dBcliping)  
        # add slider and label to vertical layout
        hbox.addWidget(slider)
        hbox.addWidget(label)
        vbox.addLayout(hbox)

        # horizontal box for dial 1 and label
        hbox = QHBoxLayout()
        vbox2 = QVBoxLayout()
        dial = QDial()
        dial.setMinimum(0)
        dial.setMaximum(99)
        dial.setValue(0)
        dial.setNotchesVisible(True)
        dial.setFixedSize(100, 100)
        label = QLabel("Phase noise angle [1°]")
        vbox2.addStretch(1)
        vbox2.addWidget(label)
        label = QLabel()
        vbox2.addWidget(label)
        vbox2.addStretch(1)
        label.setNum(dial.value())
        dial.valueChanged.connect(label.setNum)
        dial.valueChanged.connect(self.set_noise_level)
        hbox.addWidget(dial)
        hbox.addLayout(vbox2) 
        vbox.addLayout(hbox)
             
        
        # adds coordinate controls to grid
        group_box.setLayout(vbox)  
        grid.addWidget(group_box, 1,0)
        grid.setColumnStretch(0, 1)
           
        '''
        start button
        '''
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.start_button = QPushButton("START", self)
        self.start_button.setCheckable(True)
        self.start_button.setStyleSheet("background-color : lightgreen")
        self.start_button.setFont(QFont('Times', 24))
        self.start_button.setFixedHeight(90)
        self.start_button.setFixedWidth(300)
        self.start_button.clicked.connect(self.start_progres)
        hbox.addStretch(1)
        hbox.addWidget(self.start_button)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        grid.addLayout(vbox, 1, 1)
          
        '''
        file paths
        '''
        group_box = QGroupBox("File Paths")
        vbox = QVBoxLayout()
        label = QLabel("Model file path:")
        vbox.addWidget(label)
        self.model_file_label = QLabel("Not set...")
        vbox.addWidget(self.model_file_label)    
        label = QLabel("Save file path:")
        vbox.addWidget(label)
        self.save_file_label = QLabel("Not set...")
        vbox.addWidget(self.save_file_label) 
        group_box.setLayout(vbox)  
        grid.addWidget(group_box, 0,1)
        grid.setColumnStretch(1, 2)
        
        '''
        progress bar
        '''
        self.pbar = QProgressBar()
        self.pbar.setValue(0)
        grid.addWidget(self.pbar, 2,0,1,2) 
        
        # finally adds everything to the tab1
        self.tab1.setLayout(grid)
        
        
    ###################### ACTION HANDELS #########################    
    
    def update_pbar(self, value):
        self.pbar.setValue(value)
    
    def new_file(self): 
        self.update_pbar(1)
        dir_path = QFileDialog.getOpenFileName(self,"Choose file to open")
        load_file_path = dir_path[0]
        self.app.load_contributions(load_file_path)
        self.model_file_label.setText(load_file_path)
        save_file_path = load_file_path.rsplit('/',1)[0]
        self.app.set_save_file(save_file_path)
        self.save_file_label.setText(save_file_path)
        self.update_pbar(100)
        
    def set_azimuth_spacing(self, value):
        self.app.set_azimuth_spacing(int(value))
        
    def set_range_spacing(self, value):
        self.app.set_range_spacing(int(value))
        
    def set_azimuth_min(self, value):
        self.app.set_azimuth_min(value)
    
    def set_azimuth_max(self, value):
        self.app.set_azimuth_max(value)
        
    def set_range_min(self, value):
        self.app.set_range_min(value)
    
    def set_range_max(self, value):
        self.app.set_range_max(value)
        
    def set_azimuth_res(self, value):
        self.app.set_azimuth_res(value)
        
    def set_range_res(self, value):
        self.app.set_range_res(value)
    
    def set_trace_level(self, value):
        self.app.set_trace_level(value)
    
    def set_dBcliping(self, value):
        self.app.set_dBcliping(value)
    
    def set_noise_level(self, value):
        self.app.set_noise_level(value)

        
        
    ###################### WORKER THREAD #############################    

    def start_progres(self):
        '''
        Starts working with the computing task
        in a new thread. Connected to start button states.
        '''
        if self.start_button.isChecked():
            self.start_button.setStyleSheet("background-color : red")
            self.start_button.setText("STOP")
            
            # Creates worker in a new thread for computing
            self.thread = QThread()
            self.worker = Worker(self)
            self.worker.moveToThread(self.thread)
            
            # Clean exit of thread and worker
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            
            # Connects resets
            self.worker.update_signal.connect(self.update_pbar)
            self.thread.finished.connect(
                lambda: self.start_button.setText("START")
            )
            self.thread.finished.connect(
                lambda: self.start_button.setStyleSheet("background-color : lightgreen")
            )
            self.thread.finished.connect(
                lambda: self.start_button.setChecked(False)
            )
            
            self.thread.start()
                  

'''
Worker does long running tasks after it has
been mowed to a new thread.
Update signal can be passed to task and
be used to control progress bar.
'''
class Worker(QObject):
    
    # signals to monitor working thread
    finished = pyqtSignal()
    update_signal = pyqtSignal(int)
    
    def __init__(self, gui):
        super().__init__()
        self.gui = gui

    def run(self):   
        self.gui.app.compute(self.update_signal)       
        self.finished.emit()



        