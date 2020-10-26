import sys
from PySide2 import QtWidgets,QtCore
from src.gui_elements.main_window import MainWindow
# from src import qdarkstyle
settings = QtCore.QSettings('Resources/settings.ini', QtCore.QSettings.IniFormat)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # if settings.value('app_style') == 'darkstyle':
    #     style = qdarkstyle.load_stylesheet()
    #     app.setStyleSheet(style)
    # else:
    app.setStyle(settings.value('app_style'))

    window = MainWindow()
    # window.resize(1100,600)
    window.show()

    sys.exit(app.exec_())
