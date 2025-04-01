from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

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
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        
        x = np.linspace(0, 4*np.pi, 100)
        ax.plot(x, np.sin(x), label='Sine Wave')
        ax.plot(x, np.cos(x), label='Cosine Wave', linestyle='--')
        ax.plot(x, 0.5*np.tanh(x), label='Activation', color='red')
        
        ax.set_title("Signal Demonstration")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.legend()
        ax.grid(True)
        
        self.canvas.draw()