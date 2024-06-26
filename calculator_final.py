import sys
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QSizePolicy, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt, QTimer

class Calculator(QWidget):


    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Variables
        self.value = "0"
        self.previous_value = "0"
        self.dec = False
        self.current_operation = "none"
        self.timer = QTimer()
        self.operation_dictionary = {
            "adition": "+",
            "substract": "-",
            "multiply": "x",
            "divide": "/"
        }

        # Previous value tab
        self.secondary_output = QLineEdit(str(self.previous_value))
        self.secondary_output.setReadOnly(True)
        self.secondary_output.setAlignment(Qt.AlignRight)
        #self.secondary_output.setVisible(False)

        # Operation output tab
        self.operation_output = QLineEdit()
        self.operation_output.setReadOnly(True)
        self.operation_output.setAlignment(Qt.AlignRight)

        # Output tab
        self.output = QLineEdit(str(self.value))
        self.output.setReadOnly(True)
        self.output.setAlignment(Qt.AlignRight)

        # Fist Row
        self.button_clear = QPushButton("CE")
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

        # Top horizontal box layout
        h_layout = QHBoxLayout()

        # Adding elements to the top horizontal layout
        h_layout.addWidget(self.secondary_output)
        h_layout.addWidget(self.operation_output)

        # Set up the grid layout
        grid_layout = QGridLayout()

        # Adding the elements to the grid layout

        # Secondary output label
        #grid_layout.addWidget(self.secondary_output, 0, 0, 1, 3)

        # Operation output label
        #grid_layout.addWidget(self.operation_output, 0, 3, 1, 1)

        # Output label
        grid_layout.addWidget(self.output, 1, 0, 1, 4)

        # First Row to the Grid
        grid_layout.addWidget(self.button_clear, 2, 0, 1, 2)
        grid_layout.addWidget(self.button_delete, 2, 2)
        grid_layout.addWidget(self.button_divide, 2, 3)

        # Second Row to the Grid
        grid_layout.addWidget(self.button_7, 3, 0)
        grid_layout.addWidget(self.button_8, 3, 1)
        grid_layout.addWidget(self.button_9, 3, 2)
        grid_layout.addWidget(self.button_multiply, 3, 3)

        # Third Row to the Grid
        grid_layout.addWidget(self.button_4,4,0)
        grid_layout.addWidget(self.button_5,4,1)
        grid_layout.addWidget(self.button_6,4,2)
        grid_layout.addWidget(self.button_substract,4,3)

        # Fourth Row to the Grid
        grid_layout.addWidget(self.button_1,5,0)
        grid_layout.addWidget(self.button_2,5,1)
        grid_layout.addWidget(self.button_3,5,2)
        grid_layout.addWidget(self.button_adition,5,3)

        # Fifth Row to the Grid
        grid_layout.addWidget(self.button_negative,6,0)
        grid_layout.addWidget(self.button_0,6,1)
        grid_layout.addWidget(self.button_decimals,6,2)
        grid_layout.addWidget(self.button_equal,6,3)

        # Buttons connections 
        self.button_1.clicked.connect(lambda:self.typing(1))
        self.button_2.clicked.connect(lambda:self.typing(2))
        self.button_3.clicked.connect(lambda:self.typing(3))
        self.button_4.clicked.connect(lambda:self.typing(4))
        self.button_5.clicked.connect(lambda:self.typing(5))
        self.button_6.clicked.connect(lambda:self.typing(6))
        self.button_7.clicked.connect(lambda:self.typing(7))
        self.button_8.clicked.connect(lambda:self.typing(8))
        self.button_9.clicked.connect(lambda:self.typing(9))
        self.button_0.clicked.connect(lambda:self.typing(0))

        #Clear button connection
        self.button_clear.clicked.connect(lambda:self.clear(True))

        # Delete button connection
        self.button_delete.clicked.connect(lambda:self.delete())
        
        # Negative button connection
        self.button_negative.clicked.connect(lambda:self.negative())
        
        # Decimals button connection
        self.button_decimals.clicked.connect(lambda:self.decimals())

        # Adition button connection
        self.button_adition.clicked.connect(lambda:self.adition())

        # Substract button connection
        self.button_substract.clicked.connect(lambda:self.substract())

        # Multiply button connection
        self.button_multiply.clicked.connect(lambda:self.multiply())

        # Divide button connection
        self.button_divide.clicked.connect(lambda:self.divide())

        # Equal button connection
        self.button_equal.clicked.connect(lambda:self.equal())

        # Size Policy for elements
        #self.secondary_output.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed, 5))
        #self.operation_output.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed, 1))
        h_layout.setStretchFactor(self.secondary_output, 12)
        h_layout.setStretchFactor(self.operation_output, 1)


        # Setting the main vertical layout
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(grid_layout)

        # Setting the layout
        self.setLayout(v_layout)

        # Setting the windows title
        self.setWindowTitle("Calculator")
    
    # Typing method will handle the numbers connections 
    def typing(self, num):
        string = str(num)
        if self.value == "0":
            self.value = string
        else:
            self.value = self.value + string
        self.update(False)
        
    # The update method will update the output
    def update(self, secondary_update):
        if secondary_update == True:
            self.secondary_output.setText(self.previous_value)
        self.output.setText(str(self.value))
        

    # The clear method will set the current value to 0 and update the output
    def clear(self, secondary_update):
        self.value = "0"
        if secondary_update == True: 
            self.previous_value = "0"
        self.dec = False
        self.current_operation = 'none'
        self.update(True)
    
    # The delete function will delete the last number entered
    def delete(self):
        if self.value == "0":
            pass
        elif len(self.value) == 1:
            self.clear(False)
        else:
            self.value = self.value[:-1]
        if self.value == "-":
            self.clear(False)
        self.update(False)
        
    # The negative function alternates the sign of the current value
    def negative(self):
        if self.value == "0":
            pass
        elif self.value[0] == "-":
            self.value = self.value[1:]
        else:
            self.value = "-" + self.value
        self.update(False)

    # The decimal function creates a dot that indicates the beginning of a float value
    def decimals(self):
        self.dec = True
        if "." not in self.value:
            self.value = self.value + "."

    # The math operation decorator i dont know what it will do yet
    def math_operation(func):
        def wrapper(self):
            if self.current_operation == "none":
                self.operation_output.setText("")
                self.previous_value = self.value
            elif self.current_operation == "adition":
                self.previous_value = str(float(self.previous_value) + float(self.value))
            elif self.current_operation == "substract":
                self.previous_value = str(float(self.previous_value) - float(self.value))
            elif self.current_operation == "multiply":
                self.previous_value = str(float(self.previous_value) * float(self.value))
            else:
                try:
                    self.previous_value = str(float(self.previous_value) / float(self.value))
                except ZeroDivisionError:
                    self.timer.setSingleShot(True)
                    self.timer.timeout.connect(lambda:self.output.setText(self.value))
                    self.timer.start(3000)
                    self.output.setText("Zero Error Divison")
            self.value = "0"
            self.update(True)
            func(self)
            self.operation_output.setText(self.operation_dictionary[self.current_operation])
        return wrapper


    @math_operation
    def adition(self):
        self.current_operation = "adition"
    @math_operation
    def substract(self):
        self.current_operation = "substract"

    @math_operation
    def multiply(self):
        self.current_operation = "multiply"

    @math_operation
    def divide(self):
        self.current_operation = "divide"

    def equal(self):
        if self.current_operation == "none":
            pass
        elif self.current_operation == "adition":
            self.previous_value = str(float(self.previous_value) + float(self.value))
        elif self.current_operation == "substract":
            self.previous_value = str(float(self.previous_value) - float(self.value))
        elif self.current_operation == "multiply":
            self.previous_value = str(float(self.previous_value) * float(self.value))
        else:
            try:
                self.previous_value = str(float(self.previous_value) / float(self.value))
            except ZeroDivisionError:
                self.timer.setSingleShot(True)
                self.timer.timeout.connect(lambda:self.output.setText(self.value))
                self.timer.start(3000)
                self.output.setText("Zero Error Divison")
        if self.current_operation == "none":
            self.update(False)
        else:
            self.update(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Calculator()
    widget.show()
    sys.exit(app.exec())