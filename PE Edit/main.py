import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from datetime import date
from PE_CREATE_UI import *

class MainWindow(QMainWindow):

    def data_cat(self,rb):
        self.ui.PE_E_DC_STACK.setCurrentWidget(rb)
        self.ui.PE_E_DC_STACK.setMaximumSize(QtCore.QSize(16777215, 200))
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.PE_E_DC_STACK.setCurrentWidget(self.ui.PE_E_DC_NULL_PG)
        self.ui.PE_E_DC_STACK.setMaximumSize(QtCore.QSize(0, 0))
        self.ui.PE_E_M_4_W18_RB21.clicked.connect(lambda: self.data_cat(self.ui.PE_E_DC_EXIST_PG))
        self.ui.PE_E_M_4_W18_RB27.clicked.connect(lambda: self.data_cat(self.ui.PE_E_DC_NEW_PG))
        self.ui.PE_E_M_4_W18_RB33.clicked.connect(lambda: self.data_cat(self.ui.PE_E_DC_BOTH_PG))
        self.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())