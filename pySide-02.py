import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog

class ImageWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set the widget properties
        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 500, 500)
        
        # Create a label to display the image
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        
        # Create a button to show the file dialog
        self.button = QPushButton("Select Image", self)
        self.button.clicked.connect(self.show_file_dialog)
        
        # Create a vertical layout and add the button and label to it
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
    
    def show_file_dialog(self):
        # Create a file dialog window for selecting an image file
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            # Get the selected file path
            file_path = file_dialog.selectedFiles()[0]
            # Load the image
            image = QPixmap(file_path)
            # Set the image as the pixmap for the label
            self.label.setPixmap(image)
            # Resize the window to its initial size
            self.resize(self.geometry().width(), self.geometry().height())

if __name__ == "__main__":
    # Create the application instance
    app = QApplication(sys.argv)
    
    # Create the widget instance and show it
    image_widget = ImageWidget()
    image_widget.show()
    
    # Run the application event loop
    sys.exit(app.exec_())