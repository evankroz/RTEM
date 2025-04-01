from app import App
#import sys
from PyQt6.QtWidgets import QApplication

app = QApplication([])
window = App()
window.show()
app.exec()