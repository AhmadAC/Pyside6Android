# main.py
import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Qt Android App")
        label = QLabel("Hello from Qt for Python on Android!", self)
        # A more robust way to center the label:
        # from PySide6.QtCore import Qt
        # label.setAlignment(Qt.AlignCenter)
        # self.setCentralWidget(label)

        # For simplicity in this example, we'll set its geometry
        # but using layouts (QVBoxLayout, QHBoxLayout, QGridLayout) is recommended for real apps.
        label.setGeometry(50, 50, 400, 30) # x, y, width, height
        self.setFixedSize(500, 150) # Set a fixed size for the main window for simplicity

if __name__ == "__main__":
    # Ensure that the QAPPLICATION_PLATFORM environment variable is set for Android
    # import os
    # os.environ["QT_QPA_PLATFORM"] = "android" # This is usually handled by the build system

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
