import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set the window size and title
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Hello World')

        # Create a button at the center of the window
        button = QPushButton('Click me', self)
        button.setGeometry(200, 200, 100, 50)
        button.clicked.connect(self.show_message_box)

    def show_message_box(self):
        # Show a message box when the button is clicked
        message_box = QMessageBox()
        message_box.setText('Hello world')
        message_box.exec_()

if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)

    # Create the main window
    main_window = MainWindow()

    # Show the main window
    main_window.show()

    # Run the event loop
    sys.exit(app.exec_())
