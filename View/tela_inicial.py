# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/tela_inicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaInicial(object):
    def setupUi(self, TelaInicial):
        TelaInicial.setObjectName("TelaInicial")
        TelaInicial.resize(1024, 768)
        self.btIniciar = QtWidgets.QPushButton(TelaInicial)
        self.btIniciar.setGeometry(QtCore.QRect(120, 390, 212, 102))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btIniciar.setFont(font)
        self.btIniciar.setObjectName("btIniciar")
        self.btConfigurar = QtWidgets.QPushButton(TelaInicial)
        self.btConfigurar.setGeometry(QtCore.QRect(700, 390, 212, 102))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btConfigurar.setFont(font)
        self.btConfigurar.setObjectName("btConfigurar")
        self.lbLogo = QtWidgets.QLabel(TelaInicial)
        self.lbLogo.setGeometry(QtCore.QRect(23, 40, 980, 210))
        self.lbLogo.setStyleSheet("border-image: url(:/logo/logo_qualifix.JPG);\n"
"border-image: url(:/logo/logo_qualifix.JPG);")
        self.lbLogo.setText("")
        self.lbLogo.setObjectName("lbLogo")
        self.btDesligarSistema = QtWidgets.QPushButton(TelaInicial)
        self.btDesligarSistema.setGeometry(QtCore.QRect(380, 630, 260, 102))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btDesligarSistema.setFont(font)
        self.btDesligarSistema.setObjectName("btDesligarSistema")

        self.retranslateUi(TelaInicial)
        QtCore.QMetaObject.connectSlotsByName(TelaInicial)

    def retranslateUi(self, TelaInicial):
        _translate = QtCore.QCoreApplication.translate
        TelaInicial.setWindowTitle(_translate("TelaInicial", "Form"))
        self.btIniciar.setText(_translate("TelaInicial", "INICIAR"))
        self.btConfigurar.setText(_translate("TelaInicial", "CONFIGURAR"))
        self.btDesligarSistema.setText(_translate("TelaInicial", "DESLIGAR SISTEMA"))
# import logo_qualifix_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaInicial = QtWidgets.QWidget()
    ui = Ui_TelaInicial()
    ui.setupUi(TelaInicial)
    TelaInicial.show()
    sys.exit(app.exec_())
