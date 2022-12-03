import sys
from GUI import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from Q5_resnet50 import showImages, showDistribution, showMdlStructure, showCamparison, inference

imgPath = None

def loadImg():
    global imgPath
    imgPath = QFileDialog.getOpenFileName(directory="./")
    return

if __name__ == "__main__":
    # GUI window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # BtnClick
    ui.btn_loadImg.clicked.connect( loadImg )
    ui.btn_showImg.clicked.connect( showImages )
    ui.btn_showDtrb.clicked.connect( showDistribution )
    ui.btn_showMdlStruc.clicked.connect( showMdlStructure )
    # ui.btn_showCompare.clicked.connect(  )
    ui.btn_inference.clicked.connect( lambda: inference(imgPath[0], ui.label, ui.lbl_prediction) )

    # Show & Exit
    MainWindow.show()
    sys.exit(app.exec_())