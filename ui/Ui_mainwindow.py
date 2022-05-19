from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow: QtWidgets.QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 920)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 920))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 920))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralWidgetLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.centralWidgetLayout.setObjectName("centralWidgetLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        self.tabWidget.addTab(MainWindow.id_photo_generator, "")
        self.tabWidget.addTab(MainWindow.image_beautifier, "")
        self.tabWidget.addTab(MainWindow.batch_processer, "")

        self.centralWidgetLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)

    def retranslateUi(self, MainWindow: QtWidgets.QMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图像处理工具箱V1.0"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(MainWindow.id_photo_generator),
            _translate("MainWindow", "证件照生成"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(MainWindow.image_beautifier),
            _translate("MainWindow", "图片美化"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(MainWindow.batch_processer),
            _translate("MainWindow", "图片批处理"))
