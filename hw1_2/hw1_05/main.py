import sys
from GUI import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from Q5_TrainClassifier import showCifar10, showMdlStructure, showAugmentation, showAccLoss, predict

imgPath = None

def loadImg():
    global imgPath
    imgPath = QFileDialog.getOpenFileName(directory="../")
    return

if __name__ == "__main__":
    # GUI window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # BtnClick
    ui.btn_loadImg.clicked.connect(loadImg)
    ui.btn_showImg.clicked.connect(showCifar10)
    ui.btn_showMdlStruc.clicked.connect(showMdlStructure)
    ui.btn_showDataAug.clicked.connect( lambda: showAugmentation(imgPath[0], ui.label) )
    ui.btn_showAccLoss.clicked.connect( lambda: showAccLoss(ui.label) )
    ui.btn_inference.clicked.connect( lambda: predict(imgPath[0], ui.label, ui.lbl_conf, ui.lbl_prediction) )

    # Show & Exit
    MainWindow.show()
    sys.exit(app.exec_())