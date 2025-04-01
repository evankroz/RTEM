import numpy as np

def create_demo_plot(ax):
    x = np.linspace(0, 4 * np.pi, 100)
    ax.plot(x, np.sin(x), label='Sine Wave')
    ax.plot(x, np.cos(x), label='Cosine Wave', linestyle='--')
    # ax.plot(x, 0.5 * np.tanh(x), label='Activation', color='red')

    ax.set_title("Signal Demonstration")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.legend()
    ax.grid(True)