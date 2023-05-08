def setFrame(self):
frame_lst=[self.ui.CV_C_M_1,self.ui.CV_C_M_2,self.ui.CV_C_M_3,self.ui.CV_C_M_4]
#self.ui.CV_C_M_4_W15,self.ui.CV_C_M_4_W16,self.ui.CV_C_M_4_W19,self.ui.CV_C_M_4_W20,self.ui.CV_C_M_4_W21,self.ui.CV_C_M_4_W26]
for frame in frame_lst:
frame.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
frame.setLineWidth(0)
