import sys, time
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from REPORT_UI import Ui_MainWindow


class MainWindow(QMainWindow):
    def fill_table(self,table_lst,row,r):
        flag=0
        for table in table_lst:
            for n in range(table.columnCount()):
                # print(row[n])
                #print(r)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(row[flag+n])
                # if row[flag+n]=='Y':
                #     item.setBackground(QtGui.QColor(170,255,127))
                # elif row[flag+n]=='N':
                #     item.setBackground(QtGui.QColor(255, 184, 184))
                table.setItem(r, n, item)
                # item = QtWidgets.QTableWidgetItem()
                # item.setTextAlignment(QtCore.Qt.AlignCenter)
                # item.setText(row[4 + n])
                # self.ui.RPRT_TBL_2.setItem(r, n, item)
            flag=flag+table.columnCount()

    def add_data(self):

        data= [['DG-0001', '1234', '98', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y']
         ,['DG-0002', '3456', '7654', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N']
         ,['DG-0003', '5678', '15210', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y']
         ,['DG-0004', '7900', '22766', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N']
         ,['DG-0005', '10122', '30322', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y']
         ,['DG-0006', '12344', '37878', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N']
         ,['DG-0007', '14566', '45434', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y']
         ,['DG-0008', '16788', '52990', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N']
         ,['DG-0009', '19010', '60546', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y']
         ,['DG-0010', '21232', '68102', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N']]

        print(data[0][:3])
        no_of_rows=len(data)
        self.ui.RPRT_TBL_1.setRowCount(no_of_rows)
        self.ui.RPRT_TBL_2.setRowCount(no_of_rows)
        self.ui.RPRT_TBL_3.setRowCount(no_of_rows)
        self.ui.RPRT_TBL_4.setRowCount(no_of_rows)
        table_lst=[self.ui.RPRT_TBL_1, self.ui.RPRT_TBL_2, self.ui.RPRT_TBL_3,self.ui.RPRT_TBL_4]

        r=0
        for row in data:
            self.fill_table(table_lst,row,r)
            r+=1


    def set_100(self,table,column_cnt):
        for table_wid,column in zip(table,column_cnt):
            for i in range(column):
                #print(i)
                # print(table_wid.horizontalHeaderItem(i).data(0))
                # print(len(table_wid.horizontalHeaderItem(i).data(0)))
                table_wid.setColumnWidth(i,100)




    def set_column(self):
        self.set_100([ self.ui.RPRT_TBL_2, self.ui.RPRT_TBL_3, self.ui.RPRT_TBL_4],
                         [3, 5, 5])
        self.ui.RPRT_TBL_2.setFixedWidth(300)
        self.ui.RPRT_TBL_3.setFixedWidth(500)
        self.ui.RPRT_TBL_4.setFixedWidth(500)
        self.ui.RPRT_TBL_1.setMinimumSize(400,0)
        header = self.ui.RPRT_TBL_1.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.ui.RPRT_TBL_1.setAlternatingRowColors(True)
        self.ui.RPRT_TBL_2.setAlternatingRowColors(True)
        self.ui.RPRT_TBL_3.setAlternatingRowColors(True)
        self.ui.RPRT_TBL_4.setAlternatingRowColors(True)

    def move_other_scrollbars(self,idx, bar):
        scrollbars = {tbl.verticalScrollBar() for tbl in self.list_of_tables}
        scrollbars.remove(bar)
        for bar in scrollbars:
            bar.setValue(idx)
    def sync_scroll(self):
        for tbl in self.list_of_tables:
            tbl.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            tbl.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scrollbar = tbl.verticalScrollBar()
            scrollbar.valueChanged.connect(lambda idx, bar=scrollbar: self.move_other_scrollbars(idx, bar))
    def data_center(self):
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)

        self.ui.RPRT_TBL_1.setItem(0, 0, item)

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.RPRT_TBL_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.RPRT_TBL_1.verticalHeader().hide()
        self.ui.RPRT_TBL_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.RPRT_TBL_2.verticalHeader().hide()
        self.ui.RPRT_TBL_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.RPRT_TBL_3.adjustSize()
        print(self.ui.RPRT_TBL_1.columnCount())
        self.ui.RPRT_TBL_3.verticalHeader().hide()
        self.ui.RPRT_TBL_4.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.RPRT_TBL_4.verticalHeader().hide()
        #self.data_center()
        self.set_column()
        self.add_data()
        self.list_of_tables = [self.ui.RPRT_TBL_1, self.ui.RPRT_TBL_2, self.ui.RPRT_TBL_3,self.ui.RPRT_TBL_4]
        self.sync_scroll()




            #self.layout.addWidget(tbl)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())