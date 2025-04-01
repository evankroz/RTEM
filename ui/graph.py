from  matplotlib.figure import Figure
import matplotlib as plt
plt.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6.QtWidgets import QApplication

#TODO: Make this crap work - Most work will continue over the summer when I actually have time...

THRUST_COLOR = "tab:blue"

class GraphWidget(FigureCanvas):

    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(5,4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

        

