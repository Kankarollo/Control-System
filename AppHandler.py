import appJar


def GUI():
    app = appJar.gui("Modeling Project", "800x600")
    app.addLabelNumericEntry("k")
    app.addLabelNumericEntry("a")
    app.addLabelNumericEntry("b")
    app.addLabelNumericEntry("m")
    app.addLabelNumericEntry("A")
    return app