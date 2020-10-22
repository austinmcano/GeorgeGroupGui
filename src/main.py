import sys
from PySide2 import QtWidgets
from src.gui_elements.main_window import MainWindow
# import qdarkstyle

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # style = qdarkstyle.load_stylesheet()
    # app.setStyleSheet(style)
    app.setStyle('Fusion')

    window = MainWindow()
    window.resize(1100,600)
    window.show()

    sys.exit(app.exec_())
