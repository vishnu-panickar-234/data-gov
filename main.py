import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from Create_final import Ui_MainWindow
from datetime import date
from edit_popup import popup


class MainWindow(QMainWindow):

    def mandatory_pop(self):
        mandatory = QMessageBox()
        mandatory.setWindowTitle("Alert")
        mandatory.setText("Please Fill The Mandatory Fields")
        mandatory.exec_()
    def data_clear(self,radio_buttons):

        for button in radio_buttons:
            button[1].setAutoExclusive(False)
            button[1].setChecked(False)
            button[1].setAutoExclusive(True)
            button[2].setAutoExclusive(False)
            button[2].setChecked(False)
            button[2].setAutoExclusive(True)




    def data_insert(self,text,button,date,extra_fields,radio_buttons):
        gna_cv_id=str(self.ui.CV_C_M_1_W5_LE4.text())
        gna_id=int(gna_cv_id[-4:])
        insert_lst_1=text+date+button+extra_fields
        Update_Date= "CURRENT_TIMESTAMP"
        delete_flg='N'
        user_id='vpanic1'
        print(date)
        insert_lst_1.append(Update_Date)
        insert_lst_1.append(delete_flg)
        insert_lst_1.append(user_id)
        insert_lst_final=[gna_id,gna_cv_id]
        insert_lst_final.extend(insert_lst_1)
        print(insert_lst_final)
        self.data_clear(radio_buttons)




    def button_input(self, radio_buttons):

        user_data = []
        mand_flag = 0
        for data in radio_buttons:
            if data[1].isChecked():
                user_data.append(data[1].text())
                data[0].setStyleSheet("color: rgb(0, 0, 0);")
            elif data[2].isChecked():
                user_data.append(data[2].text())
                data[0].setStyleSheet("color: rgb(0, 0, 0);")
            else:
                if data[3] == 1:
                    data[0].setStyleSheet("color: rgb(255, 0, 4);")
                    mand_flag = 1
                else:
                    user_data.append("blank")
        if mand_flag:
            return 1
        else:
            return user_data

    def text_input(self, text_fields):
        input_data = []
        mand_flag = 0
        for data in text_fields:

            if data[2] == 0 or data[0].text():
                data[1].setStyleSheet("color: rgb(0, 0, 0);")
                input_data.append(data[0].text())

            else:

                data[1].setStyleSheet("color: rgb(255, 0, 4);")
                mand_flag = 1
        if mand_flag == 1:
            return 1
        else:
            return input_data

    def date_input(self,date_fields):
        date_data=[]
        mand_flag=0
        for date in date_fields:
            if date[2] == 0 or date[0].date():
                date[1].setStyleSheet("color: rgb(0, 0, 0);")
                date_data.append(str(date[0].date().toPyDate()))
            else:
                date[1].setStyleSheet("color: rgb(255, 0, 4);")
                mand_flag = 1
            if mand_flag == 1:
                return 1
            else:
                return date_data
    def extra_fields(self):
        CV_description=self.ui.CV_C_M_1_W3_PTE.toPlainText()
        NI_MISC=self.ui.CV_C_M_3_W11_PTE2.toPlainText()
        #DG_EXIST_NEW_B
        if self.ui.CV_C_M_4_W18_RB21.isChecked():
            DG_EXIST_NEW_B=self.ui.CV_C_M_4_W18_RB21.text()
        elif self.ui.CV_C_M_4_W18_RB27.isChecked():
            DG_EXIST_NEW_B=self.ui.CV_C_M_4_W18_RB27.text()
        elif self.ui.CV_C_M_4_W18_RB33.isChecked():
            DG_EXIST_NEW_B=self.ui.CV_C_M_4_W18_RB33.text()
        else:
            DG_EXIST_NEW_B="blank"
        end_list=[CV_description,NI_MISC,DG_EXIST_NEW_B]
        return end_list


    def set_gnaCV_id(self):
        query_result = 1
        GNA_CV_ID = "DG-" + str(query_result).zfill(4)
        self.ui.CV_C_M_1_W5_LE4.setText(GNA_CV_ID)
        self.ui.CV_C_M_1_W5_LE4.setReadOnly(True)

    def set_date(self, date_field):
        for data in date_field:
            data.setCalendarPopup(True)
            data.calendarWidget().setSelectedDate(QtCore.QDate.currentDate())
            #print(str(data.date().toPyDate()))

    def take_input(self):
        text_fields = [
                       [self.ui.CV_C_M_1_W5_LE6, self.ui.CV_C_M_1_W5_L3, 1],
                       [self.ui.CV_C_M_1_W5_LE7, self.ui.CV_C_M_1_W5_L4, 1],
                       [self.ui.CV_C_M_1_W5_LE9, self.ui.CV_C_M_1_W5_L6, 0],
                       [self.ui.CV_C_M_1_W4_LE5, self.ui.CV_C_M_1_W4_L2, 0],
                       [self.ui.CV_C_M_1_W4_LE10, self.ui.CV_C_M_1_W4_L7, 0],
                       [self.ui.CV_C_M_1_W4_LE11, self.ui.CV_C_M_1_W4_L8, 0],
                       [self.ui.CV_C_M_1_W2_LE14, self.ui.CV_C_M_1_W2_L12, 0],
                       [self.ui.CV_C_M_1_W2_LE16, self.ui.CV_C_M_1_W2_L14, 0],
                       [self.ui.CV_C_M_1_W2_LE15, self.ui.CV_C_M_1_W2_L13, 0],
                       [self.ui.CV_C_M_1_W2_LE17, self.ui.CV_C_M_1_W2_L15, 0]]

        date_fields=[[self.ui.CV_C_M_1_W5_LE8, self.ui.CV_C_M_1_W5_L5, 1],
                     [self.ui.CV_C_M_1_W4_LE12, self.ui.CV_C_M_1_W4_L9, 0],
                     [self.ui.CV_C_M_1_W4_LE13, self.ui.CV_C_M_1_W4_L1, 0],]

        radio_buttons = [[self.ui.CV_C_M_1_W2_L16, self.ui.CV_C_M_1_W2_RB2, self.ui.CV_C_M_1_W2_RB, 0],
                         [self.ui.CV_C_M_2_W6_L17, self.ui.CV_C_M_2_W7_RB4, self.ui.CV_C_M_2_W7_RB3, 0],
                         [self.ui.CV_C_M_2_W6_L18, self.ui.CV_C_M_2_W8_RB5, self.ui.CV_C_M_2_W8_RB6, 0],
                         [self.ui.CV_C_M_2_W6_L19, self.ui.CV_C_M_2_W9_RB7, self.ui.CV_C_M_2_W9_RB8, 0],
                         [self.ui.CV_C_M_2_W6_L20, self.ui.CV_C_M_2_W10_RB9, self.ui.CV_C_M_2_W10_RB10, 0],
                         [self.ui.CV_C_M_3_W11_L22, self.ui.CV_C_M_3_W12_RB11, self.ui.CV_C_M_3_W12_RB12, 0],
                         [self.ui.CV_C_M_3_W11_L23, self.ui.CV_C_M_3_W13_RB13, self.ui.CV_C_M_3_W13_RB14, 0],
                         [self.ui.CV_C_M_3_W11_L24, self.ui.CV_C_M_3_W14_RB15, self.ui.CV_C_M_3_W14_RB16, 0],
                         #[self.ui.CV_C_M_4_W15_L30, self.ui.CV_C_M_4_W18_RB22, self.ui.CV_C_M_4_W18_RB28, 0],
                         [self.ui.CV_C_M_4_W15_L32, self.ui.CV_C_M_4_W18_RB23, self.ui.CV_C_M_4_W18_RB29, 0],
                         [self.ui.CV_C_M_4_W15_L33, self.ui.CV_C_M_4_W18_RB24, self.ui.CV_C_M_4_W18_RB30, 0],
                         [self.ui.CV_C_M_4_W15_L34, self.ui.CV_C_M_4_W18_RB25, self.ui.CV_C_M_4_W18_RB31, 0],
                         [self.ui.CV_C_M_4_W15_L35, self.ui.CV_C_M_4_W18_RB26, self.ui.CV_C_M_4_W18_RB32, 0],
                         [self.ui.CV_C_M_4_W16_L38, self.ui.CV_C_M_4_W17_RB33, self.ui.CV_C_M_4_W17_RB36, 0],
                         [self.ui.CV_C_M_4_W16_L39, self.ui.CV_C_M_4_W17_RB35, self.ui.CV_C_M_4_W17_RB37, 0],
                         [self.ui.CV_C_M_4_W16_L40, self.ui.CV_C_M_4_W17_RB34, self.ui.CV_C_M_4_W17_RB38, 0],
                         [self.ui.CV_C_M_4_W16_L47, self.ui.CV_C_M_4_W17_RB41, self.ui.CV_C_M_4_W17_RB42, 0],
                         [self.ui.CV_C_M_4_W19_L42, self.ui.CV_C_M_4_W22_RB53, self.ui.CV_C_M_4_W22_RB54, 0],
                         [self.ui.CV_C_M_4_W19_L43, self.ui.CV_C_M_4_W22_RB43, self.ui.CV_C_M_4_W22_RB48, 0],
                         [self.ui.CV_C_M_4_W19_L44, self.ui.CV_C_M_4_W22_RB44, self.ui.CV_C_M_4_W22_RB49, 0],
                         [self.ui.CV_C_M_4_W19_L45, self.ui.CV_C_M_4_W22_RB45, self.ui.CV_C_M_4_W22_RB50, 0],
                         [self.ui.CV_C_M_4_W19_L46, self.ui.CV_C_M_4_W22_RB47, self.ui.CV_C_M_4_W22_RB51, 0],
                         [self.ui.CV_C_M_4_W19_L47, self.ui.CV_C_M_4_W22_RB46, self.ui.CV_C_M_4_W22_RB52, 0],
                         [self.ui.CV_C_M_4_W20_L48, self.ui.CV_C_M_4_W23_RB39, self.ui.CV_C_M_4_W23_RB60, 0],
                         [self.ui.CV_C_M_4_W20_L49, self.ui.CV_C_M_4_W23_RB53, self.ui.CV_C_M_4_W23_RB61, 0],
                         [self.ui.CV_C_M_4_W20_L50, self.ui.CV_C_M_4_W23_RB54, self.ui.CV_C_M_4_W23_RB62, 0],
                         [self.ui.CV_C_M_4_W20_L51, self.ui.CV_C_M_4_W23_RB55, self.ui.CV_C_M_4_W23_RB63, 0],
                         [self.ui.CV_C_M_4_W20_L52, self.ui.CV_C_M_4_W23_RB56, self.ui.CV_C_M_4_W23_RB64, 0],
                         [self.ui.CV_C_M_4_W20_L53, self.ui.CV_C_M_4_W23_RB57, self.ui.CV_C_M_4_W23_RB65, 0],
                         [self.ui.CV_C_M_4_W20_L54, self.ui.CV_C_M_4_W23_RB58, self.ui.CV_C_M_4_W23_RB66, 0],
                         [self.ui.CV_C_M_4_W20_L55, self.ui.CV_C_M_4_W23_RB59, self.ui.CV_C_M_4_W23_RB67, 0],
                         [self.ui.CV_C_M_4_W20_L56, self.ui.CV_C_M_4_W23_RB68, self.ui.CV_C_M_4_W23_RB69, 0],
                         [self.ui.CV_C_M_4_W21_L57, self.ui.CV_C_M_4_W24_RB40, self.ui.CV_C_M_4_W24_RB68, 0],
                         [self.ui.CV_C_M_4_W21_L58, self.ui.CV_C_M_4_W24_RB69, self.ui.CV_C_M_4_W24_RB70, 0]
                         ]
        mand_text = self.text_input(text_fields)
        mand_button = self.button_input(radio_buttons)
        mand_date = self.date_input(date_fields)
        extra_fields = self.extra_fields()

        if mand_text == 1 or mand_button == 1 or mand_date==1:
            self.mandatory_pop()
        else:
            self.data_insert(mand_text,mand_button,mand_date,extra_fields,radio_buttons)

    def test(self):

        self.ui.CV_C_DC_STACK.setCurrentWidget(self.ui.CV_C_DC_EXIST_PG)
        self.ui.CV_C_DC_STACK.setMaximumSize(QtCore.QSize(16777215, 200))

    def test1(self):

        self.ui.CV_C_DC_STACK.setCurrentWidget(self.ui.CV_C_DC_NEW_PG)
        self.ui.CV_C_DC_STACK.setMaximumSize(QtCore.QSize(16777215, 200))

    def test2(self):

        self.ui.CV_C_DC_STACK.setCurrentWidget(self.ui.CV_C_DC_BOTH_PG)
        self.ui.CV_C_DC_STACK.setMaximumSize(QtCore.QSize(16777215, 500))
        self.ui.CV_C_DC_BOTH_PG.setMaximumSize(QtCore.QSize(16777215, 500))

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_gnaCV_id()
        self.set_date([self.ui.CV_C_M_1_W4_LE12, self.ui.CV_C_M_1_W4_LE13,self.ui.CV_C_M_1_W5_LE8])
        self.ui.CV_C_SUBMIT_B.clicked.connect(self.take_input)
        self.ui.CV_C_DC_STACK.setCurrentWidget(self.ui.CV_C_DC_NULL_PG)
        self.ui.CV_C_DC_STACK.setMaximumSize(QtCore.QSize(0, 0))
        self.ui.CV_C_M_4_W18_RB21.clicked.connect(self.test)
        self.ui.CV_C_M_4_W18_RB27.clicked.connect(self.test1)
        self.ui.CV_C_M_4_W18_RB33.clicked.connect(self.test2)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
