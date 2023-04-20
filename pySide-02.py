import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class ImageWidget(QWidget):
    def __init__(self, image_path):
        super().__init__()
        
        # Load the image
        self.image = QPixmap(image_path)
        
        # Create a label to display the image
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        
        # Create a button to show the image
        self.button = QPushButton("Show Image", self)
        self.button.clicked.connect(self.show_image)
        
        # Create a vertical layout and add the button and label to it
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        
        # Set the widget properties
        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 300, 300)
    
    def show_image(self):
        # Set the image as the pixmap for the label
        self.label.setPixmap(self.image)
        # Resize the window to fit the image
        self.resize(self.image.width(), self.image.height())

if __name__ == "__main__":
    # Create the application instance
    app = QApplication(sys.argv)
    
    # Create the widget instance and show it
    image_widget = ImageWidget(r"D:\AI-Center\Computing\pyInterface\lab01\image\ai-center.png")
    image_widget.show()
    
    # Run the application event loop
    sys.exit(app.exec_())
