import sys, os
from GUI import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from background import subtraction
from opticalFlow import process, trackVdo
from transform import perspective
from PCA import reconstructImg, computeError

imgPath = None
vdoPath = None
directory = None

def loadImg(lbl):
    global imgPath
    imgPath = QFileDialog.getOpenFileName(directory="./")
    lbl.setText("Image path is selected.")
    return

def loadVdo(lbl):
    global vdoPath
    vdoPath = QFileDialog.getOpenFileName(directory="./")
    lbl.setText("Video path is selected.")
    return

def loadDir(lbl):
    global directory
    folderPath = QFileDialog.getExistingDirectory(directory="./")
    directory = os.listdir(folderPath)
    lbl.setText("Folder is selected.")
    # dirContent = [fileName for fileName in dirContent if fileName[-4:] == ".bmp" or fileName[-4:] == ".jpg" or fileName[-4:] == ".png" or fileName[-4:] == ".pbm" or fileName[-4:] == ".pgm" or fileName[-4:] == ".ppm" or fileName[-4:] == ".pbm"]
    # dirContent.sort(key=lambda x: int(x[:-4]))
    return

if __name__ == "__main__":
    # GUI window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # BtnClick
    ui.btn_loadvdo.clicked.connect( lambda: loadVdo(ui.lbl_loadvdo) )
    ui.btn_loadImg.clicked.connect( lambda: loadImg(ui.lbl_loadimg) )
    ui.btn_loadfld.clicked.connect( lambda: loadDir(ui.lbl_loadfld) )
    ui.btn_bgsub.clicked.connect( lambda: subtraction(vdoPath[0], ui.lbl_loadvdo) )
    ui.btn_preprs.clicked.connect( lambda: process(vdoPath[0], ui.lbl_loadvdo) )
    ui.btn_trackvdo.clicked.connect( lambda: trackVdo(vdoPath[0], ui.lbl_loadvdo) )
    ui.btn_transfromppt.clicked.connect( lambda: perspective(vdoPath[0], imgPath[0], ui.lbl_loadvdo, ui.lbl_loadimg) )
    # ui.btn_rctimg.clicked.connect(  )
    # ui.btn_computeerr.clicked.connect(  )

    # Show & Exit
    MainWindow.show()
    sys.exit(app.exec_())