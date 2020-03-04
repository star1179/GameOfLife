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

    def initTable(self, randomState):
        for y in range(self.table_height):
            for x in range(self.table_width):
                cell = Cell()
                self.layout.addWidget(cell, y, x)
                if [y+1,x+1] in self.cell_list and randomState == False:
                    cell.changeState()

        if randomState == True:
            for idx in range(self.layout.count()):
                destiny = random.randint(0,10)
                if destiny == 1:
                    item = self.layout.itemAt(idx)
                    cell = item.widget()
                    cell.changeState()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def parseArgv(self):
        argv = sys.argv
        if len(argv) == 1:
            self.random = True

        elif len(argv) > 1:
            self.cell_list = []
            self.duration = 0

            fd = open("state.txt", "r")
            lines = fd.readlines()
            lines = list(map(lambda s: s.strip(), lines))

            numOfTable = lines[0].split(" ")
            width = int(numOfTable[0])
            height = int(numOfTable[1])

            numOfCell = int(lines[1])
            lines = lines[2:]
            for line in lines:
                temp = line.split(" ")
                tempCol = int(temp[0])
                tempRow = int(temp[1])
                self.cell_list.append([tempCol,tempRow])

            if len(argv) == 3:
                duration = argv[2]

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
