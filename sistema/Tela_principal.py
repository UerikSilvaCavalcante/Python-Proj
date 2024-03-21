# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTableView, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(884, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 141, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_pg_home = QPushButton(self.centralwidget)
        self.btn_pg_home.setObjectName(u"btn_pg_home")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pg_home.sizePolicy().hasHeightForWidth())
        self.btn_pg_home.setSizePolicy(sizePolicy)
        self.btn_pg_home.setMinimumSize(QSize(0, 30))
        self.btn_pg_home.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(12)
        font.setBold(True)
        self.btn_pg_home.setFont(font)
        self.btn_pg_home.setStyleSheet(u"QPushButton{background-color: #0A601B;\n"
"color: white;\n"
"border: none; border-radius: 5px;}\n"
" QPushButton:hover{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;}")

        self.horizontalLayout.addWidget(self.btn_pg_home)

        self.btn_pg_estoque = QPushButton(self.centralwidget)
        self.btn_pg_estoque.setObjectName(u"btn_pg_estoque")
        sizePolicy.setHeightForWidth(self.btn_pg_estoque.sizePolicy().hasHeightForWidth())
        self.btn_pg_estoque.setSizePolicy(sizePolicy)
        self.btn_pg_estoque.setMinimumSize(QSize(0, 30))
        self.btn_pg_estoque.setMaximumSize(QSize(16777215, 40))
        self.btn_pg_estoque.setFont(font)
        self.btn_pg_estoque.setStyleSheet(u"QPushButton{background-color: #0A601B;\n"
"color: white;\n"
"border: none; border-radius: 5px;}\n"
" QPushButton:hover{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;}")

        self.horizontalLayout.addWidget(self.btn_pg_estoque)

        self.btn_pg_cad_produto = QPushButton(self.centralwidget)
        self.btn_pg_cad_produto.setObjectName(u"btn_pg_cad_produto")
        sizePolicy.setHeightForWidth(self.btn_pg_cad_produto.sizePolicy().hasHeightForWidth())
        self.btn_pg_cad_produto.setSizePolicy(sizePolicy)
        self.btn_pg_cad_produto.setMinimumSize(QSize(0, 30))
        self.btn_pg_cad_produto.setMaximumSize(QSize(16777215, 40))
        self.btn_pg_cad_produto.setFont(font)
        self.btn_pg_cad_produto.setStyleSheet(u"QPushButton{background-color: #0A601B;\n"
"color: white;\n"
"border: none; border-radius: 5px;}\n"
" QPushButton:hover{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;}")

        self.horizontalLayout.addWidget(self.btn_pg_cad_produto)

        self.btn_pg_orc = QPushButton(self.centralwidget)
        self.btn_pg_orc.setObjectName(u"btn_pg_orc")
        sizePolicy.setHeightForWidth(self.btn_pg_orc.sizePolicy().hasHeightForWidth())
        self.btn_pg_orc.setSizePolicy(sizePolicy)
        self.btn_pg_orc.setMinimumSize(QSize(0, 30))
        self.btn_pg_orc.setMaximumSize(QSize(16777215, 40))
        self.btn_pg_orc.setFont(font)
        self.btn_pg_orc.setStyleSheet(u"QPushButton{background-color: #0A601B;\n"
"color: white;\n"
"border: none; border-radius: 5px;}\n"
" QPushButton:hover{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;}")

        self.horizontalLayout.addWidget(self.btn_pg_orc)

        self.btn_pg_sobre = QPushButton(self.centralwidget)
        self.btn_pg_sobre.setObjectName(u"btn_pg_sobre")
        sizePolicy.setHeightForWidth(self.btn_pg_sobre.sizePolicy().hasHeightForWidth())
        self.btn_pg_sobre.setSizePolicy(sizePolicy)
        self.btn_pg_sobre.setMinimumSize(QSize(0, 30))
        self.btn_pg_sobre.setMaximumSize(QSize(16777215, 40))
        self.btn_pg_sobre.setFont(font)
        self.btn_pg_sobre.setStyleSheet(u"QPushButton{background-color: #0A601B;\n"
"color: white;\n"
"border: none; border-radius: 5px;}\n"
" QPushButton:hover{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;}")

        self.horizontalLayout.addWidget(self.btn_pg_sobre)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy1)
        self.Pages.setMinimumSize(QSize(0, 500))
        self.Pages.setMaximumSize(QSize(16777215, 500))
        self.Pages.setStyleSheet(u"color: white;\n"
"background-color: rgb(173, 202, 155);")
        self.Pages.setFrameShape(QFrame.Box)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_2 = QVBoxLayout(self.home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_11.addWidget(self.label)

        self.btn_pg_cd_usu = QPushButton(self.frame)
        self.btn_pg_cd_usu.setObjectName(u"btn_pg_cd_usu")
        sizePolicy.setHeightForWidth(self.btn_pg_cd_usu.sizePolicy().hasHeightForWidth())
        self.btn_pg_cd_usu.setSizePolicy(sizePolicy)
        self.btn_pg_cd_usu.setMinimumSize(QSize(0, 30))
        self.btn_pg_cd_usu.setMaximumSize(QSize(16777215, 40))
        self.btn_pg_cd_usu.setFont(font)
        self.btn_pg_cd_usu.setStyleSheet(u"QPushButton{background-color: #0A601B;\n"
"color: white;\n"
"border: none; border-radius: 5px;}\n"
" QPushButton:hover{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;}")

        self.verticalLayout_11.addWidget(self.btn_pg_cd_usu)


        self.verticalLayout_2.addWidget(self.frame)

        self.Pages.addWidget(self.home)
        self.pg_estoque = QWidget()
        self.pg_estoque.setObjectName(u"pg_estoque")
        self.verticalLayout_10 = QVBoxLayout(self.pg_estoque)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_28 = QLabel(self.pg_estoque)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_10.addWidget(self.label_28)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.pg_estoque)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(650, 0))
        self.frame_2.setMaximumSize(QSize(415, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(36, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.txt_cod = QLineEdit(self.frame_2)
        self.txt_cod.setObjectName(u"txt_cod")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.txt_cod.sizePolicy().hasHeightForWidth())
        self.txt_cod.setSizePolicy(sizePolicy4)
        self.txt_cod.setMinimumSize(QSize(0, 0))
        self.txt_cod.setMaximumSize(QSize(63, 20))
        self.txt_cod.setStyleSheet(u"background-color: white; color: black;")

        self.verticalLayout_3.addWidget(self.txt_cod)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setFont(font)

        self.verticalLayout_7.addWidget(self.label_6)

        self.txt_quant = QSpinBox(self.frame_2)
        self.txt_quant.setObjectName(u"txt_quant")
        sizePolicy4.setHeightForWidth(self.txt_quant.sizePolicy().hasHeightForWidth())
        self.txt_quant.setSizePolicy(sizePolicy4)
        self.txt_quant.setMinimumSize(QSize(73, 0))
        self.txt_quant.setMaximumSize(QSize(40, 16777215))
        self.txt_quant.setStyleSheet(u"background-color: white; color: black;")

        self.verticalLayout_7.addWidget(self.txt_quant)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setFont(font)

        self.verticalLayout_8.addWidget(self.label_5)

        self.txt_preco = QDoubleSpinBox(self.frame_2)
        self.txt_preco.setObjectName(u"txt_preco")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.txt_preco.sizePolicy().hasHeightForWidth())
        self.txt_preco.setSizePolicy(sizePolicy5)
        self.txt_preco.setMinimumSize(QSize(0, 0))
        self.txt_preco.setMaximumSize(QSize(74, 16777215))
        self.txt_preco.setStyleSheet(u"background-color: white; color: black;")
        self.txt_preco.setMaximum(5000.000000000000000)

        self.verticalLayout_8.addWidget(self.txt_preco)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_4.addWidget(self.label_4)

        self.txt_tipo = QLineEdit(self.frame_2)
        self.txt_tipo.setObjectName(u"txt_tipo")
        sizePolicy5.setHeightForWidth(self.txt_tipo.sizePolicy().hasHeightForWidth())
        self.txt_tipo.setSizePolicy(sizePolicy5)
        self.txt_tipo.setMaximumSize(QSize(300, 16777215))
        self.txt_tipo.setStyleSheet(u"background-color: white; color: black;")

        self.verticalLayout_4.addWidget(self.txt_tipo)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_5.addWidget(self.label_3)

        self.txt_nome_prod = QLineEdit(self.frame_2)
        self.txt_nome_prod.setObjectName(u"txt_nome_prod")
        sizePolicy5.setHeightForWidth(self.txt_nome_prod.sizePolicy().hasHeightForWidth())
        self.txt_nome_prod.setSizePolicy(sizePolicy5)
        self.txt_nome_prod.setMaximumSize(QSize(300, 16777215))
        self.txt_nome_prod.setStyleSheet(u"background-color: white; color: black;")

        self.verticalLayout_5.addWidget(self.txt_nome_prod)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_20.addLayout(self.verticalLayout_6)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_altera_estoque = QPushButton(self.pg_estoque)
        self.btn_altera_estoque.setObjectName(u"btn_altera_estoque")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_altera_estoque.sizePolicy().hasHeightForWidth())
        self.btn_altera_estoque.setSizePolicy(sizePolicy6)
        self.btn_altera_estoque.setMinimumSize(QSize(150, 17))
        self.btn_altera_estoque.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setBold(True)
        self.btn_altera_estoque.setFont(font1)
        self.btn_altera_estoque.setStyleSheet(u"\n"
" QPushButton{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;\n"
"border-radius: 5px;}\n"
"QPushButton:hover{background-color: #0A601B;\n"
"color: white;\n"
"border: none;}")

        self.verticalLayout_9.addWidget(self.btn_altera_estoque)

        self.btn_deleta_estoque = QPushButton(self.pg_estoque)
        self.btn_deleta_estoque.setObjectName(u"btn_deleta_estoque")
        sizePolicy6.setHeightForWidth(self.btn_deleta_estoque.sizePolicy().hasHeightForWidth())
        self.btn_deleta_estoque.setSizePolicy(sizePolicy6)
        self.btn_deleta_estoque.setMinimumSize(QSize(150, 17))
        self.btn_deleta_estoque.setMaximumSize(QSize(16777215, 30))
        self.btn_deleta_estoque.setFont(font1)
        self.btn_deleta_estoque.setStyleSheet(u"\n"
" QPushButton{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;\n"
"border-radius: 5px;}\n"
"QPushButton:hover{background-color: #0A601B;\n"
"color: white;\n"
"border: none;}")

        self.verticalLayout_9.addWidget(self.btn_deleta_estoque)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(39, 47, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.tb_estoque = QTableView(self.pg_estoque)
        self.tb_estoque.setObjectName(u"tb_estoque")
        self.tb_estoque.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: black")
        self.tb_estoque.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tb_estoque.horizontalHeader().setMinimumSectionSize(39)
        self.tb_estoque.horizontalHeader().setDefaultSectionSize(160)

        self.verticalLayout_10.addWidget(self.tb_estoque)

        self.Pages.addWidget(self.pg_estoque)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.Pages.addWidget(self.page_2)
        self.pg_orc = QWidget()
        self.pg_orc.setObjectName(u"pg_orc")
        self.verticalLayout_20 = QVBoxLayout(self.pg_orc)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_7 = QLabel(self.pg_orc)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: white")

        self.verticalLayout_20.addWidget(self.label_7)

        self.txt_filtro = QLineEdit(self.pg_orc)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setStyleSheet(u"background-color: white; color: black;")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.txt_filtro)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_8 = QLabel(self.pg_orc)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: white")

        self.verticalLayout_12.addWidget(self.label_8)

        self.tw_estoque = QTreeWidget(self.pg_orc)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(4, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setFont(4, font);
        __qtreewidgetitem.setForeground(4, brush);
        __qtreewidgetitem.setFont(3, font);
        __qtreewidgetitem.setFont(2, font);
        __qtreewidgetitem.setFont(1, font);
        __qtreewidgetitem.setFont(0, font);
        self.tw_estoque.setHeaderItem(__qtreewidgetitem)
        self.tw_estoque.setObjectName(u"tw_estoque")
        self.tw_estoque.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: black")
        self.tw_estoque.header().setMinimumSectionSize(31)
        self.tw_estoque.header().setDefaultSectionSize(126)

        self.verticalLayout_12.addWidget(self.tw_estoque)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_9 = QLabel(self.pg_orc)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: white")

        self.verticalLayout_13.addWidget(self.label_9)

        self.tw_pedido = QTreeWidget(self.pg_orc)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setFont(4, font);
        __qtreewidgetitem1.setFont(3, font);
        __qtreewidgetitem1.setFont(2, font);
        __qtreewidgetitem1.setFont(1, font);
        __qtreewidgetitem1.setFont(0, font);
        self.tw_pedido.setHeaderItem(__qtreewidgetitem1)
        self.tw_pedido.setObjectName(u"tw_pedido")
        self.tw_pedido.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: black\n"
"")
        self.tw_pedido.setWordWrap(True)
        self.tw_pedido.header().setCascadingSectionResizes(False)
        self.tw_pedido.header().setDefaultSectionSize(126)
        self.tw_pedido.header().setHighlightSections(False)

        self.verticalLayout_13.addWidget(self.tw_pedido)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)


        self.horizontalLayout_2.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.btn_adiciona = QPushButton(self.pg_orc)
        self.btn_adiciona.setObjectName(u"btn_adiciona")
        sizePolicy.setHeightForWidth(self.btn_adiciona.sizePolicy().hasHeightForWidth())
        self.btn_adiciona.setSizePolicy(sizePolicy)
        self.btn_adiciona.setMinimumSize(QSize(93, 40))
        self.btn_adiciona.setMaximumSize(QSize(16777215, 40))
        self.btn_adiciona.setStyleSheet(u"\n"
" QPushButton{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;\n"
"border-radius: 5px;}\n"
"QPushButton:hover{background-color: #0A601B;\n"
"color: white;\n"
"border: none;}")

        self.verticalLayout_15.addWidget(self.btn_adiciona)

        self.btn_retirar = QPushButton(self.pg_orc)
        self.btn_retirar.setObjectName(u"btn_retirar")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_retirar.sizePolicy().hasHeightForWidth())
        self.btn_retirar.setSizePolicy(sizePolicy7)
        self.btn_retirar.setMinimumSize(QSize(0, 40))
        self.btn_retirar.setMaximumSize(QSize(16777215, 40))
        self.btn_retirar.setStyleSheet(u"\n"
" QPushButton{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;\n"
"border-radius: 5px;}\n"
"QPushButton:hover{background-color: #0A601B;\n"
"color: white;\n"
"border: none;}")

        self.verticalLayout_15.addWidget(self.btn_retirar)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_29 = QLabel(self.pg_orc)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"color: white")

        self.verticalLayout_16.addWidget(self.label_29)

        self.txt_quantidade_orc = QSpinBox(self.pg_orc)
        self.txt_quantidade_orc.setObjectName(u"txt_quantidade_orc")
        self.txt_quantidade_orc.setMinimum(1)
        self.txt_quantidade_orc.setMaximum(100)

        self.verticalLayout_16.addWidget(self.txt_quantidade_orc)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)

        self.verticalSpacer_2 = QSpacerItem(43, 45, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_15)


        self.verticalLayout_20.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.verticalLayout_20.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.pg_orc)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.btn_fecha_orc = QPushButton(self.pg_orc)
        self.btn_fecha_orc.setObjectName(u"btn_fecha_orc")
        sizePolicy7.setHeightForWidth(self.btn_fecha_orc.sizePolicy().hasHeightForWidth())
        self.btn_fecha_orc.setSizePolicy(sizePolicy7)
        self.btn_fecha_orc.setMinimumSize(QSize(0, 40))
        self.btn_fecha_orc.setStyleSheet(u"QPushButton{background-color: #0A601B;\n"
"color: white;\n"
"border: none; border-radius: 5px;}\n"
" QPushButton:hover{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;}")

        self.horizontalLayout_7.addWidget(self.btn_fecha_orc)

        self.label_11 = QLabel(self.pg_orc)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_7.addWidget(self.label_11)


        self.verticalLayout_20.addLayout(self.horizontalLayout_7)

        self.Pages.addWidget(self.pg_orc)
        self.pg_cad_prod = QWidget()
        self.pg_cad_prod.setObjectName(u"pg_cad_prod")
        self.verticalLayout_17 = QVBoxLayout(self.pg_cad_prod)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_12 = QLabel(self.pg_cad_prod)
        self.label_12.setObjectName(u"label_12")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy8)
        self.label_12.setMaximumSize(QSize(16777215, 100))
        self.label_12.setStyleSheet(u"color: white")

        self.verticalLayout_17.addWidget(self.label_12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, -1, -1, -1)
        self.label_13 = QLabel(self.pg_cad_prod)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setMinimumSize(QSize(71, 0))
        self.label_13.setMaximumSize(QSize(100, 16777215))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: white")

        self.horizontalLayout_8.addWidget(self.label_13)

        self.txt_novo_tipo = QLineEdit(self.pg_cad_prod)
        self.txt_novo_tipo.setObjectName(u"txt_novo_tipo")
        self.txt_novo_tipo.setStyleSheet(u"background-color: white; color: black;")

        self.horizontalLayout_8.addWidget(self.txt_novo_tipo)


        self.verticalLayout_17.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, -1, -1, -1)
        self.label_14 = QLabel(self.pg_cad_prod)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: white")

        self.horizontalLayout_9.addWidget(self.label_14)

        self.txt_novo_produto = QLineEdit(self.pg_cad_prod)
        self.txt_novo_produto.setObjectName(u"txt_novo_produto")
        self.txt_novo_produto.setStyleSheet(u"background-color: white; color: black;")

        self.horizontalLayout_9.addWidget(self.txt_novo_produto)


        self.verticalLayout_17.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, -1, -1, -1)
        self.label_15 = QLabel(self.pg_cad_prod)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setMinimumSize(QSize(53, 0))
        self.label_15.setMaximumSize(QSize(71, 16777215))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: white")

        self.horizontalLayout_10.addWidget(self.label_15)

        self.txt_novo_quant = QDoubleSpinBox(self.pg_cad_prod)
        self.txt_novo_quant.setObjectName(u"txt_novo_quant")
        self.txt_novo_quant.setMinimumSize(QSize(0, 0))
        self.txt_novo_quant.setStyleSheet(u"background-color: white; color: black;")
        self.txt_novo_quant.setMaximum(50000.000000000000000)

        self.horizontalLayout_10.addWidget(self.txt_novo_quant)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_16 = QLabel(self.pg_cad_prod)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"color: white")

        self.horizontalLayout_11.addWidget(self.label_16)

        self.txt_quantidade_cad_produto = QSpinBox(self.pg_cad_prod)
        self.txt_quantidade_cad_produto.setObjectName(u"txt_quantidade_cad_produto")
        self.txt_quantidade_cad_produto.setStyleSheet(u"background-color: white; color: black;")

        self.horizontalLayout_11.addWidget(self.txt_quantidade_cad_produto)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)


        self.verticalLayout_17.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_17 = QLabel(self.pg_cad_prod)
        self.label_17.setObjectName(u"label_17")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy9)
        self.label_17.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_13.addWidget(self.label_17)

        self.btn_cad_produto = QPushButton(self.pg_cad_prod)
        self.btn_cad_produto.setObjectName(u"btn_cad_produto")
        sizePolicy7.setHeightForWidth(self.btn_cad_produto.sizePolicy().hasHeightForWidth())
        self.btn_cad_produto.setSizePolicy(sizePolicy7)
        self.btn_cad_produto.setMaximumSize(QSize(16777215, 40))
        self.btn_cad_produto.setStyleSheet(u"QPushButton{background-color: #0A601B;\n"
"color: white;\n"
"border: none; border-radius: 5px;}\n"
" QPushButton:hover{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;}")

        self.horizontalLayout_13.addWidget(self.btn_cad_produto)

        self.label_18 = QLabel(self.pg_cad_prod)
        self.label_18.setObjectName(u"label_18")
        sizePolicy9.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy9)
        self.label_18.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_13.addWidget(self.label_18)


        self.verticalLayout_17.addLayout(self.horizontalLayout_13)

        self.Pages.addWidget(self.pg_cad_prod)
        self.pg_cad_usu = QWidget()
        self.pg_cad_usu.setObjectName(u"pg_cad_usu")
        self.verticalLayout_18 = QVBoxLayout(self.pg_cad_usu)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_19 = QLabel(self.pg_cad_usu)
        self.label_19.setObjectName(u"label_19")
        sizePolicy8.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy8)
        self.label_19.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_18.addWidget(self.label_19)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, -1, -1, -1)
        self.label_24 = QLabel(self.pg_cad_usu)
        self.label_24.setObjectName(u"label_24")
        sizePolicy3.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy3)
        self.label_24.setMaximumSize(QSize(140, 16777215))
        self.label_24.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_24)

        self.txt_nome_usu = QLineEdit(self.pg_cad_usu)
        self.txt_nome_usu.setObjectName(u"txt_nome_usu")
        self.txt_nome_usu.setStyleSheet(u"background-color: white; color: black;")

        self.horizontalLayout_17.addWidget(self.txt_nome_usu)


        self.verticalLayout_18.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(10, -1, -1, -1)
        self.label_22 = QLabel(self.pg_cad_usu)
        self.label_22.setObjectName(u"label_22")
        sizePolicy3.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy3)
        self.label_22.setMinimumSize(QSize(53, 0))
        self.label_22.setMaximumSize(QSize(142, 16777215))
        self.label_22.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_22)

        self.txt_email = QLineEdit(self.pg_cad_usu)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setStyleSheet(u"background-color: white; color: black;")

        self.horizontalLayout_15.addWidget(self.txt_email)


        self.verticalLayout_18.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(10, -1, -1, -1)
        self.label_25 = QLabel(self.pg_cad_usu)
        self.label_25.setObjectName(u"label_25")
        sizePolicy3.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy3)
        self.label_25.setMinimumSize(QSize(71, 0))
        self.label_25.setMaximumSize(QSize(142, 16777215))
        self.label_25.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_25)

        self.txt_senha = QLineEdit(self.pg_cad_usu)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"background-color: white; color: black;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_18.addWidget(self.txt_senha)


        self.verticalLayout_18.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, -1, -1, -1)
        self.label_23 = QLabel(self.pg_cad_usu)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_23)

        self.txt_comfirma_senha = QLineEdit(self.pg_cad_usu)
        self.txt_comfirma_senha.setObjectName(u"txt_comfirma_senha")
        self.txt_comfirma_senha.setStyleSheet(u"background-color: white; color: black;")
        self.txt_comfirma_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_16.addWidget(self.txt_comfirma_senha)


        self.verticalLayout_18.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, -1, -1, -1)
        self.label_30 = QLabel(self.pg_cad_usu)
        self.label_30.setObjectName(u"label_30")
        sizePolicy2.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy2)
        self.label_30.setMinimumSize(QSize(144, 0))
        self.label_30.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_30)

        self.cb_perfil = QComboBox(self.pg_cad_usu)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setStyleSheet(u"background-color: white; color: black;")

        self.horizontalLayout_19.addWidget(self.cb_perfil)


        self.verticalLayout_18.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_20 = QLabel(self.pg_cad_usu)
        self.label_20.setObjectName(u"label_20")
        sizePolicy9.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy9)
        self.label_20.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_14.addWidget(self.label_20)

        self.btn_cad_usu = QPushButton(self.pg_cad_usu)
        self.btn_cad_usu.setObjectName(u"btn_cad_usu")
        sizePolicy7.setHeightForWidth(self.btn_cad_usu.sizePolicy().hasHeightForWidth())
        self.btn_cad_usu.setSizePolicy(sizePolicy7)
        self.btn_cad_usu.setMaximumSize(QSize(16777215, 40))
        self.btn_cad_usu.setStyleSheet(u"QPushButton{background-color: #0A601B;\n"
"color: white;\n"
"border: none; border-radius: 5px;}\n"
" QPushButton:hover{background-color: white;\n"
"color: #0A601B;\n"
"border: 2px solid #0A601B;}")

        self.horizontalLayout_14.addWidget(self.btn_cad_usu)

        self.label_21 = QLabel(self.pg_cad_usu)
        self.label_21.setObjectName(u"label_21")
        sizePolicy9.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy9)
        self.label_21.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_14.addWidget(self.label_21)


        self.verticalLayout_18.addLayout(self.horizontalLayout_14)

        self.Pages.addWidget(self.pg_cad_usu)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_19 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_26 = QLabel(self.pg_sobre)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_19.addWidget(self.label_26)

        self.label_27 = QLabel(self.pg_sobre)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_19.addWidget(self.label_27)

        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 884, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_pg_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_pg_estoque.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.btn_pg_cad_produto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Produto", None))
        self.btn_pg_orc.setText(QCoreApplication.translate("MainWindow", u"Or\u00e7amento", None))
        self.btn_pg_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">EF- Produtos Artesanais</span></p><p align=\"center\"><span style=\" font-size:28pt;\">Sistema</span></p></body></html>", None))
        self.btn_pg_cd_usu.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usuario", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Estoque</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.btn_altera_estoque.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_deleta_estoque.setText(QCoreApplication.translate("MainWindow", u"Deletar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">OR\u00c7AMENTO</span></p></body></html>", None))
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"filtro", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Estoque</span></p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Estoque", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Cod", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Pedido</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tw_pedido.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Estoque", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Cod", None));
        self.btn_adiciona.setText(QCoreApplication.translate("MainWindow", u"Adicinar Produto", None))
        self.btn_retirar.setText(QCoreApplication.translate("MainWindow", u"Retirar Produto", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Quantidade</span></p></body></html>", None))
        self.label_10.setText("")
        self.btn_fecha_orc.setText(QCoreApplication.translate("MainWindow", u"Fechar or\u00e7amento", None))
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Cadastrar Novo Produto</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_17.setText("")
        self.btn_cad_produto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Cadastrar Novo Usuario</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"senha:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Cofirmar Senha:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Perfil: ", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Adiministrador", None))

        self.label_20.setText("")
        self.btn_cad_usu.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_21.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">SOBRE</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Este Sistema foi desenvolvido para fins educativos</span></p></body></html>", None))
    # retranslateUi

