import sys

from PyQt5 import QtWidgets

from Home import Ui_HomeWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    HomeWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow(HomeWindow)
    ui.setup_ui()
    HomeWindow.show()
    HomeWindow.setWindowTitle('Bio-GATS')
    sys.exit(app.exec_())
