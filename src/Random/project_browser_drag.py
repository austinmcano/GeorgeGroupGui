# from Ui_Files.DockWidgets_OLD.dw_ProjectView import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
from src.gui_elements.settings import ApplicationSettings

class ProjectBrowser(QtWidgets.QDockWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # self.dw = QtWidgets.QDockWidget()
        # self.dw_ui = Ui_DockWidget()
        # self.dw_ui.setupUi(self.dw)
        # Above for Tree() Class

        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)
        # Above for QtWidgets.QTreeView class

        self._init_vars()
        self._init_widgets()
        self._init_UI()

    def _init_vars(self):
        self.current_data_container = None

    def _init_widgets(self):
        self.tree_view = self.ui.treeView
        # Above for Tree class drag drop QTreeView
        # self.tree_view = self.ui.treeView
        # Above for normal QtWidgets.QTreeView
        self.context_menu = QtWidgets.QMenu(self)
        # rc_browser_options(self)

    def _init_UI(self):
        # pass
        # self.model = QtWidgets.QFileSystemModel()
        # self.model.setRootPath(QtCore.QDir.currentPath())
        #
        # self.tree_view.setModel(self.model)
        # self.tree_view.setSortingEnabled(True)
        #
        # self.tree_view.sortByColumn(True)
        # self.tree_view.setRootIndex(self.model.index(ApplicationSettings.PROJECT_PATH))
        #
        # self.tree_view.setModel(self.model)
        # self.tree_view.clicked.connect(self.item_clicked)
        self.tree_view.installEventFilter(self)
        # self.tree_view.setColumnWidth(0, 200)
        # Above for QTreeView class and for Tree() then pass

        # Create context menu
        rc_browser_options(self)

    def project_changed(self):
        pass

    def item_clicked(self):
        pass

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False


class Tree(QtWidgets.QTreeView):
    def __init__(self):
        QtWidgets.QTreeView.__init__(self)
        model = QtWidgets.QFileSystemModel()
        model.setRootPath(QtCore.QDir.currentPath())

        self.setModel(model)
        self.setRootIndex(model.index(ApplicationSettings.PROJECT_PATH))
        model.setReadOnly(False)

        self.setSelectionMode(self.SingleSelection)
        self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setColumnWidth(0, 200)

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False
        print('RC')

    def dragEnterEvent(self, event):
        m = event.mimeData()
        if m.hasUrls():
            for url in m.urls():
                if url.isLocalFile():
                    event.accept()
                    return
        event.ignore()

    def dropEvent(self, event):
        if event.source():
            QtWidgets.QTreeView.dropEvent(self, event)
        else:
            ix = self.indexAt(event.pos())
            if not self.model().isDir(ix):
                ix = ix.parent()
            pathDir = self.model().filePath(ix)
            m = event.mimeData()
            if m.hasUrls():
                urlLocals = [url for url in m.urls() if url.isLocalFile()]
                accepted = False
                for urlLocal in urlLocals:
                    path = urlLocal.toLocalFile()
                    info = QtWidgets.QFileInfo(path)
                    n_path = QtWidgets.QDir(pathDir).filePath(info.fileName())
                    o_path = info.absoluteFilePath()
                    if n_path == o_path:
                        continue
                    if info.isDir():
                        QtWidgets.QDir().rename(o_path, n_path)
                    else:
                        qfile = QtWidgets.QFile(o_path)
                        if QtWidgets.QFile(n_path).exists():
                            n_path += "(copy)"
                        qfile.rename(n_path)
                    accepted = True
                if accepted:
                    event.acceptProposedAction()


class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(237, 460)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        # self.treeView = QtWidgets.QTreeView(self.dockWidgetContents)
        self.treeView = Tree()
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout.addWidget(self.treeView)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QtCore.QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QtCore.QCoreApplication.translate("DockWidget", u"Project View", None))
    # retranslateUi



