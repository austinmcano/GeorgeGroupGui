import sys
from PySide2 import QtWidgets,QtCore, QtGui
from src.gui_elements.main_window import MainWindow
# from src import pyqtcss

settings = QtCore.QSettings('Resources/settings.ini', QtCore.QSettings.IniFormat)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    style = settings.value('app_style')
    if style == 'DarkFusion':
        app.setStyle('Fusion')
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)

        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
        palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
        app.setPalette(palette)
    elif style == 'GrayFusion':
        app.setStyle('Fusion')
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(180, 180, 180))
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(40, 40, 40))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.darkGray)
        palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.darkGray)
        palette.setColor(QtGui.QPalette.Text, QtGui.QColor(180, 180, 180))
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(180, 180, 180))
        palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(60, 60, 60).lighter())
        palette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(180, 180, 180))
        app.setPalette(palette)
    else:
        app.setStyle(style)


    window = MainWindow()
    window.resize(settings.value('size'))
    window.show()
    sys.exit(app.exec_())

"""
to do list:
Need to enable multiple line saving in the SAVE_Csv dialog (mostly done)
remake the figure by saving all the parts of figure 
Plot Annotations
Uploading Figures and saving Figures
"""