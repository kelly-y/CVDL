import sys
from GUI import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap

from Q5_resnet50 import showImages, showDistribution, showMdlStructure, showCamparison, inference

imgPath = None

def loadImg(picLbl):
    global imgPath
    imgPath = QFileDialog.getOpenFileName(directory="./")

    # Show image
    pixmap = QPixmap(imgPath[0])
    pixmap = pixmap.scaled(224, 224, aspectRatioMode=Qt.IgnoreAspectRatio)
    picLbl.setPixmap(pixmap)

    return

if __name__ == "__main__":
    # GUI window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # BtnClick
    ui.btn_loadImg.clicked.connect( lambda: loadImg(ui.label) )
    ui.btn_showImg.clicked.connect( showImages )
    ui.btn_showDtrb.clicked.connect( showDistribution )
    ui.btn_showMdlStruc.clicked.connect( showMdlStructure )
    ui.btn_showCompare.clicked.connect( showCamparison )
    ui.btn_inference.clicked.connect( lambda: inference(imgPath[0], ui.lbl_prediction) )

    # Show & Exit
    MainWindow.show()
    sys.exit(app.exec_())