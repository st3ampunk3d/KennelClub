# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'memberIDcardszGsIS.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_memberIDCard(QWidget):
    def setupUi(self, memberIDCard):
        if memberIDCard.objectName():
            memberIDCard.setObjectName(u"memberIDCard")
        memberIDCard.resize(750, 400)
        self.name = QLabel(memberIDCard)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(10, 10, 400, 30))
        font = QFont()
        font.setPointSize(16)
        self.name.setFont(font)
        self.name.setAlignment(Qt.AlignCenter)
        self.Photo = QLabel(memberIDCard)
        self.Photo.setObjectName(u"Photo")
        self.Photo.setGeometry(QRect(430, 10, 300, 300))
        self.Photo.setStyleSheet(u"")
        self.Photo.setFrameShape(QFrame.NoFrame)
        self.Photo.setFrameShadow(QFrame.Plain)
        self.Photo.setLineWidth(6)
        self.Photo.setMidLineWidth(4)
        self.Photo.setPixmap(QPixmap(u"gui/resources/noProfilephoto.png"))
        self.Photo.setScaledContents(True)
        self.horizontalLayoutWidget = QWidget(memberIDCard)
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

        self.Edit_2 = QToolButton(self.horizontalLayoutWidget)
        self.Edit_2.setObjectName(u"Edit_2")
        icon1 = QIcon()
        icon1.addFile(u"gui/resources/plus.png", QSize(), QIcon.Normal, QIcon.On)
        self.Edit_2.setIcon(icon1)
        self.Edit_2.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.Edit_2)

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

        self.formLayoutWidget = QWidget(memberIDCard)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 40, 381, 271))
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

        self.MemberDateLabel = QLabel(self.formLayoutWidget)
        self.MemberDateLabel.setObjectName(u"MemberDateLabel")
        self.MemberDateLabel.setMinimumSize(QSize(0, 20))
        self.MemberDateLabel.setFont(font1)
        self.MemberDateLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.MemberDateLabel)

        self.MemberDate = QLabel(self.formLayoutWidget)
        self.MemberDate.setObjectName(u"MemberDate")
        self.MemberDate.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.MemberDate)

        self.PhoneLabel_2 = QLabel(self.formLayoutWidget)
        self.PhoneLabel_2.setObjectName(u"PhoneLabel_2")
        self.PhoneLabel_2.setMinimumSize(QSize(0, 20))
        self.PhoneLabel_2.setFont(font1)
        self.PhoneLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.PhoneLabel_2)

        self.Phone_3 = QLabel(self.formLayoutWidget)
        self.Phone_3.setObjectName(u"Phone_3")
        self.Phone_3.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Phone_3)

        self.AddressLabel = QLabel(self.formLayoutWidget)
        self.AddressLabel.setObjectName(u"AddressLabel")
        self.AddressLabel.setMinimumSize(QSize(0, 20))
        self.AddressLabel.setFont(font1)
        self.AddressLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.AddressLabel)

        self.Address = QLabel(self.formLayoutWidget)
        self.Address.setObjectName(u"Address")
        self.Address.setMinimumSize(QSize(0, 90))
        self.Address.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.Address)

        self.EmailLabel = QLabel(self.formLayoutWidget)
        self.EmailLabel.setObjectName(u"EmailLabel")
        self.EmailLabel.setMinimumSize(QSize(0, 20))
        self.EmailLabel.setFont(font1)
        self.EmailLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.EmailLabel)

        self.Email = QLabel(self.formLayoutWidget)
        self.Email.setObjectName(u"Email")
        self.Email.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.Email)

        self.PhoneLabel = QLabel(self.formLayoutWidget)
        self.PhoneLabel.setObjectName(u"PhoneLabel")
        self.PhoneLabel.setMinimumSize(QSize(0, 20))
        self.PhoneLabel.setFont(font1)
        self.PhoneLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.PhoneLabel)

        self.Phone = QLabel(self.formLayoutWidget)
        self.Phone.setObjectName(u"Phone")
        self.Phone.setFont(font1)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.Phone)


        self.retranslateUi(memberIDCard)

        QMetaObject.connectSlotsByName(memberIDCard)
    # setupUi

    def retranslateUi(self, memberIDCard):
        memberIDCard.setWindowTitle(QCoreApplication.translate("memberIDCard", u"Form", None))
        self.name.setText(QCoreApplication.translate("memberIDCard", u"Name", None))
        self.Photo.setText("")
        self.Edit.setText(QCoreApplication.translate("memberIDCard", u"...", None))
        self.Edit_2.setText(QCoreApplication.translate("memberIDCard", u"...", None))
        self.span.setText("")
        self.Delete.setText(QCoreApplication.translate("memberIDCard", u"...", None))
        self.idLabel.setText(QCoreApplication.translate("memberIDCard", u"Membership #:", None))
        self.id.setText("")
        self.MemberDateLabel.setText(QCoreApplication.translate("memberIDCard", u"Member Tier:", None))
        self.MemberDate.setText("")
        self.PhoneLabel_2.setText(QCoreApplication.translate("memberIDCard", u"# of Dogs:", None))
        self.Phone_3.setText("")
        self.AddressLabel.setText(QCoreApplication.translate("memberIDCard", u"Address:", None))
        self.Address.setText("")
        self.EmailLabel.setText(QCoreApplication.translate("memberIDCard", u"Email:", None))
        self.Email.setText("")
        self.PhoneLabel.setText(QCoreApplication.translate("memberIDCard", u"Phone:", None))
        self.Phone.setText("")
    # retranslateUi