# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designeriYQgAJ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.show()

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        self.actionadd = QAction(MainWindow)
        self.actionadd.setObjectName(u"actionadd")
        icon = QIcon()
        icon.addFile(u"resources/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionadd.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1200, 800))
        self.background.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.505364, y2:0.46, stop:0.176136 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));")
        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(10, 50, 250, 740))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 250, 40))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.memberCardWdiget = QWidget(self.centralwidget)
        self.memberCardWdiget.setObjectName(u"memberCardWidget")
        self.memberCardWdiget.setGeometry(QRect(270, 0, 920, 400))
        self.memberCard = QVBoxLayout(self.memberCardWdiget)
        self.memberCard.setObjectName(u"memberCard")
        self.memberCard.setContentsMargins(0, 0, 0, 0)
        self.dogCardWidget = QWidget(self.centralwidget)
        self.dogCardWidget.setObjectName(u"dogCardWidget")
        self.dogCardWidget.setGeometry(QRect(270, 400, 920, 400))
        self.dogCard = QVBoxLayout(self.dogCardWidget)
        self.dogCard.setObjectName(u"dogCard")
        self.dogCard.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionadd)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionadd.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.background.setText("")
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Member", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Dog", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Dog2", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"CLUB MEMBERS", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi




