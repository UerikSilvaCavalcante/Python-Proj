# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tl_login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_login(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 367)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 23))
        self.label_3.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.label_3)

        self.txt_usuario_log = QLineEdit(self.frame)
        self.txt_usuario_log.setObjectName(u"txt_usuario_log")
        self.txt_usuario_log.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_usuario_log)

        self.txt_senha_log = QLineEdit(self.frame)
        self.txt_senha_log.setObjectName(u"txt_senha_log")
        self.txt_senha_log.setEchoMode(QLineEdit.Password)
        self.txt_senha_log.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_senha_log)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.btn_entrar = QPushButton(Form)
        self.btn_entrar.setObjectName(u"btn_entrar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_entrar.sizePolicy().hasHeightForWidth())
        self.btn_entrar.setSizePolicy(sizePolicy1)
        self.btn_entrar.setMinimumSize(QSize(150, 50))
        self.btn_entrar.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_2.addWidget(self.btn_entrar)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText("")
        self.txt_usuario_log.setPlaceholderText(QCoreApplication.translate("Form", u"Usuario", None))
        self.txt_senha_log.setPlaceholderText(QCoreApplication.translate("Form", u"Senha", None))
        self.label_4.setText("")
        self.label.setText("")
        self.btn_entrar.setText(QCoreApplication.translate("Form", u"Entrar", None))
        self.label_2.setText("")
    # retranslateUi

