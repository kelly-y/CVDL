import sys, os
from GUI import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from Q1_CareraCalibration import CornerDectection, FindIntrinsic, FindExtrinsic, FindDistortion, ShowResult
from Q2_AugmentedReality import ShowOnBoard, ShowVertically
from Q3_StereoDisparityMap import StereoDisparityMap, CheckDisparityValue

folderPath = None
dirContent = None
dataL = None
dataR = None

def loadFolder():
    global folderPath, dirContent
    folderPath = QFileDialog.getExistingDirectory(directory="./")
    dirContent = os.listdir(folderPath)
    dirContent = [fileName for fileName in dirContent if fileName[-4:] == ".bmp" or fileName[-4:] == ".jpg" or fileName[-4:] == ".png" or fileName[-4:] == ".pbm" or fileName[-4:] == ".pgm" or fileName[-4:] == ".ppm" or fileName[-4:] == ".pbm"]
    dirContent.sort(key=lambda x: int(x[:-4]))
    return

def loadL():
    global dataL
    dataL = QFileDialog.getOpenFileName(directory="./")
    return

def loadR():
    global dataR
    dataR = QFileDialog.getOpenFileName(directory="./")
    return

if __name__ == "__main__":
    # GUI window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # BtnClick
    ui.btn_load_folder.clicked.connect(loadFolder)
    ui.btn_loadL.clicked.connect(loadL)
    ui.btn_loadR.clicked.connect(loadR)
    ui.btn_corner.clicked.connect( lambda: CornerDectection(folderPath, dirContent) )
    ui.btn_intrinsic.clicked.connect( lambda: FindIntrinsic (folderPath, dirContent) )
    ui.btn_extrinsic.clicked.connect( lambda: FindExtrinsic( ui.box_num_bmp.currentText(), folderPath, dirContent ) )
    ui.btn_distortion.clicked.connect( lambda: FindDistortion(folderPath, dirContent) )
    ui.btn_result1.clicked.connect( lambda: ShowResult(folderPath, dirContent) )
    ui.btn_show_board.clicked.connect( lambda: ShowOnBoard(ui.txt_2.text(), folderPath, dirContent) )
    ui.btn_show_vertical.clicked.connect( lambda: ShowVertically(ui.txt_2.text(), folderPath, dirContent) )
    ui.btn_show_disparity_map.clicked.connect( lambda: StereoDisparityMap(dataL[0], dataR[0]) )
    ui.btn_check_disparity_value.clicked.connect( lambda: CheckDisparityValue(dataL[0], dataR[0]) )

    # Show & Exit
    MainWindow.show()
    sys.exit(app.exec_())