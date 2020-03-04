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
        self.setGeometry(100,100,500,500)
        self.title_label = QLabel("John Conway's Game Of Life")
        self.state_label = QLabel("Initial state : ")
        self.gene_label = QLabel("Generation : 0")
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")

        table = Table()

        self.layout_state = QHBoxLayout()
        self.layout_state.addWidget(self.state_label)
        self.layout_state.addWidget(self.gene_label)

        self.layout_button = QHBoxLayout()
        self.layout_button.addWidget(self.start_button)
        self.layout_button.addWidget(self.stop_button)

        self.layout_all = QVBoxLayout()
        self.layout_all.addWidget(self.title_label)
        self.layout_all.addLayout(self.layout_state)
        self.layout_all.addWidget(table)
        self.layout_all.addLayout(self.layout_button)

        self.setLayout(self.layout_all)
        self.show()

if __name__ == "__main__":
    pass
