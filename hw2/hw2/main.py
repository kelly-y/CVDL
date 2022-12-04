import sys, os
from GUI import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from Q1_background import subtraction
from Q2_opticalFlow import process, trackVdo
from Q3_transform import perspective
from Q4_PCA import reconstructImg, computeError

imgPath = None
vdoPath = None
fldPath = None
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
    global fldPath, directory
    fldPath = QFileDialog.getExistingDirectory(directory="./")
    directory = os.listdir(fldPath)
    lbl.setText("Folder is selected and loaded.")
    directory = [fileName for fileName in directory if fileName[-4:] == ".bmp" or fileName[-4:] == ".jpg" or fileName[-4:] == ".png" or fileName[-4:] == ".pbm" or fileName[-4:] == ".pgm" or fileName[-4:] == ".ppm" or fileName[-4:] == ".pbm"]
    directory.sort(key=lambda x: int(x[8:-5]))
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
    ui.btn_rctimg.clicked.connect( lambda: reconstructImg(fldPath, directory) )
    ui.btn_computeerr.clicked.connect( lambda: computeError(fldPath, directory) )

    # Show & Exit
    MainWindow.show()
    sys.exit(app.exec_())