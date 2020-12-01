import sys
from PySide2 import QtWidgets,QtCore
from src.gui_elements.main_window import MainWindow
from src import qdarkstyle
settings = QtCore.QSettings('Resources/settings.ini', QtCore.QSettings.IniFormat)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    style = settings.value('app_style')
    # if style == 'darkstyle':
    #     sty = qdarkstyle.load_stylesheet()
    #     app.setStyleSheet(sty)
    # else:
    app.setStyle(settings.value('app_style'))

    window = MainWindow()
    # window.resize(1100,600)
    window.show()

    sys.exit(app.exec_())
"""
to do list:
Need to enable multiple line saving in the SAVE_Csv dialog (mostly done)
remake the figure by saving all the parts of figure 
Plot Annotations
Uploading Figures and saving Figures
"""