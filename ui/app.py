from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from demo_plot import create_demo_plot

#TODO: Create App(QApplication) instead of QMainWindow?

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Demo Plot")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.canvas = FigureCanvas(Figure(figsize=(8, 4)))
        layout.addWidget(self.canvas)

        button = QPushButton("Refresh Plot")
        button.clicked.connect(self.plot)
        layout.addWidget(button)

        self.plot()

    def plot(self):
        self.canvas.figure.clear()  # Clear the figure
        ax = self.canvas.figure.add_subplot(111)  # Create a new subplot
        create_demo_plot(ax)  # Pass the Axes object to the function
        self.canvas.draw()  # Redraw the canvas