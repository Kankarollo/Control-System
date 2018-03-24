import appJar


def GUI():
    app = appJar.gui("Modeling Project", "800x600")
    app.addImage("pic", "graf.gif", 0, 0, colspan=2)
    app.addLabelNumericEntry("k", row=1, column=0)
    app.addLabelNumericEntry("a", 2, 0)
    app.addLabelNumericEntry("b", 3, 0)
    app.addLabelNumericEntry("m", 4, 0)
    app.addLabelNumericEntry("A", 5, 0)
    return app