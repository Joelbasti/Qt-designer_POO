# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(613, 372)
        font = QFont()
        font.setBold(True)
        font.setStrikeOut(False)
        vtnPrincipal.setFont(font)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblNombre = QLabel(self.centralwidget)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(40, 20, 91, 41))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.lblNombre.setFont(font1)
        self.lblApellido = QLabel(self.centralwidget)
        self.lblApellido.setObjectName(u"lblApellido")
        self.lblApellido.setGeometry(QRect(40, 60, 91, 31))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.lblApellido.setFont(font2)
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(140, 20, 321, 31))
        self.txtNombre.setMaxLength(20)
        self.txtApellido = QLineEdit(self.centralwidget)
        self.txtApellido.setObjectName(u"txtApellido")
        self.txtApellido.setGeometry(QRect(140, 60, 321, 31))
        self.txtApellido.setMaxLength(20)
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(260, 280, 91, 31))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setStrikeOut(False)
        self.btnGuardar.setFont(font3)
        self.txtCedula = QLineEdit(self.centralwidget)
        self.txtCedula.setObjectName(u"txtCedula")
        self.txtCedula.setGeometry(QRect(140, 100, 131, 31))
        self.txtCedula.setMaxLength(20)
        self.lblCedula = QLabel(self.centralwidget)
        self.lblCedula.setObjectName(u"lblCedula")
        self.lblCedula.setGeometry(QRect(50, 100, 81, 31))
        self.lblCedula.setFont(font2)
        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(440, 280, 91, 31))
        self.btnLimpiar.setFont(font3)
        self.btnSexo = QComboBox(self.centralwidget)
        self.btnSexo.addItem("")
        self.btnSexo.addItem("")
        self.btnSexo.addItem("")
        self.btnSexo.addItem("")
        self.btnSexo.setObjectName(u"btnSexo")
        self.btnSexo.setGeometry(QRect(140, 150, 111, 26))
        self.lblSexo = QLabel(self.centralwidget)
        self.lblSexo.setObjectName(u"lblSexo")
        self.lblSexo.setGeometry(QRect(60, 150, 61, 31))
        self.lblSexo.setFont(font2)
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.lblNombre.raise_()
        self.lblApellido.raise_()
        self.txtApellido.raise_()
        self.btnGuardar.raise_()
        self.txtNombre.raise_()
        self.txtCedula.raise_()
        self.lblCedula.raise_()
        self.btnLimpiar.raise_()
        self.btnSexo.raise_()
        self.lblSexo.raise_()
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 613, 33))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txtNombre, self.txtApellido)
        QWidget.setTabOrder(self.txtApellido, self.btnGuardar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"Sistema de Administracion de persona", None))
        self.lblNombre.setText(QCoreApplication.translate("vtnPrincipal", u"Nombre:", None))
        self.lblApellido.setText(QCoreApplication.translate("vtnPrincipal", u"Apellido:", None))
        self.btnGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"Guardar", None))
        self.lblCedula.setText(QCoreApplication.translate("vtnPrincipal", u"Cedula:", None))
        self.btnLimpiar.setText(QCoreApplication.translate("vtnPrincipal", u"Limpiar", None))
        self.btnSexo.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"Seleccionar", None))
        self.btnSexo.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"Masculino", None))
        self.btnSexo.setItemText(2, QCoreApplication.translate("vtnPrincipal", u"Femenino", None))
        self.btnSexo.setItemText(3, QCoreApplication.translate("vtnPrincipal", u"Prefiero no decirlo", None))

        self.lblSexo.setText(QCoreApplication.translate("vtnPrincipal", u"Sexo:", None))
    # retranslateUi

