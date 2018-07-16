import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from tool import Ui_MainWindow


def show_window():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    tool_ui = Ui_MainWindow()
    tool_ui.iniWindow(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())


show_window()

