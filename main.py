import AppHandler


def submitEvent():
    k = app.getEntry("k")
    a = app.getEntry("a")
    b = app.getEntry("b")
    m = app.getEntry("m")
    A = app.getEntry("A")
    print(a)


app = AppHandler.GUI()
app.addButton("submit", submitEvent)
app.go()
k = 0
a = 0
b = 0
m = 0
A = 0
