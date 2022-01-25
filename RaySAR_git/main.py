'''
Created on 13 Dec 2021

@author: rasmus
'''




import sys
from PyQt5.QtWidgets import QApplication
from gui import GUI



def main():
        
    # Use global to prevent crashing on exit
    global qapp
    qapp = QApplication(sys.argv)
    gui = GUI()

    # Start the Qt event loop end exit after it stops
    sys.exit(qapp.exec_())
    
    
if __name__ == '__main__':
    main()