import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
)
from Grid import GridTab
from Combination import Combination
from template import template

class MainWindow(QMainWindow, template):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 500)
        self.setWindowTitle("Team 7")

        self.menubar = self.menuBar()

        self.menuOperation = self.menubar.addMenu("&Operation")
        
        self.menu("&Addition (+)", self.displayPlus, self.menuOperation)
        self.menu("&Subtraction (-)", self.displayMin, self.menuOperation)
        self.menu("&Multiply (x)", self.displayMultiply, self.menuOperation)
        self.menu("&Division (:)", self.displayDivision, self.menuOperation)
        self.menu("&Equal (=)", self.equal, self.menuOperation)

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.tabs.setMovable(True)

        self.tabs.addTab(GridTab(), "Grid")
        self.tabs.addTab(Combination(), "Combination")

        self.setCentralWidget(self.tabs)

app = QApplication(sys.argv)
app.setFont(QFont("Times New Roman"))

window = MainWindow()
window.show()

app.exec()