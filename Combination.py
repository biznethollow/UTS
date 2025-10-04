import sys
from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
)

from template import template  

class Combination(template):  
    def __init__(self, output):
        super().__init__(output)

        self.layout1 = QVBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout4 = QHBoxLayout()
        self.layout5 = QHBoxLayout()

        self.layout1.addWidget(self.output)

        # Baris pertama (setelah output)
        self.CombiLayout(self.layout2, self.layout1, self.button1, self.button3, self.buttonPlus)

        # Baris kedua
        self.CombiLayout(self.layout3, self.layout1, self.button4, self.button7, self.buttonMin)
        
        # Baris ketiga
        self.CombiLayout(self.layout4, self.layout1, self.button8, self.button9, self.buttonDivision)

        # baris keempat
        self.CombiLayout(self.layout5, self.layout1, self.buttonErase, self.buttonEqual, self.buttonMultiply)

        self.setLayout(self.layout1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Combination()
    window.show()
    app.exec()  
