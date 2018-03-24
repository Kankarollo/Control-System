import AppHandler
import math
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

def submitEvent():
    k = app.getEntry("k")
    a = app.getEntry("a")
    b = app.getEntry("b")
    m = app.getEntry("m")
    A = app.getEntry("A")
    list = [k, a, b, m, A]
    if all(list) is not None and all(list) > 0:
        checkStability(k, a, b, m, A)
    else:
        app.warningBox("Error", "Wykryto puste pola, lub wartości mniejsze od zera!")


def checkStability(k, a, b, m, A):
    if a * b > m * k * A:
        app.infoBox("Stability", "Układ jest stabilny!")
    else:
        app.warningBox("Stability", "Układ nie jest stabilny!")


def sineWave():
    arg = (2 * math.pi) / 1000
    x = []
    y = []
    for i in range(2000):
        x.append(arg * i)
        y.append(math.sin(arg * i))
    plt.plot(x, y)
    plt.show()

def squareWave():
    t = np.linspace(0, 1, 500, endpoint=False)
    plt.plot(t, signal.square(2 * math.pi * 5 * t))
    plt.ylim(-2, 2)
    plt.show()


app = AppHandler.GUI()
app.addButton("Submit", submitEvent, column=1, row=1)
app.addButton("Show Sin Wave", sineWave, column=1, row=2)
app.addButton("Show Square Wave", squareWave, column=1, row=3)
app.go()
k = 0
a = 0
b = 0
m = 0
A = 0
