# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bhavatoshr\Desktop\DGT\REPORT_TAB.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 295)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.report_main = QtWidgets.QWidget(self.centralwidget)
        self.report_main.setObjectName("report_main")
        self.report_main_GL = QtWidgets.QGridLayout(self.report_main)
        self.report_main_GL.setHorizontalSpacing(0)
        self.report_main_GL.setObjectName("report_main_GL")
        self.RPRT_F_3 = QtWidgets.QFrame(self.report_main)
        self.RPRT_F_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RPRT_F_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RPRT_F_3.setObjectName("RPRT_F_3")
        self.RPRT_F_3_GL = QtWidgets.QGridLayout(self.RPRT_F_3)
        self.RPRT_F_3_GL.setObjectName("RPRT_F_3_GL")
        self.RPRT_F_3_L = QtWidgets.QLabel(self.RPRT_F_3)
        self.RPRT_F_3_L.setObjectName("RPRT_F_3_L")
        self.RPRT_F_3_GL.addWidget(self.RPRT_F_3_L, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.report_main_GL.addWidget(self.RPRT_F_3, 1, 1, 1, 1)
        self.RPRT_F_5 = QtWidgets.QFrame(self.report_main)
        self.RPRT_F_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RPRT_F_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RPRT_F_5.setObjectName("RPRT_F_5")
        self.report_main_GL.addWidget(self.RPRT_F_5, 1, 0, 1, 1)
        self.RPRT_TBL_1 = QtWidgets.QTableWidget(self.report_main)
        self.RPRT_TBL_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.RPRT_TBL_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RPRT_TBL_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)

        self.RPRT_TBL_1.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.RPRT_TBL_1.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.RPRT_TBL_1.setGridStyle(QtCore.Qt.DashLine)
        self.RPRT_TBL_1.setWordWrap(True)
        self.RPRT_TBL_1.setCornerButtonEnabled(True)
        #self.RPRT_TBL_1.setRowCount(10)
        self.RPRT_TBL_1.setObjectName("RPRT_TBL_1")
        self.RPRT_TBL_1.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.RPRT_TBL_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        self.RPRT_TBL_1.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_1.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_1.setItem(0, 2, item)
        self.RPRT_TBL_1.horizontalHeader().setSortIndicatorShown(False)
        self.RPRT_TBL_1.horizontalHeader().setStretchLastSection(False)
        self.RPRT_TBL_1.verticalHeader().setSortIndicatorShown(False)
        self.RPRT_TBL_1.verticalHeader().setStretchLastSection(False)
        self.report_main_GL.addWidget(self.RPRT_TBL_1, 2, 0, 1, 1)
        self.RPRT_F_4 = QtWidgets.QFrame(self.report_main)
        self.RPRT_F_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RPRT_F_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RPRT_F_4.setObjectName("RPRT_F_4")
        self.RPRT_F_4_GL = QtWidgets.QGridLayout(self.RPRT_F_4)
        self.RPRT_F_4_GL.setObjectName("RPRT_F_4_GL")
        self.RPRT_F_4_L = QtWidgets.QLabel(self.RPRT_F_4)
        self.RPRT_F_4_L.setObjectName("RPRT_F_4_L")
        self.RPRT_F_4_GL.addWidget(self.RPRT_F_4_L, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.report_main_GL.addWidget(self.RPRT_F_4, 1, 4, 1, 2)
        self.RPRT_F_2 = QtWidgets.QFrame(self.report_main)
        self.RPRT_F_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RPRT_F_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RPRT_F_2.setObjectName("RPRT_F_2")
        self.RPRT_F_2_GL = QtWidgets.QGridLayout(self.RPRT_F_2)
        self.RPRT_F_2_GL.setObjectName("RPRT_F_2_GL")
        self.RPRT_F_2_L = QtWidgets.QLabel(self.RPRT_F_2)
        self.RPRT_F_2_L.setObjectName("RPRT_F_2_L")
        self.RPRT_F_2_GL.addWidget(self.RPRT_F_2_L, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.report_main_GL.addWidget(self.RPRT_F_2, 1, 2, 1, 2)
        self.RPRT_TBL_4 = QtWidgets.QTableWidget(self.report_main)
        #self.RPRT_TBL_4.setRowCount(10)
        self.RPRT_TBL_4.setObjectName("RPRT_TBL_4")
        self.RPRT_TBL_4.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_4.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_4.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_4.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_4.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_4.setItem(0, 4, item)
        self.report_main_GL.addWidget(self.RPRT_TBL_4, 2, 4, 1, 1)
        self.RPRT_TBL_3 = QtWidgets.QTableWidget(self.report_main)
        #self.RPRT_TBL_3.setRowCount(10)
        self.RPRT_TBL_3.setObjectName("RPRT_TBL_3")
        self.RPRT_TBL_3.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_3.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_3.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_3.setItem(0, 4, item)
        self.report_main_GL.addWidget(self.RPRT_TBL_3, 2, 2, 1, 1)
        self.RPRT_TBL_2 = QtWidgets.QTableWidget(self.report_main)
        self.RPRT_TBL_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        #self.RPRT_TBL_2.setRowCount(10)
        self.RPRT_TBL_2.setObjectName("RPRT_TBL_2")
        self.RPRT_TBL_2.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RPRT_TBL_2.setItem(0, 2, item)
        self.report_main_GL.addWidget(self.RPRT_TBL_2, 2, 1, 1, 1)
        self.RPRT_F_1 = QtWidgets.QFrame(self.report_main)
        self.RPRT_F_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RPRT_F_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RPRT_F_1.setObjectName("RPRT_F_1")
        self.RPRT_F_1_GL = QtWidgets.QGridLayout(self.RPRT_F_1)
        self.RPRT_F_1_GL.setContentsMargins(-1, -1, -1, 10)
        self.RPRT_F_1_GL.setObjectName("RPRT_F_1_GL")
        self.RPRT_F_1_L = QtWidgets.QLabel(self.RPRT_F_1)
        self.RPRT_F_1_L.setObjectName("RPRT_F_1_L")
        self.RPRT_F_1_GL.addWidget(self.RPRT_F_1_L, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.report_main_GL.addWidget(self.RPRT_F_1, 0, 0, 1, 5)
        self.verticalLayout.addWidget(self.report_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RPRT_F_3_L.setText(_translate("MainWindow", "Concept Validation"))
        item = self.RPRT_TBL_1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "GNA CV ID"))
        item = self.RPRT_TBL_1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Jira ID"))
        item = self.RPRT_TBL_1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PMO CV"))
        __sortingEnabled = self.RPRT_TBL_1.isSortingEnabled()
        self.RPRT_TBL_1.setSortingEnabled(False)
        self.RPRT_TBL_1.setSortingEnabled(__sortingEnabled)
        self.RPRT_F_4_L.setText(_translate("MainWindow", "Planning Execution"))
        self.RPRT_F_2_L.setText(_translate("MainWindow", "Program Development"))
        item = self.RPRT_TBL_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "IO APP"))
        item = self.RPRT_TBL_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "GNA APP"))
        item = self.RPRT_TBL_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CF Team"))
        item = self.RPRT_TBL_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "BT APP"))
        item = self.RPRT_TBL_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "BT DNA "))
        __sortingEnabled = self.RPRT_TBL_4.isSortingEnabled()
        self.RPRT_TBL_4.setSortingEnabled(False)
        self.RPRT_TBL_4.setSortingEnabled(__sortingEnabled)
        item = self.RPRT_TBL_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "IO APP"))
        item = self.RPRT_TBL_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "GNA APP"))
        item = self.RPRT_TBL_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CF Team"))
        item = self.RPRT_TBL_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "BT APP"))
        item = self.RPRT_TBL_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "BT DNA APP"))
        __sortingEnabled = self.RPRT_TBL_3.isSortingEnabled()
        self.RPRT_TBL_3.setSortingEnabled(False)
        self.RPRT_TBL_3.setSortingEnabled(__sortingEnabled)
        item = self.RPRT_TBL_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "IO App"))
        item = self.RPRT_TBL_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "GNA App"))
        item = self.RPRT_TBL_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "GNA Ack DI"))
        __sortingEnabled = self.RPRT_TBL_2.isSortingEnabled()
        self.RPRT_TBL_2.setSortingEnabled(False)
        self.RPRT_TBL_2.setSortingEnabled(__sortingEnabled)
        self.RPRT_F_1_L.setText(_translate("MainWindow", "DG Initiative status"))