from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtWidgets import QGraphicsView
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("MapViewer")
        self.fdir_ = ''
        layout = QGridLayout()

        openButton = QPushButton()
        openButton.setText("Open File")
        openButton.clicked.connect(self.on_click)

        layout.addWidget(openButton, 0, 0,)

        graphicsView = QGraphicsView()
        graphicsView.setAlignment(Qt.AlignCenter)
        graphicsView.setFixedSize(1200, 800)

        layout.addWidget(graphicsView, 1, 0, 1, 8)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    @pyqtSlot()
    def on_click(self):
        self.fdir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        print(bool(self.fdir_))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
