import sys
from tkinter import * 
from tkinter.ttk import * 
from time import strftime 
import pyqtgraph as pg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QPushButton,QGraphicsGridLayout
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLabel, QTabWidget, QGridLayout, QVBoxLayout, \
QHBoxLayout, QSizePolicy, QSpacerItem, QStyle, QStyleFactory, QPushButton, QFrame, QFontDialog, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5 import QtGui

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("untitled.ui",self) 
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.graphicsView.setBackground(QtGui.QColor("white"))
        self.Button.clicked.connect(self.rezolva)
        self.Button.clicked.connect(self.DisplayGraph)
        self.graphicsView.getAxis('left').setPen('black')
        self.graphicsView.getAxis('left').setTextPen('black')
        self.graphicsView.getAxis('right').setPen('black')
        self.graphicsView.getAxis('right').setTextPen('black')
        self.graphicsView.getAxis('top').setPen('black')
        self.graphicsView.getAxis('top').setTextPen('black')
        self.graphicsView.getAxis('bottom').setTextPen('black')
        self.graphicsView.getAxis('bottom').setPen('black')
        self.graphicsView.setLabel("left", "Imaginar")
        self.graphicsView.setLabel("bottom", "Real")
        self.graphicsView.showGrid(x=True, y=True)
    def rezolva(self):
        try:
            a =self.lineEdita.text()
            print(a,end=' ')
            try:
                b =self.lineEditb.text()
                print(b,end=' ')
                try:
                    c =self.lineEditc.text()
                    print(c,end=' ')
                    try:
                        d =self.lineEditd.text()
                        print(d,end=' ')
                    except ValueError:
                        print("Trebuie sa introduceti un numar")
                except ValueError:
                    print("Trebuie sa introduceti un numar")
            except ValueError:
                print("Trebuie sa introduceti un numar")
        except ValueError:
            print("Trebuie sa introduceti un numar")
        A=float(a)
        B=float(b)
        C=float(c)
        D=float(d)
        Delta=(B**2)*(C**2)-4*A*C**3-4*(B**3)*D-27*(A**2)*D**2+18*A*B*C*D
        if Delta>0:
            self.label_2.setText("ecuatia are 3 radacini reale")
        elif Delta<0:
            self.label_2.setText("ecuatia are o radacina reala si 2 complexe")
        coef=[a,b,c,d]
        a=np.roots(coef)
        x1=str(a[0])
        x2=str(a[1])
        x3=str(a[2])
        print(x1,x2,x3)
        self.label.setText(x1)
        self.label2_2.setText(x2)
        self.label3_2.setText(x3)
    def DisplayGraph(self):
        self.graphicsView.clear()
        a1=complex(window.label.text())
        a2=complex(window.label2_2.text())
        a3=complex(window.label3_2.text())
        pen=pg.mkPen(color='r',width=-100)
        pen1=pg.mkPen(color='r',width=3)
        pen2=pg.mkPen(color='b',width=3)
        pen3=pg.mkPen(color='g',width=3)
        real=[a1.real,a2.real,a3.real]
        imaginar=[a1.imag,a2.imag,a3.imag]
        self.graphicsView.plot(
            real,
            imaginar,
            pen=pen,
            symbol="o",
            symbolSize=10,
            symbolBrush="k",
)
        self.graphicsView.plot([0,a1.real],[0,a1.imag],pen=pen1)
        self.graphicsView.plot([0,a2.real],[0,a2.imag],pen=pen2)
        self.graphicsView.plot([0,a3.real],[0,a3.imag],pen=pen3)

        


if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    window = Main()
    window.resize
    window.show()
    app.exec_()
    
