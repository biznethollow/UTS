import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QLineEdit
)
from Grid import GridTab
from Combination import Combination
from template import template

class MainWindow(QMainWindow, template):
    def __init__(self):

        # Output dan input
        self.output = QLineEdit()
        self.output.setReadOnly(True)
        self.output.setFixedSize(275, 100)

        super().__init__(self.output)
        
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

        self.tabs.addTab(GridTab(self.output), "Grid")
        self.tabs.addTab(Combination(self.output), "Combination")

        self.setCentralWidget(self.tabs)

app = QApplication(sys.argv)
app.setFont(QFont("Times New Roman"))

window = MainWindow()
window.show()

app.exec()
