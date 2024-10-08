# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/tela_cria_receita.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaCriaReceita(object):
    def setupUi(self, TelaCriaReceita):
        TelaCriaReceita.setObjectName("TelaCriaReceita")
        TelaCriaReceita.resize(1024, 768)
        self.btVoltar = QtWidgets.QPushButton(TelaCriaReceita)
        self.btVoltar.setGeometry(QtCore.QRect(766, 720, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btVoltar.setFont(font)
        self.btVoltar.setObjectName("btVoltar")
        self.lbImgEsquerdo = QtWidgets.QLabel(TelaCriaReceita)
        self.lbImgEsquerdo.setGeometry(QtCore.QRect(62, 60, 420, 600))
        self.lbImgEsquerdo.setStyleSheet("background-color: rgb(171, 171, 171);")
        self.lbImgEsquerdo.setObjectName("lbImgEsquerdo")
        self.lbImgDireito = QtWidgets.QLabel(TelaCriaReceita)
        self.lbImgDireito.setGeometry(QtCore.QRect(542, 60, 420, 600))
        self.lbImgDireito.setStyleSheet("background-color: rgb(171, 171, 171);")
        self.lbImgDireito.setObjectName("lbImgDireito")
        self.txNomePrograma = QtWidgets.QLineEdit(TelaCriaReceita)
        self.txNomePrograma.setGeometry(QtCore.QRect(370, 25, 280, 32))
        self.txNomePrograma.setText("")
        self.txNomePrograma.setObjectName("txNomePrograma")
        self.label = QtWidgets.QLabel(TelaCriaReceita)
        self.label.setGeometry(QtCore.QRect(430, 0, 140, 22))
        self.label.setObjectName("label")
        self.btAtualizar = QtWidgets.QPushButton(TelaCriaReceita)
        self.btAtualizar.setGeometry(QtCore.QRect(606, 720, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btAtualizar.setFont(font)
        self.btAtualizar.setObjectName("btAtualizar")
        self.btApagar = QtWidgets.QPushButton(TelaCriaReceita)
        self.btApagar.setGeometry(QtCore.QRect(446, 720, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btApagar.setFont(font)
        self.btApagar.setObjectName("btApagar")
        self.btSlavar = QtWidgets.QPushButton(TelaCriaReceita)
        self.btSlavar.setGeometry(QtCore.QRect(286, 720, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btSlavar.setFont(font)
        self.btSlavar.setObjectName("btSlavar")
        self.btLocalizar = QtWidgets.QPushButton(TelaCriaReceita)
        self.btLocalizar.setGeometry(QtCore.QRect(126, 720, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btLocalizar.setFont(font)
        self.btLocalizar.setObjectName("btLocalizar")
        self.lbEletrodo1_Esque = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo1_Esque.setEnabled(True)
        self.lbEletrodo1_Esque.setGeometry(QtCore.QRect(60, 20, 18, 18))
        self.lbEletrodo1_Esque.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo1_Esque.setMidLineWidth(1)
        self.lbEletrodo1_Esque.setObjectName("lbEletrodo1_Esque")
        self.lbEletrodo2_Esque = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo2_Esque.setEnabled(True)
        self.lbEletrodo2_Esque.setGeometry(QtCore.QRect(80, 20, 18, 18))
        self.lbEletrodo2_Esque.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo2_Esque.setMidLineWidth(1)
        self.lbEletrodo2_Esque.setObjectName("lbEletrodo2_Esque")
        self.lbEletrodo3_Esque = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo3_Esque.setEnabled(True)
        self.lbEletrodo3_Esque.setGeometry(QtCore.QRect(100, 20, 18, 18))
        self.lbEletrodo3_Esque.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo3_Esque.setMidLineWidth(1)
        self.lbEletrodo3_Esque.setObjectName("lbEletrodo3_Esque")
        self.lbEletrodo4_Esque = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo4_Esque.setEnabled(True)
        self.lbEletrodo4_Esque.setGeometry(QtCore.QRect(120, 20, 18, 18))
        self.lbEletrodo4_Esque.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo4_Esque.setMidLineWidth(1)
        self.lbEletrodo4_Esque.setObjectName("lbEletrodo4_Esque")
        self.lbEletrodo5_Esque = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo5_Esque.setEnabled(True)
        self.lbEletrodo5_Esque.setGeometry(QtCore.QRect(140, 20, 18, 18))
        self.lbEletrodo5_Esque.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo5_Esque.setMidLineWidth(1)
        self.lbEletrodo5_Esque.setObjectName("lbEletrodo5_Esque")
        self.lbEletrodo6_Esque = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo6_Esque.setEnabled(True)
        self.lbEletrodo6_Esque.setGeometry(QtCore.QRect(160, 20, 18, 18))
        self.lbEletrodo6_Esque.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo6_Esque.setMidLineWidth(1)
        self.lbEletrodo6_Esque.setObjectName("lbEletrodo6_Esque")
        self.lbEletrodo7_Esque = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo7_Esque.setEnabled(True)
        self.lbEletrodo7_Esque.setGeometry(QtCore.QRect(180, 20, 18, 18))
        self.lbEletrodo7_Esque.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo7_Esque.setMidLineWidth(1)
        self.lbEletrodo7_Esque.setObjectName("lbEletrodo7_Esque")
        self.lbEletrodo8_Esque = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo8_Esque.setEnabled(True)
        self.lbEletrodo8_Esque.setGeometry(QtCore.QRect(200, 20, 18, 18))
        self.lbEletrodo8_Esque.setStyleSheet("background-color: rgb(0, 255, 0);;")
        self.lbEletrodo8_Esque.setMidLineWidth(1)
        self.lbEletrodo8_Esque.setObjectName("lbEletrodo8_Esque")
        self.lbEletrodo1_Dir = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo1_Dir.setEnabled(True)
        self.lbEletrodo1_Dir.setGeometry(QtCore.QRect(740, 20, 18, 18))
        self.lbEletrodo1_Dir.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo1_Dir.setMidLineWidth(1)
        self.lbEletrodo1_Dir.setObjectName("lbEletrodo1_Dir")
        self.lbEletrodo4_Dir = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo4_Dir.setEnabled(True)
        self.lbEletrodo4_Dir.setGeometry(QtCore.QRect(800, 20, 18, 18))
        self.lbEletrodo4_Dir.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo4_Dir.setMidLineWidth(1)
        self.lbEletrodo4_Dir.setObjectName("lbEletrodo4_Dir")
        self.lbEletrodo8_Dir = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo8_Dir.setEnabled(True)
        self.lbEletrodo8_Dir.setGeometry(QtCore.QRect(880, 20, 18, 18))
        self.lbEletrodo8_Dir.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo8_Dir.setMidLineWidth(1)
        self.lbEletrodo8_Dir.setObjectName("lbEletrodo8_Dir")
        self.lbEletrodo3_Dir = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo3_Dir.setEnabled(True)
        self.lbEletrodo3_Dir.setGeometry(QtCore.QRect(780, 20, 18, 18))
        self.lbEletrodo3_Dir.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo3_Dir.setMidLineWidth(1)
        self.lbEletrodo3_Dir.setObjectName("lbEletrodo3_Dir")
        self.lbEletrodo5_Dir = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo5_Dir.setEnabled(True)
        self.lbEletrodo5_Dir.setGeometry(QtCore.QRect(820, 20, 18, 18))
        self.lbEletrodo5_Dir.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo5_Dir.setMidLineWidth(1)
        self.lbEletrodo5_Dir.setObjectName("lbEletrodo5_Dir")
        self.lbEletrodo2_Dir = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo2_Dir.setEnabled(True)
        self.lbEletrodo2_Dir.setGeometry(QtCore.QRect(760, 20, 18, 18))
        self.lbEletrodo2_Dir.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo2_Dir.setMidLineWidth(1)
        self.lbEletrodo2_Dir.setObjectName("lbEletrodo2_Dir")
        self.lbEletrodo7_Dir = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo7_Dir.setEnabled(True)
        self.lbEletrodo7_Dir.setGeometry(QtCore.QRect(860, 20, 18, 18))
        self.lbEletrodo7_Dir.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo7_Dir.setMidLineWidth(1)
        self.lbEletrodo7_Dir.setObjectName("lbEletrodo7_Dir")
        self.lbEletrodo6_Dir = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo6_Dir.setEnabled(True)
        self.lbEletrodo6_Dir.setGeometry(QtCore.QRect(840, 20, 18, 18))
        self.lbEletrodo6_Dir.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo6_Dir.setMidLineWidth(1)
        self.lbEletrodo6_Dir.setObjectName("lbEletrodo6_Dir")
        self.lbEletrodo11_Esque = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo11_Esque.setEnabled(True)
        self.lbEletrodo11_Esque.setGeometry(QtCore.QRect(260, 20, 18, 18))
        self.lbEletrodo11_Esque.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo11_Esque.setMidLineWidth(1)
        self.lbEletrodo11_Esque.setObjectName("lbEletrodo11_Esque")
        self.lbEletrodo9_Esque = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo9_Esque.setEnabled(True)
        self.lbEletrodo9_Esque.setGeometry(QtCore.QRect(220, 20, 18, 18))
        self.lbEletrodo9_Esque.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo9_Esque.setMidLineWidth(1)
        self.lbEletrodo9_Esque.setObjectName("lbEletrodo9_Esque")
        self.lbEletrodo12_Esque = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo12_Esque.setEnabled(True)
        self.lbEletrodo12_Esque.setGeometry(QtCore.QRect(280, 20, 18, 18))
        self.lbEletrodo12_Esque.setStyleSheet("background-color: rgb(0, 255, 0);;")
        self.lbEletrodo12_Esque.setMidLineWidth(1)
        self.lbEletrodo12_Esque.setObjectName("lbEletrodo12_Esque")
        self.lbEletrodo10_Esque = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo10_Esque.setEnabled(True)
        self.lbEletrodo10_Esque.setGeometry(QtCore.QRect(240, 20, 18, 18))
        self.lbEletrodo10_Esque.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo10_Esque.setMidLineWidth(1)
        self.lbEletrodo10_Esque.setObjectName("lbEletrodo10_Esque")
        self.lbEletrodo12_Dir = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo12_Dir.setEnabled(True)
        self.lbEletrodo12_Dir.setGeometry(QtCore.QRect(960, 20, 18, 18))
        self.lbEletrodo12_Dir.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo12_Dir.setMidLineWidth(1)
        self.lbEletrodo12_Dir.setObjectName("lbEletrodo12_Dir")
        self.lbEletrodo11_Dir = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo11_Dir.setEnabled(True)
        self.lbEletrodo11_Dir.setGeometry(QtCore.QRect(940, 20, 18, 18))
        self.lbEletrodo11_Dir.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo11_Dir.setMidLineWidth(1)
        self.lbEletrodo11_Dir.setObjectName("lbEletrodo11_Dir")
        self.lbEletrodo10_Dir = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo10_Dir.setEnabled(True)
        self.lbEletrodo10_Dir.setGeometry(QtCore.QRect(920, 20, 18, 18))
        self.lbEletrodo10_Dir.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo10_Dir.setMidLineWidth(1)
        self.lbEletrodo10_Dir.setObjectName("lbEletrodo10_Dir")
        self.lbEletrodo9_Dir = QtWidgets.QLabel(TelaCriaReceita)
        self.lbEletrodo9_Dir.setEnabled(True)
        self.lbEletrodo9_Dir.setGeometry(QtCore.QRect(900, 20, 18, 18))
        self.lbEletrodo9_Dir.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lbEletrodo9_Dir.setMidLineWidth(1)
        self.lbEletrodo9_Dir.setObjectName("lbEletrodo9_Dir")

        self.retranslateUi(TelaCriaReceita)
        QtCore.QMetaObject.connectSlotsByName(TelaCriaReceita)

    def retranslateUi(self, TelaCriaReceita):
        _translate = QtCore.QCoreApplication.translate
        TelaCriaReceita.setWindowTitle(_translate("TelaCriaReceita", "TelaCriaReceita"))
        self.btVoltar.setText(_translate("TelaCriaReceita", "VOLTAR"))
        self.lbImgEsquerdo.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\">Clique para configurar o lado esquerdo</p></body></html>"))
        self.lbImgDireito.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\">Clique para configurar o lado direito</p></body></html>"))
        self.label.setText(_translate("TelaCriaReceita", "Nome do Programa"))
        self.btAtualizar.setText(_translate("TelaCriaReceita", "ATUALIZAR"))
        self.btApagar.setText(_translate("TelaCriaReceita", "APAGAR"))
        self.btSlavar.setText(_translate("TelaCriaReceita", "SALVAR"))
        self.btLocalizar.setText(_translate("TelaCriaReceita", "LOCALIZAR"))
        self.lbEletrodo1_Esque.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">1</span></p></body></html>"))
        self.lbEletrodo2_Esque.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">2</span></p></body></html>"))
        self.lbEletrodo3_Esque.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">3</span></p></body></html>"))
        self.lbEletrodo4_Esque.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">4</span></p></body></html>"))
        self.lbEletrodo5_Esque.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">5</span></p></body></html>"))
        self.lbEletrodo6_Esque.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">6</span></p></body></html>"))
        self.lbEletrodo7_Esque.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">7</span></p></body></html>"))
        self.lbEletrodo8_Esque.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">8</span></p></body></html>"))
        self.lbEletrodo1_Dir.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">1</span></p></body></html>"))
        self.lbEletrodo4_Dir.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">4</span></p></body></html>"))
        self.lbEletrodo8_Dir.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">8</span></p></body></html>"))
        self.lbEletrodo3_Dir.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">3</span></p></body></html>"))
        self.lbEletrodo5_Dir.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">5</span></p></body></html>"))
        self.lbEletrodo2_Dir.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">2</span></p></body></html>"))
        self.lbEletrodo7_Dir.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">7</span></p></body></html>"))
        self.lbEletrodo6_Dir.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">6</span></p></body></html>"))
        self.lbEletrodo11_Esque.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">11</span></p></body></html>"))
        self.lbEletrodo9_Esque.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">9</span></p></body></html>"))
        self.lbEletrodo12_Esque.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">12</span></p></body></html>"))
        self.lbEletrodo10_Esque.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">10</span></p></body></html>"))
        self.lbEletrodo12_Dir.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">12</span></p></body></html>"))
        self.lbEletrodo11_Dir.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">11</span></p></body></html>"))
        self.lbEletrodo10_Dir.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">10</span></p></body></html>"))
        self.lbEletrodo9_Dir.setText(_translate("TelaCriaReceita", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">9</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaCriaReceita = QtWidgets.QWidget()
    ui = Ui_TelaCriaReceita()
    ui.setupUi(TelaCriaReceita)
    TelaCriaReceita.show()
    sys.exit(app.exec_())
