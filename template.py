from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QWidget,
    QLineEdit,
    QPushButton,
    
)
from operation import operate

class template(QWidget): 
    def __init__(self):
        super().__init__()

        # Output dan input
        self.output = QLineEdit()
        self.output.setReadOnly(True)
        self.output.setFixedSize(275, 100)

        # Semua tombol
        self.button1 = QPushButton("1")
        self.button3 = QPushButton("3")
        self.button4 = QPushButton("4")
        self.button7 = QPushButton("7")
        self.button8 = QPushButton("8")
        self.button9 = QPushButton("9")
        self.buttonPlus = QPushButton("+")
        self.buttonMin = QPushButton("-")
        self.buttonMultiply = QPushButton("x")
        self.buttonDivision = QPushButton(":")
        self.buttonEqual = QPushButton("=")
        self.buttonErase = QPushButton("⌫")

        self.button_and_ouput = [self.button1, self.button3, self.button4, self.button7, 
                                self.button8, self.button9, self.buttonDivision, 
                                self.buttonEqual, self.buttonErase, self.buttonMin, 
                                self.buttonMultiply, self.buttonPlus]
        
        for i in self.button_and_ouput:
            i.setFixedSize(90, 70)

        # Hubungkan tombol ke fungsi
        self.button1.clicked.connect(self.display1)
        self.button3.clicked.connect(self.display3)
        self.button4.clicked.connect(self.display4)
        self.button7.clicked.connect(self.display7)
        self.button8.clicked.connect(self.display8)
        self.button9.clicked.connect(self.display9)
        self.buttonPlus.clicked.connect(self.displayPlus)
        self.buttonMin.clicked.connect(self.displayMin)
        self.buttonMultiply.clicked.connect(self.displayMultiply)
        self.buttonDivision.clicked.connect(self.displayDivision)

        # Tombol hapus
        self.buttonErase.clicked.connect(self.erase_last)

        # Tombol sama dengan
        self.buttonEqual.clicked.connect(self.equal)

    def display1(self):
        self.output.setText(self.output.text() + "1")

    def display3(self):
        self.output.setText(self.output.text() + "3")

    def display4(self):
        self.output.setText(self.output.text() + "4")

    def display7(self):
        self.output.setText(self.output.text() + "7")

    def display8(self):
        self.output.setText(self.output.text() + "8")

    def display9(self):
        self.output.setText(self.output.text() + "9")
    
    def displayMin(self):
        self.output.setText(self.output.text() + "-")
        print("-")

    def displayMultiply(self):
        self.output.setText(self.output.text() + "x")
        print("x")

    def displayDivision(self):
        self.output.setText(self.output.text() + ":")
        print(":")

    def displayPlus(self):
        self.output.setText(self.output.text() + "+")
        print("+")

    def erase_last(self):
        current_text = self.output.text()
        self.output.setText(current_text[:-1])
    
    def equal(self):
        expr = self.output.text()
        result = eval(operate(expr))
        self.output.setText(str(result))
    
    def menu(self, text, slot, menuOperation):
        action = QAction(text, self)
        action.triggered.connect(slot)
        menuOperation.addAction(action)
    
    def CombiLayout(self, layout1, layout2, *button):
        for i in button:
            layout1.addWidget(i)
        layout2.addLayout(layout1)

