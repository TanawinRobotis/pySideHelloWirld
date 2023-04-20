import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set the window size and title
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Hello World')

        # Create the "Hello world" button at the center of the window
        button_hello = QPushButton('hello world', self)
        button_hello.setGeometry(150, 250, 100, 50)
        button_hello.clicked.connect(self.show_message_box)

        # Create the "Show image" button to the right of the "Hello world" button
        self.button_image = QPushButton('image', self)
        self.button_image.setGeometry(250, 250, 100, 50)
        self.button_image.clicked.connect(self.select_image)

    def show_message_box(self):
        # Show a message box when the "Hello world" button is clicked
        message_box = QMessageBox()
        message_box.setText('Hello world')
        message_box.exec_()

    def select_image(self):
        # Open a file dialog and allow the user to select an image file
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter('Image Files (*.png *.jpg *.jpeg *.bmp)')
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec():
            path = file_dialog.selectedFiles()[0]
            self.show_image(path)

    def show_image(self, path):
        # Show the selected image when the "Show image" button is clicked
        label = QLabel(self)
        label.setGeometry(0, 0, 500, 400)

        try:
            # Load the image file using QPixmap and set it as the label's pixmap
            pixmap = QPixmap(path)
            label.setPixmap(pixmap)

        except Exception as error:
            print(error)

if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)

    # Create the main window instance
    window = MainWindow()
    window.show()

    # Start the event loop
    sys.exit(app.exec_())