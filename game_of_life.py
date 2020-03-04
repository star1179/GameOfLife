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
    def __init__(self, width = 80, height = 40, random = False, duration = 0):
        super().__init__()
        self.table_width = width
        self.table_height = height
        self.layout = QGridLayout()
        self.setLayout(self.layout)

    def initTable(self):
        for x in range(self.table_width):
            for y in range(self.table_height):
                cell = Cell()
                self.layout.addWidget(cell, x, y)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("John Conway's Game Of Life")
        self.control_button = QPushButton("Start")
        self.state_button = QPushButton("generation : 0")
        self.state_button.setFlat(True)

        table = Table()

        self.setGeometry(100, 100, table.table_width*10, table.table_height*10)
        self.layout_bottom = QHBoxLayout()
        self.layout_bottom.addWidget(self.control_button)
        self.layout_bottom.addWidget(self.state_button)

        self.layout_all = QVBoxLayout()
        self.layout_all.addWidget(table)
        self.layout_all.addLayout(self.layout_bottom)

        self.setLayout(self.layout_all)
        self.show()

if __name__ == "__main__":
    pass
