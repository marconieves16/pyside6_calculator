import sys
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout
from PySide6.QtCore import Qt

class Calculator(QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        # Output tab
        self.value = 0
        self.output = QLineEdit(str(self.value))
        self.output.setReadOnly(True)
        self.output.setAlignment(Qt.AlignRight)
        self.output.setText("123")

        # Fist Row
        self.button_clean = QPushButton("CE")
        self.button_delete = QPushButton("Delete")
        self.button_divide = QPushButton("/")

        # Second Row
        self.button_7 = QPushButton("7")
        self.button_8 = QPushButton("8")
        self.button_9 = QPushButton("9")
        self.button_multiply = QPushButton("x")

        # Third Row
        self.button_4 = QPushButton("4")
        self.button_5 = QPushButton("5")
        self.button_6 = QPushButton("6")
        self.button_substract = QPushButton("-")

        # Fourth Row
        self.button_1 = QPushButton("1")
        self.button_2 = QPushButton("2")
        self.button_3 = QPushButton("3")
        self.button_adition = QPushButton("+")

        # Fifth Row
        self.button_negative = QPushButton("+-")
        self.button_0 = QPushButton("0")
        self.button_decimals = QPushButton(".")
        self.button_equal = QPushButton("=")

        # Set up the grid layout
        grid_layout = QGridLayout()

        # Adding the elements to the grid layout
        
        # Output label
        grid_layout.addWidget(self.output,0,0,1,4)

        # First Row to the Grid
        grid_layout.addWidget(self.button_clean,1,0,1,2)
        grid_layout.addWidget(self.button_delete,1,2)
        grid_layout.addWidget(self.button_divide,1,3)

        # Second Row to the Grid
        grid_layout.addWidget(self.button_7,2,0)
        grid_layout.addWidget(self.button_8,2,1)
        grid_layout.addWidget(self.button_9,2,2)
        grid_layout.addWidget(self.button_multiply,2,3)

        # Third Row to the Grid
        grid_layout.addWidget(self.button_4,3,0)
        grid_layout.addWidget(self.button_5,3,1)
        grid_layout.addWidget(self.button_6,3,2)
        grid_layout.addWidget(self.button_substract,3,3)

        # Fourth Row to the Grid
        grid_layout.addWidget(self.button_1,4,0)
        grid_layout.addWidget(self.button_2,4,1)
        grid_layout.addWidget(self.button_3,4,2)
        grid_layout.addWidget(self.button_adition,4,3)

        # Fifth Row to the Grid
        grid_layout.addWidget(self.button_negative,5,0)
        grid_layout.addWidget(self.button_0,5,1)
        grid_layout.addWidget(self.button_decimals,5,2)
        grid_layout.addWidget(self.button_equal,5,3)

        # Setting the layout
        self.setLayout(grid_layout)

        # Setting the windows title
        self.setWindowTitle("Calculator")


   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Calculator()
    widget.show()
    sys.exit(app.exec_())