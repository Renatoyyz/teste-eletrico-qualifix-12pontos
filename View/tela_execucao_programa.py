# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/tela_execucao_programa.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaExecucao(object):
    def setupUi(self, TelaExecucao):
        TelaExecucao.setObjectName("TelaExecucao")
        TelaExecucao.resize(1024, 768)
        self.btVoltar = QtWidgets.QPushButton(TelaExecucao)
        self.btVoltar.setGeometry(QtCore.QRect(880, 720, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btVoltar.setFont(font)
        self.btVoltar.setObjectName("btVoltar")
        self.lbImgEsquerdo = QtWidgets.QLabel(TelaExecucao)
        self.lbImgEsquerdo.setGeometry(QtCore.QRect(3, 110, 420, 600))
        self.lbImgEsquerdo.setStyleSheet("background-color: rgb(171, 171, 171);")
        self.lbImgEsquerdo.setObjectName("lbImgEsquerdo")
        self.lbImgDireito = QtWidgets.QLabel(TelaExecucao)
        self.lbImgDireito.setGeometry(QtCore.QRect(601, 110, 420, 600))
        self.lbImgDireito.setStyleSheet("background-color: rgb(171, 171, 171);")
        self.lbImgDireito.setObjectName("lbImgDireito")
        self.lbNomePrograma = QtWidgets.QLabel(TelaExecucao)
        self.lbNomePrograma.setGeometry(QtCore.QRect(335, 10, 351, 22))
        self.lbNomePrograma.setObjectName("lbNomePrograma")
        self.btFinalizar = QtWidgets.QPushButton(TelaExecucao)
        self.btFinalizar.setGeometry(QtCore.QRect(520, 720, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btFinalizar.setFont(font)
        self.btFinalizar.setObjectName("btFinalizar")
        self.btPausar = QtWidgets.QPushButton(TelaExecucao)
        self.btPausar.setGeometry(QtCore.QRect(360, 720, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btPausar.setFont(font)
        self.btPausar.setObjectName("btPausar")
        self.btIniciar = QtWidgets.QPushButton(TelaExecucao)
        self.btIniciar.setGeometry(QtCore.QRect(0, 720, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btIniciar.setFont(font)
        self.btIniciar.setObjectName("btIniciar")
        self.lbEletrodo1_E = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo1_E.setEnabled(True)
        self.lbEletrodo1_E.setGeometry(QtCore.QRect(50, 150, 18, 18))
        self.lbEletrodo1_E.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo1_E.setMidLineWidth(1)
        self.lbEletrodo1_E.setObjectName("lbEletrodo1_E")
        self.lbEletrodo2_E = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo2_E.setEnabled(True)
        self.lbEletrodo2_E.setGeometry(QtCore.QRect(70, 150, 18, 18))
        self.lbEletrodo2_E.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo2_E.setMidLineWidth(1)
        self.lbEletrodo2_E.setObjectName("lbEletrodo2_E")
        self.lbEletrodo3_E = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo3_E.setEnabled(True)
        self.lbEletrodo3_E.setGeometry(QtCore.QRect(90, 150, 18, 18))
        self.lbEletrodo3_E.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo3_E.setMidLineWidth(1)
        self.lbEletrodo3_E.setObjectName("lbEletrodo3_E")
        self.lbEletrodo4_E = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo4_E.setEnabled(True)
        self.lbEletrodo4_E.setGeometry(QtCore.QRect(110, 150, 18, 18))
        self.lbEletrodo4_E.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo4_E.setMidLineWidth(1)
        self.lbEletrodo4_E.setObjectName("lbEletrodo4_E")
        self.lbEletrodo5_E = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo5_E.setEnabled(True)
        self.lbEletrodo5_E.setGeometry(QtCore.QRect(130, 150, 18, 18))
        self.lbEletrodo5_E.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo5_E.setMidLineWidth(1)
        self.lbEletrodo5_E.setObjectName("lbEletrodo5_E")
        self.lbEletrodo6_E = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo6_E.setEnabled(True)
        self.lbEletrodo6_E.setGeometry(QtCore.QRect(150, 150, 18, 18))
        self.lbEletrodo6_E.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo6_E.setMidLineWidth(1)
        self.lbEletrodo6_E.setObjectName("lbEletrodo6_E")
        self.lbEletrodo7_E = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo7_E.setEnabled(True)
        self.lbEletrodo7_E.setGeometry(QtCore.QRect(170, 150, 18, 18))
        self.lbEletrodo7_E.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo7_E.setMidLineWidth(1)
        self.lbEletrodo7_E.setObjectName("lbEletrodo7_E")
        self.lbEletrodo8_E = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo8_E.setEnabled(True)
        self.lbEletrodo8_E.setGeometry(QtCore.QRect(190, 150, 18, 18))
        self.lbEletrodo8_E.setStyleSheet("background-color: rgb(0, 255, 0);;")
        self.lbEletrodo8_E.setMidLineWidth(1)
        self.lbEletrodo8_E.setObjectName("lbEletrodo8_E")
        self.lbEletrodo1_D = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo1_D.setEnabled(True)
        self.lbEletrodo1_D.setGeometry(QtCore.QRect(715, 150, 18, 18))
        self.lbEletrodo1_D.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo1_D.setMidLineWidth(1)
        self.lbEletrodo1_D.setObjectName("lbEletrodo1_D")
        self.lbEletrodo4_D = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo4_D.setEnabled(True)
        self.lbEletrodo4_D.setGeometry(QtCore.QRect(775, 150, 18, 18))
        self.lbEletrodo4_D.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo4_D.setMidLineWidth(1)
        self.lbEletrodo4_D.setObjectName("lbEletrodo4_D")
        self.lbEletrodo8_D = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo8_D.setEnabled(True)
        self.lbEletrodo8_D.setGeometry(QtCore.QRect(855, 150, 18, 18))
        self.lbEletrodo8_D.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo8_D.setMidLineWidth(1)
        self.lbEletrodo8_D.setObjectName("lbEletrodo8_D")
        self.lbEletrodo3_D = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo3_D.setEnabled(True)
        self.lbEletrodo3_D.setGeometry(QtCore.QRect(755, 150, 18, 18))
        self.lbEletrodo3_D.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo3_D.setMidLineWidth(1)
        self.lbEletrodo3_D.setObjectName("lbEletrodo3_D")
        self.lbEletrodo5_D = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo5_D.setEnabled(True)
        self.lbEletrodo5_D.setGeometry(QtCore.QRect(795, 150, 18, 18))
        self.lbEletrodo5_D.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo5_D.setMidLineWidth(1)
        self.lbEletrodo5_D.setObjectName("lbEletrodo5_D")
        self.lbEletrodo2_D = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo2_D.setEnabled(True)
        self.lbEletrodo2_D.setGeometry(QtCore.QRect(735, 150, 18, 18))
        self.lbEletrodo2_D.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo2_D.setMidLineWidth(1)
        self.lbEletrodo2_D.setObjectName("lbEletrodo2_D")
        self.lbEletrodo7_D = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo7_D.setEnabled(True)
        self.lbEletrodo7_D.setGeometry(QtCore.QRect(835, 150, 18, 18))
        self.lbEletrodo7_D.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo7_D.setMidLineWidth(1)
        self.lbEletrodo7_D.setObjectName("lbEletrodo7_D")
        self.lbEletrodo6_D = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo6_D.setEnabled(True)
        self.lbEletrodo6_D.setGeometry(QtCore.QRect(815, 150, 18, 18))
        self.lbEletrodo6_D.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo6_D.setMidLineWidth(1)
        self.lbEletrodo6_D.setObjectName("lbEletrodo6_D")
        self.label = QtWidgets.QLabel(TelaExecucao)
        self.label.setGeometry(QtCore.QRect(3, 10, 111, 22))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(TelaExecucao)
        self.label_2.setGeometry(QtCore.QRect(3, 40, 120, 22))
        self.label_2.setObjectName("label_2")
        self.txAprovadoE = QtWidgets.QLineEdit(TelaExecucao)
        self.txAprovadoE.setGeometry(QtCore.QRect(126, 4, 70, 30))
        self.txAprovadoE.setReadOnly(True)
        self.txAprovadoE.setObjectName("txAprovadoE")
        self.txReprovadoE = QtWidgets.QLineEdit(TelaExecucao)
        self.txReprovadoE.setGeometry(QtCore.QRect(125, 37, 70, 30))
        self.txReprovadoE.setReadOnly(True)
        self.txReprovadoE.setObjectName("txReprovadoE")
        self.txRetrabalhoE = QtWidgets.QLineEdit(TelaExecucao)
        self.txRetrabalhoE.setGeometry(QtCore.QRect(125, 70, 70, 30))
        self.txRetrabalhoE.setReadOnly(True)
        self.txRetrabalhoE.setObjectName("txRetrabalhoE")
        self.label_4 = QtWidgets.QLabel(TelaExecucao)
        self.label_4.setGeometry(QtCore.QRect(3, 73, 120, 22))
        self.label_4.setObjectName("label_4")
        self.lbContinuIndicaE = QtWidgets.QLabel(TelaExecucao)
        self.lbContinuIndicaE.setGeometry(QtCore.QRect(210, 10, 110, 40))
        self.lbContinuIndicaE.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.lbContinuIndicaE.setObjectName("lbContinuIndicaE")
        self.lbIsolaIndicaE = QtWidgets.QLabel(TelaExecucao)
        self.lbIsolaIndicaE.setGeometry(QtCore.QRect(210, 60, 110, 40))
        self.lbIsolaIndicaE.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.lbIsolaIndicaE.setObjectName("lbIsolaIndicaE")
        self.txRetrabalhoD = QtWidgets.QLineEdit(TelaExecucao)
        self.txRetrabalhoD.setGeometry(QtCore.QRect(950, 70, 70, 30))
        self.txRetrabalhoD.setReadOnly(True)
        self.txRetrabalhoD.setObjectName("txRetrabalhoD")
        self.txReprovadoD = QtWidgets.QLineEdit(TelaExecucao)
        self.txReprovadoD.setGeometry(QtCore.QRect(950, 37, 70, 30))
        self.txReprovadoD.setReadOnly(True)
        self.txReprovadoD.setObjectName("txReprovadoD")
        self.label_6 = QtWidgets.QLabel(TelaExecucao)
        self.label_6.setGeometry(QtCore.QRect(828, 10, 111, 22))
        self.label_6.setObjectName("label_6")
        self.txAprovadoD = QtWidgets.QLineEdit(TelaExecucao)
        self.txAprovadoD.setGeometry(QtCore.QRect(951, 4, 70, 30))
        self.txAprovadoD.setReadOnly(True)
        self.txAprovadoD.setObjectName("txAprovadoD")
        self.label_7 = QtWidgets.QLabel(TelaExecucao)
        self.label_7.setGeometry(QtCore.QRect(828, 73, 120, 22))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(TelaExecucao)
        self.label_8.setGeometry(QtCore.QRect(828, 40, 120, 22))
        self.label_8.setObjectName("label_8")
        self.lbIsolaIndicaD = QtWidgets.QLabel(TelaExecucao)
        self.lbIsolaIndicaD.setGeometry(QtCore.QRect(706, 60, 110, 40))
        self.lbIsolaIndicaD.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.lbIsolaIndicaD.setObjectName("lbIsolaIndicaD")
        self.lbContinuIndicaD = QtWidgets.QLabel(TelaExecucao)
        self.lbContinuIndicaD.setGeometry(QtCore.QRect(706, 10, 110, 40))
        self.lbContinuIndicaD.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.lbContinuIndicaD.setObjectName("lbContinuIndicaD")
        self.btDesHabEsquerdo = QtWidgets.QPushButton(TelaExecucao)
        self.btDesHabEsquerdo.setGeometry(QtCore.QRect(178, 720, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btDesHabEsquerdo.setFont(font)
        self.btDesHabEsquerdo.setObjectName("btDesHabEsquerdo")
        self.btDesHabDireito = QtWidgets.QPushButton(TelaExecucao)
        self.btDesHabDireito.setGeometry(QtCore.QRect(680, 720, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btDesHabDireito.setFont(font)
        self.btDesHabDireito.setObjectName("btDesHabDireito")
        self.lbDataHora = QtWidgets.QLabel(TelaExecucao)
        self.lbDataHora.setGeometry(QtCore.QRect(420, 45, 180, 22))
        self.lbDataHora.setObjectName("lbDataHora")
        self.txNumerosCiclos = QtWidgets.QLineEdit(TelaExecucao)
        self.txNumerosCiclos.setGeometry(QtCore.QRect(474, 280, 70, 30))
        self.txNumerosCiclos.setReadOnly(True)
        self.txNumerosCiclos.setObjectName("txNumerosCiclos")
        self.label_5 = QtWidgets.QLabel(TelaExecucao)
        self.label_5.setGeometry(QtCore.QRect(475, 250, 70, 22))
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(TelaExecucao)
        self.label_9.setGeometry(QtCore.QRect(475, 340, 70, 22))
        self.label_9.setObjectName("label_9")
        self.txTempoCiclos = QtWidgets.QLineEdit(TelaExecucao)
        self.txTempoCiclos.setGeometry(QtCore.QRect(474, 370, 70, 30))
        self.txTempoCiclos.setReadOnly(True)
        self.txTempoCiclos.setObjectName("txTempoCiclos")
        self.btContato = QtWidgets.QPushButton(TelaExecucao)
        self.btContato.setGeometry(QtCore.QRect(443, 450, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btContato.setFont(font)
        self.btContato.setObjectName("btContato")
        self.lbAvisos = QtWidgets.QLabel(TelaExecucao)
        self.lbAvisos.setGeometry(QtCore.QRect(335, 80, 351, 22))
        self.lbAvisos.setObjectName("lbAvisos")
        self.btRetrabalhar = QtWidgets.QPushButton(TelaExecucao)
        self.btRetrabalhar.setGeometry(QtCore.QRect(432, 660, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btRetrabalhar.setFont(font)
        self.btRetrabalhar.setObjectName("btRetrabalhar")
        self.btDescartar = QtWidgets.QPushButton(TelaExecucao)
        self.btDescartar.setGeometry(QtCore.QRect(432, 610, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btDescartar.setFont(font)
        self.btDescartar.setObjectName("btDescartar")
        self.lbEletrodo10_E = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo10_E.setEnabled(True)
        self.lbEletrodo10_E.setGeometry(QtCore.QRect(230, 150, 18, 18))
        self.lbEletrodo10_E.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo10_E.setMidLineWidth(1)
        self.lbEletrodo10_E.setObjectName("lbEletrodo10_E")
        self.lbEletrodo9_E = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo9_E.setEnabled(True)
        self.lbEletrodo9_E.setGeometry(QtCore.QRect(210, 150, 18, 18))
        self.lbEletrodo9_E.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo9_E.setMidLineWidth(1)
        self.lbEletrodo9_E.setObjectName("lbEletrodo9_E")
        self.lbEletrodo11_E = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo11_E.setEnabled(True)
        self.lbEletrodo11_E.setGeometry(QtCore.QRect(250, 150, 18, 18))
        self.lbEletrodo11_E.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo11_E.setMidLineWidth(1)
        self.lbEletrodo11_E.setObjectName("lbEletrodo11_E")
        self.lbEletrodo12_E = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo12_E.setEnabled(True)
        self.lbEletrodo12_E.setGeometry(QtCore.QRect(270, 150, 18, 18))
        self.lbEletrodo12_E.setStyleSheet("background-color: rgb(0, 255, 0);;")
        self.lbEletrodo12_E.setMidLineWidth(1)
        self.lbEletrodo12_E.setObjectName("lbEletrodo12_E")
        self.lbEletrodo9_D = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo9_D.setEnabled(True)
        self.lbEletrodo9_D.setGeometry(QtCore.QRect(880, 150, 18, 18))
        self.lbEletrodo9_D.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo9_D.setMidLineWidth(1)
        self.lbEletrodo9_D.setObjectName("lbEletrodo9_D")
        self.lbEletrodo10_D = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo10_D.setEnabled(True)
        self.lbEletrodo10_D.setGeometry(QtCore.QRect(900, 150, 18, 18))
        self.lbEletrodo10_D.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo10_D.setMidLineWidth(1)
        self.lbEletrodo10_D.setObjectName("lbEletrodo10_D")
        self.lbEletrodo12_D = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo12_D.setEnabled(True)
        self.lbEletrodo12_D.setGeometry(QtCore.QRect(940, 150, 18, 18))
        self.lbEletrodo12_D.setStyleSheet("background-color: rgb(0, 255, 0);;")
        self.lbEletrodo12_D.setMidLineWidth(1)
        self.lbEletrodo12_D.setObjectName("lbEletrodo12_D")
        self.lbEletrodo11_D = QtWidgets.QLabel(TelaExecucao)
        self.lbEletrodo11_D.setEnabled(True)
        self.lbEletrodo11_D.setGeometry(QtCore.QRect(920, 150, 18, 18))
        self.lbEletrodo11_D.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo11_D.setMidLineWidth(1)
        self.lbEletrodo11_D.setObjectName("lbEletrodo11_D")
        self.cbMolaEsquerda = QtWidgets.QCheckBox(TelaExecucao)
        self.cbMolaEsquerda.setGeometry(QtCore.QRect(430, 500, 160, 40))
        self.cbMolaEsquerda.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"border-color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(192, 191, 188);")
        self.cbMolaEsquerda.setChecked(True)
        self.cbMolaEsquerda.setObjectName("cbMolaEsquerda")
        self.cbMolaDireita = QtWidgets.QCheckBox(TelaExecucao)
        self.cbMolaDireita.setGeometry(QtCore.QRect(431, 560, 160, 40))
        self.cbMolaDireita.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbMolaDireita.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"alternate-background-color: rgb(192, 191, 188);")
        self.cbMolaDireita.setChecked(True)
        self.cbMolaDireita.setObjectName("cbMolaDireita")

        self.retranslateUi(TelaExecucao)
        QtCore.QMetaObject.connectSlotsByName(TelaExecucao)

    def retranslateUi(self, TelaExecucao):
        _translate = QtCore.QCoreApplication.translate
        TelaExecucao.setWindowTitle(_translate("TelaExecucao", "TelaCriaReceita"))
        self.btVoltar.setText(_translate("TelaExecucao", "VOLTAR"))
        self.lbImgEsquerdo.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\">Clique para configurar o lado esquerdo</p></body></html>"))
        self.lbImgDireito.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\">Clique para configurar o lado direito</p></body></html>"))
        self.lbNomePrograma.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\">Nome do Programa</p></body></html>"))
        self.btFinalizar.setText(_translate("TelaExecucao", "FINALIZAR"))
        self.btPausar.setText(_translate("TelaExecucao", "PAUSAR"))
        self.btIniciar.setText(_translate("TelaExecucao", "INICIAR"))
        self.lbEletrodo1_E.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">1</span></p></body></html>"))
        self.lbEletrodo2_E.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">2</span></p></body></html>"))
        self.lbEletrodo3_E.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">3</span></p></body></html>"))
        self.lbEletrodo4_E.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">4</span></p></body></html>"))
        self.lbEletrodo5_E.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">5</span></p></body></html>"))
        self.lbEletrodo6_E.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">6</span></p></body></html>"))
        self.lbEletrodo7_E.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">7</span></p></body></html>"))
        self.lbEletrodo8_E.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">8</span></p></body></html>"))
        self.lbEletrodo1_D.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">1</span></p></body></html>"))
        self.lbEletrodo4_D.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">4</span></p></body></html>"))
        self.lbEletrodo8_D.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">8</span></p></body></html>"))
        self.lbEletrodo3_D.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">3</span></p></body></html>"))
        self.lbEletrodo5_D.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">5</span></p></body></html>"))
        self.lbEletrodo2_D.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">2</span></p></body></html>"))
        self.lbEletrodo7_D.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">7</span></p></body></html>"))
        self.lbEletrodo6_D.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">6</span></p></body></html>"))
        self.label.setText(_translate("TelaExecucao", "Peça Aprovada"))
        self.label_2.setText(_translate("TelaExecucao", "Peça Reprovada"))
        self.txAprovadoE.setText(_translate("TelaExecucao", "0"))
        self.txReprovadoE.setText(_translate("TelaExecucao", "0"))
        self.txRetrabalhoE.setText(_translate("TelaExecucao", "0"))
        self.label_4.setText(_translate("TelaExecucao", "Peça Retrabalho"))
        self.lbContinuIndicaE.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\">Continuidade</p></body></html>"))
        self.lbIsolaIndicaE.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\">Isolação</p></body></html>"))
        self.txRetrabalhoD.setText(_translate("TelaExecucao", "0"))
        self.txReprovadoD.setText(_translate("TelaExecucao", "0"))
        self.label_6.setText(_translate("TelaExecucao", "Peça Aprovada"))
        self.txAprovadoD.setText(_translate("TelaExecucao", "0"))
        self.label_7.setText(_translate("TelaExecucao", "Peça Retrabalho"))
        self.label_8.setText(_translate("TelaExecucao", "Peça Reprovada"))
        self.lbIsolaIndicaD.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\">Isolação</p></body></html>"))
        self.lbContinuIndicaD.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\">Continuidade</p></body></html>"))
        self.btDesHabEsquerdo.setText(_translate("TelaExecucao", "DESABILITAR ESQUERDO"))
        self.btDesHabDireito.setText(_translate("TelaExecucao", "DESABILITAR DIREITO"))
        self.lbDataHora.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>"))
        self.txNumerosCiclos.setText(_translate("TelaExecucao", "0"))
        self.label_5.setText(_translate("TelaExecucao", "No Ciclos"))
        self.label_9.setText(_translate("TelaExecucao", "Tempo s"))
        self.txTempoCiclos.setText(_translate("TelaExecucao", "0"))
        self.btContato.setText(_translate("TelaExecucao", "CONTATO"))
        self.lbAvisos.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\">Nome do Programa</p></body></html>"))
        self.btRetrabalhar.setText(_translate("TelaExecucao", "RETRABALHAR"))
        self.btDescartar.setText(_translate("TelaExecucao", "DESCARTAR"))
        self.lbEletrodo10_E.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">10</span></p></body></html>"))
        self.lbEletrodo9_E.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">9</span></p></body></html>"))
        self.lbEletrodo11_E.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">11</span></p></body></html>"))
        self.lbEletrodo12_E.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">12</span></p></body></html>"))
        self.lbEletrodo9_D.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">9</span></p></body></html>"))
        self.lbEletrodo10_D.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">10</span></p></body></html>"))
        self.lbEletrodo12_D.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">12</span></p></body></html>"))
        self.lbEletrodo11_D.setText(_translate("TelaExecucao", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">11</span></p></body></html>"))
        self.cbMolaEsquerda.setText(_translate("TelaExecucao", "  MOLA ESQUERDA"))
        self.cbMolaDireita.setText(_translate("TelaExecucao", "    MOLA DIREITA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaExecucao = QtWidgets.QWidget()
    ui = Ui_TelaExecucao()
    ui.setupUi(TelaExecucao)
    TelaExecucao.show()
    sys.exit(app.exec_())
