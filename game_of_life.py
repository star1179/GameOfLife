import sys
import PyQt5.QtWidgets import *
import PyQt5.QtGui import *
import PyQt5.QtCore import *

class Cell(QWidget):
    def __init__(self):
        super().__init__()
        self.color = 'gray'
        self.life = 0
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
        qp.drawRect(0, 0, 10, 10)

    def changeState(self):
        if self.life == False:
            self.life = True
            self.color = 'yellow'
        else:
            self.life = False
            self.color = 'gray'

        self.update()

    def checkDestiny(self):
        if self.alive_round < 2 and self.life == 1:
            self.changeState()
        elif self.alive_round == 3 and self.life == 0:
            self.changeState()
        elif self.alive_round > 3 and self.life == 1:
            self.changeState()
        else:
            pass

class Table(QWidget):
    def __init__(self, main=None, width = 80, height = 40, random = False, duration = 0, cell_list = []):
        super().__init__()
        self.main = main
        self.generation = 0
        self.duration = 10
        self.table_width = width
        self.table_height = height
        self.cell_list = cell_list
        self.initUI()
        self.initTable(randomState=random)
        self.main.control_button.clicked.connect(self.initTimer)

    def initUI(self):
        self.layout = QGridLayout()
        self.layout.setSpacing(0)
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

    def initTimer(self):
        if self.main.control_button.text() == "Start":
            self.timer_run = QTimer()
            self.timer_run.setInterval(1000)  # 1 sec
            self.timer_run.timeout.connect(self.timeOutEvent)
            self.timer_run.start()
            self.main.control_button.setText("Stop")
        else:
            self.timer_run.stop()
            self.main.contol_button.setText("Start")

    def timeOutEvent(self):
        if self.generation == self.duration and self.duration != 0:
            self.timer_run.stop()
            self.dumpState()
            self.main.control_button.setText("End")
            return

        for idx in range(self.layout.count()):
            item = self.layout.itemAt(idx)
            pos = self.layout.getItemPosition(idx)
            x, y = pos[0], pos[1]
            target_widget = item.widget()
            self.getNumOfAlive(x, y, target_widget)

        for idx in range(self.layout.count()):
            item = self.layout.itemAt(idx)
            cell = item.widget()
            cell.checkDestiny()

        self.generation += 1
        self.main.state_button.setText("generation : {}".format(self.generation))

    def getNumOfAlive(self, x, y, target):
        sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                try:
                    sum += self.layout.itemAtPosition(x + i, y + j).widget().life
                except AttributeError:
                    pass

        target.alive_round = sum

    def dumpState(self):
        fd = open(sys.argv[1], "w")
        fd.write("{} {}\n".format(str(self.table_height), str(self.table_width)))
        alive_num = 0
        alive_list = [[], []]
        for i in range(self.table_height):
            for j in range(self.table_width):
                if self.layout.itemAtPosition(i,j).widget().life == 1:
                    alive_num += 1
                    alive_list[0].append(i+1)
                    alive_list[1].ap[end(j+1)
        fd.write("{}\n".format(str(alive_num))
        for idx in range(len(alive_list[0])):
            fd.write("{} {}\n".format(str(alive_list[0][idx]), str(alive_list[1][idx]))
        fd.close()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.parseArgv()
        self.initUI()

    def parseArgv(self):
        argv = sys.argv
        self.cell_list = []
        self.duration = 0
        self.random = False

        if len(argv) == 1:
            self.random = True
            self.table_width = 80
            self.table_height = 40

        elif len(argv) > 1:
            self.cell_list = []
            self.duration = 0

            fd = open(sys.argv[1], "r")
            lines = fd.readlines()
            fd.close()
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
                self.duration = argv[2]

    def initUI(self):
        self.setWindowTitle("John Conway's Game Of Life")
        self.control_button = QPushButton("Start")
        self.state_button = QPushButton("generation : 0")
        self.state_button.setFlat(True)

        table = Table(main = self, width = self.table_width, height = self.table_height, random = self.random, duration = self.duration, cell_list = self.cell_list)

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
