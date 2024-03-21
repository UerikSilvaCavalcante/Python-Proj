# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orc.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_orc(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 500)
        Form.setMinimumSize(QSize(700, 500))
        Form.setMaximumSize(QSize(700, 500))
        Form.setStyleSheet(u"background-color: rgb(49, 134, 0, 70);")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setStyleSheet(u"color: black;")

        self.horizontalLayout.addWidget(self.label)

        self.txt_cliente = QLineEdit(Form)
        self.txt_cliente.setObjectName(u"txt_cliente")
        self.txt_cliente.setStyleSheet(u"background-color: white;")

        self.horizontalLayout.addWidget(self.txt_cliente)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 0))
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setStyleSheet(u"color: black;")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setStyleSheet(u"background-color: white;")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(45, 0))
        self.label_5.setStyleSheet(u"color: black;")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.txt_cnpj = QLineEdit(Form)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        self.txt_cnpj.setStyleSheet(u"background-color: white;")
        self.txt_cnpj.setMaxLength(8)

        self.horizontalLayout_3.addWidget(self.txt_cnpj)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_9.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: black;")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.txt_endereo = QLineEdit(Form)
        self.txt_endereo.setObjectName(u"txt_endereo")
        self.txt_endereo.setStyleSheet(u"background-color: white;")

        self.horizontalLayout_6.addWidget(self.txt_endereo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.txt_data = QLabel(Form)
        self.txt_data.setObjectName(u"txt_data")
        self.txt_data.setMaximumSize(QSize(107, 16777215))
        self.txt_data.setStyleSheet(u"color: black;")

        self.horizontalLayout_5.addWidget(self.txt_data)

        self.dateTimeEdit = QDateTimeEdit(Form)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setStyleSheet(u"background-color: white;")
        self.dateTimeEdit.setWrapping(False)
        self.dateTimeEdit.setDateTime(QDateTime(QDate(2000, 1, 5), QTime(3, 0, 0)))
        self.dateTimeEdit.setMaximumTime(QTime(2, 59, 59))
        self.dateTimeEdit.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setTimeSpec(Qt.UTC)

        self.horizontalLayout_5.addWidget(self.dateTimeEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: black;")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.txt_obs = QTextEdit(Form)
        self.txt_obs.setObjectName(u"txt_obs")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txt_obs.sizePolicy().hasHeightForWidth())
        self.txt_obs.setSizePolicy(sizePolicy1)
        self.txt_obs.setMaximumSize(QSize(16777215, 50))
        self.txt_obs.setStyleSheet(u"background-color: white;")

        self.horizontalLayout_4.addWidget(self.txt_obs)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_9.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_pdf = QPushButton(Form)
        self.btn_pdf.setObjectName(u"btn_pdf")
        self.btn_pdf.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(12)
        font.setBold(True)
        self.btn_pdf.setFont(font)
        self.btn_pdf.setStyleSheet(u"QPushButton{background-color: #0A601B;\n"
"color: white;\n"
"border: none; border-radius: 5px;}\n"
" QPushButton:hover{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;}")

        self.horizontalLayout_7.addWidget(self.btn_pdf)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_excel = QPushButton(Form)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(0, 50))
        self.btn_excel.setFont(font)
        self.btn_excel.setStyleSheet(u"QPushButton{background-color: #0A601B;\n"
"color: white;\n"
"border: none; border-radius: 5px;}\n"
" QPushButton:hover{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;}")

        self.horizontalLayout_8.addWidget(self.btn_excel)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.tb_orc_pedido = QTreeWidget(Form)
        self.tb_orc_pedido.setObjectName(u"tb_orc_pedido")
        self.tb_orc_pedido.setFont(font)
        self.tb_orc_pedido.setStyleSheet(u"background-color: white")
        self.tb_orc_pedido.header().setDefaultSectionSize(145)

        self.verticalLayout_3.addWidget(self.tb_orc_pedido)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextDirection(QProgressBar.BottomToTop)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cliente</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Pagamento</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"PIX", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Cart\u00e3o-credito", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Cart\u00e3o-d\u00e9bito", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Dinheiro", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">CNPJ</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Endere\u00e7o</span></p></body></html>", None))
        self.txt_data.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Data de Entrega</span></p></body></html>", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("Form", u"dd/MM/yyyy ", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">OBS</span></p></body></html>", None))
        self.btn_pdf.setText(QCoreApplication.translate("Form", u"Gerar PDF", None))
        self.btn_excel.setText(QCoreApplication.translate("Form", u"Gerar Exel", None))
        ___qtreewidgetitem = self.tb_orc_pedido.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("Form", u"Quantidade", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("Form", u"Pre\u00e7o", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"Produto", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"Tipo", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"Cod", None));
        self.progressBar.setFormat(QCoreApplication.translate("Form", u"%p", None))
    # retranslateUi

