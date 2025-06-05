# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources.icons.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(977, 640)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(0, 0))
        self.sidebar.setMaximumSize(QSize(200, 16777215))
        self.sidebar.setStyleSheet(u"")
        self.sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.sidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnCustomer = QPushButton(self.sidebar)
        self.btnCustomer.setObjectName(u"btnCustomer")

        self.verticalLayout.addWidget(self.btnCustomer)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnQuit = QPushButton(self.sidebar)
        self.btnQuit.setObjectName(u"btnQuit")

        self.verticalLayout.addWidget(self.btnQuit)


        self.horizontalLayout.addWidget(self.sidebar)

        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"")
        self.container.setFrameShape(QFrame.Shape.StyledPanel)
        self.container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.container_header = QFrame(self.container)
        self.container_header.setObjectName(u"container_header")
        self.container_header.setMinimumSize(QSize(0, 80))
        self.container_header.setMaximumSize(QSize(16777215, 80))
        self.container_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.container_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.container_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.toggleSidebar = QPushButton(self.container_header)
        self.toggleSidebar.setObjectName(u"toggleSidebar")
        self.toggleSidebar.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/feather/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toggleSidebar.setIcon(icon)
        self.toggleSidebar.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.toggleSidebar)


        self.verticalLayout_2.addWidget(self.container_header, 0, Qt.AlignmentFlag.AlignLeft)

        self.content = QFrame(self.container)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.content)


        self.horizontalLayout.addWidget(self.container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnCustomer.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btnQuit.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.toggleSidebar.setText("")
    # retranslateUi

