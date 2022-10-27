import sys, os
from GUI import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from Q4_SIFT import keypoints, matchKeypoints

img1Path = None
img2Path = None

def loadImg1():
    global img1Path
    img1Path = QFileDialog.getOpenFileName(directory="../")
    return
    
def loadImg2():
    global img2Path
    img2Path = QFileDialog.getOpenFileName(directory="../")
    return

if __name__ == "__main__":
    # GUI window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # BtnClick
    ui.btn_loadImg1.clicked.connect(loadImg1)
    ui.btn_loadImg2.clicked.connect(loadImg2)
    ui.btn_keypts.clicked.connect( lambda: keypoints(img1Path[0]) )
    ui.btn_matchKeyPts.clicked.connect( lambda: matchKeypoints(img1Path[0], img2Path[0]) )

    # Show & Exit
    MainWindow.show()
    sys.exit(app.exec_())