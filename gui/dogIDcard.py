# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dogIDcardLeRlwG.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_dogIDcard(QWidget):
    def setupUi(self, dogIDcard):
        if dogIDcard.objectName():
            dogIDcard.setObjectName(u"dogIDcard")
        dogIDcard.resize(750, 400)
        self.name = QLabel(dogIDcard)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(10, 10, 400, 30))
        font = QFont()
        font.setPointSize(16)
        self.name.setFont(font)
        self.name.setAlignment(Qt.AlignCenter)
        self.Photo = QLabel(dogIDcard)
        self.Photo.setObjectName(u"Photo")
        self.Photo.setGeometry(QRect(430, 10, 300, 300))
        self.Photo.setStyleSheet(u"")
        self.Photo.setFrameShape(QFrame.NoFrame)
        self.Photo.setFrameShadow(QFrame.Plain)
        self.Photo.setLineWidth(6)
        self.Photo.setMidLineWidth(4)
        self.Photo.setPixmap(QPixmap(u"gui/resources/nophoto.png"))
        self.Photo.setScaledContents(False)
        self.horizontalLayoutWidget = QWidget(dogIDcard)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 345, 731, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Edit = QToolButton(self.horizontalLayoutWidget)
        self.Edit.setObjectName(u"Edit")
        icon = QIcon()
        icon.addFile(u"gui/resources/edit.png", QSize(), QIcon.Normal, QIcon.On)
        self.Edit.setIcon(icon)
        self.Edit.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.Edit)

        self.Transfer = QToolButton(self.horizontalLayoutWidget)
        self.Transfer.setObjectName(u"Transfer")
        icon1 = QIcon()
        icon1.addFile(u"gui/resources/arrows_swap.png", QSize(), QIcon.Normal, QIcon.On)
        self.Transfer.setIcon(icon1)
        self.Transfer.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.Transfer)

        self.span = QLabel(self.horizontalLayoutWidget)
        self.span.setObjectName(u"span")

        self.horizontalLayout.addWidget(self.span)

        self.Delete = QToolButton(self.horizontalLayoutWidget)
        self.Delete.setObjectName(u"Delete")
        icon2 = QIcon()
        icon2.addFile(u"gui/resources/delete.png", QSize(), QIcon.Normal, QIcon.On)
        self.Delete.setIcon(icon2)
        self.Delete.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.Delete)

        self.formLayoutWidget = QWidget(dogIDcard)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 100, 381, 201))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.idLabel = QLabel(self.formLayoutWidget)
        self.idLabel.setObjectName(u"idLabel")
        self.idLabel.setMinimumSize(QSize(0, 20))
        font1 = QFont()
        font1.setPointSize(12)
        self.idLabel.setFont(font1)
        self.idLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.idLabel)

        self.id = QLabel(self.formLayoutWidget)
        self.id.setObjectName(u"id")
        self.id.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.id)

        self.OwnerLabel = QLabel(self.formLayoutWidget)
        self.OwnerLabel.setObjectName(u"OwnerLabel")
        self.OwnerLabel.setMinimumSize(QSize(0, 20))
        self.OwnerLabel.setFont(font1)
        self.OwnerLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.OwnerLabel)

        self.owner = QLabel(self.formLayoutWidget)
        self.owner.setObjectName(u"owner")
        self.owner.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.owner)

        self.dob = QLabel(self.formLayoutWidget)
        self.dob.setObjectName(u"dob")
        self.dob.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dob)

        self.ColorLabel = QLabel(self.formLayoutWidget)
        self.ColorLabel.setObjectName(u"ColorLabel")
        self.ColorLabel.setMinimumSize(QSize(0, 20))
        self.ColorLabel.setFont(font1)
        self.ColorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.ColorLabel)

        self.color = QLabel(self.formLayoutWidget)
        self.color.setObjectName(u"color")
        self.color.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.color)

        self.BreedLabel = QLabel(self.formLayoutWidget)
        self.BreedLabel.setObjectName(u"BreedLabel")
        self.BreedLabel.setMinimumSize(QSize(0, 20))
        self.BreedLabel.setFont(font1)
        self.BreedLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.BreedLabel)

        self.breed = QLabel(self.formLayoutWidget)
        self.breed.setObjectName(u"breed")
        self.breed.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.breed)

        self.DoBLabel = QLabel(self.formLayoutWidget)
        self.DoBLabel.setObjectName(u"DoBLabel")
        self.DoBLabel.setMinimumSize(QSize(0, 20))
        self.DoBLabel.setFont(font1)
        self.DoBLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.DoBLabel)

        self.background = QLabel(dogIDcard)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 750, 400))
        self.background.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.505364, y2:0.46, stop:0.176136 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));")
        self.background.raise_()
        self.name.raise_()
        self.Photo.raise_()
        self.horizontalLayoutWidget.raise_()
        self.formLayoutWidget.raise_()

        self.retranslateUi(dogIDcard)

        QMetaObject.connectSlotsByName(dogIDcard)
    # setupUi

    def retranslateUi(self, dogIDcard):
        dogIDcard.setWindowTitle(QCoreApplication.translate("dogIDcard", u"Form", None))
        self.name.setText(QCoreApplication.translate("dogIDcard", u"Name", None))
        self.Photo.setText("")
        self.Edit.setText(QCoreApplication.translate("dogIDcard", u"...", None))
        self.Transfer.setText(QCoreApplication.translate("dogIDcard", u"...", None))
        self.span.setText("")
        self.Delete.setText(QCoreApplication.translate("dogIDcard", u"...", None))
        self.idLabel.setText(QCoreApplication.translate("dogIDcard", u"Registration #:", None))
        self.id.setText("")
        self.OwnerLabel.setText(QCoreApplication.translate("dogIDcard", u"Registered To:", None))
        self.owner.setText("")
        self.dob.setText("")
        self.ColorLabel.setText(QCoreApplication.translate("dogIDcard", u"Color(s):", None))
        self.color.setText("")
        self.BreedLabel.setText(QCoreApplication.translate("dogIDcard", u"Breed:", None))
        self.breed.setText("")
        self.DoBLabel.setText(QCoreApplication.translate("dogIDcard", u"Age:", None))
        self.background.setText("")
    # retranslateUi

