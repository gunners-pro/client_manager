# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customer_form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_customer_form(object):
    def setupUi(self, customer_form):
        if not customer_form.objectName():
            customer_form.setObjectName(u"customer_form")
        customer_form.resize(400, 420)
        customer_form.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout = QVBoxLayout(customer_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setObjectName(u"layout")
        self.lbl_title = QLabel(customer_form)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_title.setFont(font)
        self.lbl_title.setTextFormat(Qt.TextFormat.PlainText)
        self.lbl_title.setScaledContents(False)
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.lbl_title)

        self.frame = QFrame(customer_form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.name_input = QLineEdit(self.frame)
        self.name_input.setObjectName(u"name_input")

        self.verticalLayout_2.addWidget(self.name_input)

        self.email_input = QLineEdit(self.frame)
        self.email_input.setObjectName(u"email_input")

        self.verticalLayout_2.addWidget(self.email_input)

        self.phone_input = QLineEdit(self.frame)
        self.phone_input.setObjectName(u"phone_input")

        self.verticalLayout_2.addWidget(self.phone_input)


        self.layout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignVCenter)

        self.save_btn = QPushButton(customer_form)
        self.save_btn.setObjectName(u"save_btn")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.save_btn.setFont(font1)

        self.layout.addWidget(self.save_btn)


        self.verticalLayout.addLayout(self.layout)


        self.retranslateUi(customer_form)

        QMetaObject.connectSlotsByName(customer_form)
    # setupUi

    def retranslateUi(self, customer_form):
        customer_form.setWindowTitle(QCoreApplication.translate("customer_form", u"Cadastro de Cliente", None))
        self.lbl_title.setText(QCoreApplication.translate("customer_form", u"Cadastrar Novo Cliente", None))
        self.name_input.setPlaceholderText(QCoreApplication.translate("customer_form", u"Nome", None))
        self.email_input.setPlaceholderText(QCoreApplication.translate("customer_form", u"Email", None))
        self.phone_input.setPlaceholderText(QCoreApplication.translate("customer_form", u"Telefone", None))
        self.save_btn.setText(QCoreApplication.translate("customer_form", u"Salvar", None))
    # retranslateUi

