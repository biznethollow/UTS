import sys

from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
)

from template import template  

class GridTab(template):  
    def __init__(self):
        super().__init__()

        # Buat layout grid
        self.layout = QGridLayout()

        # Pasang widget dan tombol yang sudah diwarisi dari template
        self.layout.addWidget(self.output, 0, 0, 1, 3)
        self.layout.addWidget(self.button1, 1, 0)
        self.layout.addWidget(self.button3, 1, 1)
        self.layout.addWidget(self.buttonPlus, 1, 2)
        self.layout.addWidget(self.button4, 2, 0)
        self.layout.addWidget(self.button7, 2, 1)
        self.layout.addWidget(self.buttonMin, 2, 2)
        self.layout.addWidget(self.button8, 3, 0)
        self.layout.addWidget(self.button9, 3, 1)
        self.layout.addWidget(self.buttonDivision, 3, 2)
        self.layout.addWidget(self.buttonMultiply, 4, 2)
        self.layout.addWidget(self.buttonErase, 4, 0)
        self.layout.addWidget(self.buttonEqual, 4, 1)

        # Set layout ke window
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GridTab()
    window.show()
    app.exec()