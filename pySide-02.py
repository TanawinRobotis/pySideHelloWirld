import sys
import cv2
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap, QPainter, QPen
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox

class ImageWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set the widget properties
        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 500, 500)

        # Initialize the image and flag variables
        self.image = None
        self.image_loaded = False
        
        # Create a label to display the image
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        # Create a button to show the file dialog
        self.load_button = QPushButton("Select Image", self)
        self.load_button.clicked.connect(self.show_file_dialog)

        # Create a button to draw a rectangle in the center of the image
        self.draw_button = QPushButton("Draw Rectangle", self)
        self.draw_button.clicked.connect(self.draw_rectangle)

        # Create a vertical layout and add the buttons and label to it
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.draw_button)
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
            self.image = cv2.imread(file_path)
            # Check if the image was successfully loaded
            if self.image is not None:
                # Set the image loaded flag to true
                self.image_loaded = True
                # Convert the image from BGR to RGB color space
                self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
                # Check if the image is larger than 400x400 and resize it if necessary
                if self.image.shape[1] > 400 or self.image.shape[0] > 400:
                    self.image = cv2.resize(self.image, (400, 400), interpolation=cv2.INTER_AREA)
                # Convert the image to a Qt pixmap
                height, width, channel = self.image.shape
                bytesPerLine = 3 * width
                qt_image = QPixmap.fromImage(
                    QImage(self.image.data, width, height, bytesPerLine, QImage.Format_RGB888)
                )
                # Set the image as the pixmap for the label
                self.label.setPixmap(qt_image)
                # Resize the window to its initial size
                self.resize(self.geometry().width(), self.geometry().height())
            else:
                # Display an error message if the image could not be loaded
                QMessageBox.critical(self, "Error", "Could not load the image")

    def draw_rectangle(self):
        # Check if an image is loaded in the GUI
        if self.image_loaded:
            # Get the height and width of the image
            height, width, channel = self.image.shape
            # Calculate the center point of the image
            center_x = width // 2
            center_y = height // 2
            # Calculate the size of
            # the rectangle
            rect_width = 100
            rect_height = 100
            # Calculate the top-left corner coordinates of the rectangle
            rect_x = center_x - rect_width // 2
            rect_y = center_y - rect_height // 2
            # Draw the rectangle on the image using OpenCV
            cv2.rectangle(self.image, (rect_x, rect_y), (rect_x+rect_width, rect_y+rect_height), (0, 255, 0), thickness=2)
            # Convert the image to a Qt pixmap
            bytesPerLine = 3 * width
            qt_image = QPixmap.fromImage(
                QImage(self.image.data, width, height, bytesPerLine, QImage.Format_RGB888)
            )
            # Set the image as the pixmap for the label
            self.label.setPixmap(qt_image)
            # Resize the window to its initial size
            self.resize(self.geometry().width(), self.geometry().height())
        else:
            # Display an error message if no image is loaded in the GUI
            QMessageBox.warning(self, "Warning", "No image loaded")

if __name__ == "__main__":
    # Create the application instance
    app = QApplication(sys.argv)
    
    # Create the widget instance and show it
    image_widget = ImageWidget()
    image_widget.show()
    
    # Run the application event loop
    sys.exit(app.exec_())