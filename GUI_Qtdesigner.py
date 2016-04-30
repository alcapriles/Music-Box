import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 190, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.Partitura = QtGui.QGraphicsView(self.centralwidget)
        self.Partitura.setGeometry(QtCore.QRect(290, 60, 331, 221))
        self.Partitura.setObjectName(_fromUtf8("Partitura"))
        self.Imagem_gravacao = QtGui.QGraphicsView(self.centralwidget)
        self.Imagem_gravacao.setGeometry(QtCore.QRect(10, 0, 256, 192))
        self.Imagem_gravacao.setObjectName(_fromUtf8("Imagem_gravacao"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(400, 30, 91, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 230, 171, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 260, 256, 192))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOp = QtGui.QMenu(self.menubar)
        self.menuOp.setObjectName(_fromUtf8("menuOp"))
        self.menuCompartilhar = QtGui.QMenu(self.menuOp)
        self.menuCompartilhar.setObjectName(_fromUtf8("menuCompartilhar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalvar = QtGui.QAction(MainWindow)
        self.actionSalvar.setObjectName(_fromUtf8("actionSalvar"))
        self.actionImprimir = QtGui.QAction(MainWindow)
        self.actionImprimir.setObjectName(_fromUtf8("actionImprimir"))
        self.actionEnviar = QtGui.QAction(MainWindow)
        self.actionEnviar.setObjectName(_fromUtf8("actionEnviar"))
        self.actionFacebook = QtGui.QAction(MainWindow)
        self.actionFacebook.setObjectName(_fromUtf8("actionFacebook"))
        self.actionTwitter = QtGui.QAction(MainWindow)
        self.actionTwitter.setObjectName(_fromUtf8("actionTwitter"))
        self.menuCompartilhar.addAction(self.actionFacebook)
        self.menuCompartilhar.addAction(self.actionTwitter)
        self.menuOp.addAction(self.actionSalvar)
        self.menuOp.addAction(self.actionImprimir)
        self.menuOp.addAction(self.menuCompartilhar.menuAction())
        self.menuOp.addAction(self.actionEnviar)
        self.menubar.addAction(self.menuOp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Box", None))
        self.pushButton.setText(_translate("MainWindow", "Gravar", None))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Partitura</span></p></body></html>", None))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Últimas Gravações</span></p></body></html>", None))
        self.menuOp.setTitle(_translate("MainWindow", "Opções", None))
        self.menuCompartilhar.setTitle(_translate("MainWindow", "Compartilhar", None))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar", None))
        self.actionImprimir.setText(_translate("MainWindow", "Imprimir", None))
        self.actionEnviar.setText(_translate("MainWindow", "Enviar", None))
        self.actionFacebook.setText(_translate("MainWindow", "Facebook", None))
        self.actionTwitter.setText(_translate("MainWindow", "Twitter", None))

def main():
    
    app = QtGui.QApplication(sys.argv) # Esse " sys.argv" corresponde aos argumentos que podemos usar
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 