import sys
import PyQt5.QtWidgets import *
import PyQt5.QtGui import *
import PyQt5.QtCore import *

class Cell(QWidget):
    def __init__(self):
        super().__init__()
        self.color = 'gray'
        self.life = False
        self.alive_round = 0

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCell(qp)
        qp.end()

    def drawCell(self, qp):
        pen = QColor(0, 0, 0)
        qp.setPen(pen)
        qp.setBrush(QColor(self.color))
        qp.drawRect(0, 0, 5, 5)

    def changeState(self):
        if self.life == False:
            self.life = True
            self.color = 'yellow'
        else:
            self.life = False
            self.color = 'gray'

        self.update()


class Table(QWidget):
    def __init__(self, width = 40, height = 80, random = False, duration = 0):
        super().__init__()
        self.width = width
        self.height = height
        self.layout = QGridLayout()
        self.setLayout(self.layout)

    def initTable(self):
        for x in range(len(self.width)):
            for y in range(len(self.height)):
                cell = Cell()
                self.layout.addWidget(cell, x, y)

if __name__ == "__main__":
    pass
