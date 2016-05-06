import sys
from PyQt4 import QtGui, QtCore
from recorder import Record


class GUI(QtGui.QMainWindow): #Coloca QMainWIndow ou QWidget afeta o restante da programação.
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI(self)
        
        
    def initUI(self, QMainWindow):        
#        self.setGeometry(250, 100, 800, 450) # Primeiros dois argumentos: posição da janela; depois os outros dois são o tamanho
        
        self.resize(800,450)       
        self.center()   #Coloca no centro a partir da resolução da tela encontrada.    
        self.setWindowTitle('Music Box')
        
#       self.setWindowIcon(QtGui.QIcon('arquivo.png'))        Essa linha serve para quando tivermos um ícone pronto para o app.     
     
#        self.paint_gravar()
    def gravar(self):
        gravar = QtGui.QPushButton('Gravar', self)
        gravar.setToolTip('Aperte <b>Gravar</b> para começar a gravação') # Ao passar o mouse por cima do botão, aparece um texto de explicação.
#       gravar.resize
        gravar.adjustSize() 
        gravar.move(150, 200)   
        self.show()
        gravar.clicked.connect(self.recorder.record)          
        
    def salvar(self):
        salvar= QtGui.QAction(QtGui.QIcon('arquivo.png'), '&Salvar', self)
        salvar.setStatusTip('Salvar o arquivo')
        salvar.setShortcut('Ctrl+S')
#        salvar.triggered.connect(Ação)
#        salvar.clicked.connect(self.confirm_action) 
    
    def imprimir(self):
        imprimir= QtGui.QAction(QtGui.QIcon('arquivo.png'), '&Imprimir', self)
        imprimir.setStatusTip('Imprimir o arquivo')
        imprimir.setShortcut('Ctrl+P')
#        imprimir.triggered.connect(Ação)
    def compartilhar(self):
        compartilhar= QtGui.QAction(QtGui.QIcon('arquivo.png'), '&Compartilhar', self)
        compartilhar.setStatusTip('Compartilhar o arquivo')
        compartilhar.setShortcut('Ctrl+F')
#        compartilhar.triggered.connect(Ação)        
    def enviar(self):
        enviar= QtGui.QAction(QtGui.QIcon('arquivo.png'), '&Enviar', self)
        enviar.setStatusTip('Enviar o arquivo')
        enviar.setShortcut('Ctrl+E')
#        enviar.triggered.connect(Ação)        
    def menu(self):
        menubar = self.menuBar() # Aqui criei um menu com as opções de o que fazer com o arquvo gravado.
        fileMenu = menubar.addMenu('&Opções')
        fileMenu.addAction(salvar) #Adiciona a opção salvar dentro do menu "Opções"
        fileMenu.addAction(imprimir)
        fileMenu.addAction(compartilhar)
        fileMenu.addAction(enviar)
        self.statusBar() #Possibilita que o StatusTip apareça na tela.
#        
#        self.centralwidget = QtGui.QWidget(QMainWindow)
#        self.centralwidget.setObjectName("centralwidget")
#        self.Partitura = QtGui.QGraphicsView(self.centralwidget)
#        self.Partitura.setGeometry(400,10, 50, 50)
#        self.Partitura.setObjectName("Partitura") 
        
        self.label = QtGui.QLabel(self)
        self.label.setText('Partitura')
        self.label.setFont(QtGui.QFont('SansSerif', 18))
        self.label.adjustSize() 
        self.label.move(545, 75)
        self.label.show()
        
        self.label = QtGui.QLabel(self)
        self.label.setText('Recentes')
        self.label.setFont(QtGui.QFont('SansSerif', 18))
        self.label.adjustSize() 
        self.label.move(135, 250)
        self.label.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center() #Isso dá informações sobre o Desktop do usuário, como a resolução da tela.
        qr.moveCenter(cp)
        self.move(qr.topLeft())
            
#    def change_status(self):
#        if():        
#            self.statusBar().showMessage('Carregando')
#        elif():
#            self.statusBar().showMessage('Carregando')
    
    def send_email(self):
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)
        
    def confirm_action(self): # Quando uma opção for selecionada, essa função vai ser ativada.
        sender = self.sender() # Informa qual botão foi clicado.
        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox) 
    
    def gravar_clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' foi pressionado') #Exemplo até agora
        
    def loading(self): # Enquanto estiver carregando vai mostrar uma barra de progresso na tela.
        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        
        self.timer = QtCore.QBasicTimer()
        self.step = 0
        
        self.timer.start(100, self)
        
        if self.step >= 100: # Exemplo, aqui vai ser a condição de ter acabado de carregar ou não.
            self.timer.stop()
            self.btn.setText('Finished')
            return
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        
    def open_images(self): # Pensei que poderíamos precisar utilizar essa função para mostrar a partitura.
        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap("arquivo.png")

        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)
#==================================================================================#       
#    def select_language(self): DEPOIS PODEMOS MUDAR A LINGUAGEM DO PROGRAMA CONFORME A OPÇÃO SELECIONADA.
#
#        combo = QtGui.QComboBox(self)
#        combo.addItem("Portuguese")
#        combo.addItem("English")
#        
#        combo.move(50, 50)
#        self.lbl.move(50, 150)
#        
#        combo.activated[str].connect(self.onActivated)
#        
#    def onActivated(self, text):
#  
#        self.lbl.setText(text)
#        self.lbl.adjustSize()  
#================================================================================#       
#   def drawNotes(self): # Mostra na tela as notas que foram tocadas. 
# DEPOIS COMPLETAMOS A CONDIÇÃO DO IF CONFORME O RESULTADO DA LEITURA DO CROMAGRAMA
#        if ():
#            self.text = ''
#    
#   def paintEvent(self, event): #Desenha na tela usando a função drawText
#        qp = QtGui.QPainter()
#        qp.begin(self)
#        self.drawText(event, qp)
#        qp.end()
#        
#    def drawText(self, event, qp): #
#        qp.setPen(QtGui.QColor(168, 34, 3))
#        qp.setFont(QtGui.QFont('Decorative', 10))
#        qp.drawText(event.rect(), QtCore.Qt.AlignRight, self.text) 
#=================================================================================#
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()
        
    def drawBrushes(self, qp):
        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        brush.setStyle(QtCore.Qt.VerPattern) #Do Gravar
        qp.setBrush(brush)
        qp.drawRect(25, 25, 325, 175)        
        
        brush.setStyle(QtCore.Qt.BDiagPattern) #Da Partitura
        qp.setBrush(brush)
        qp.drawRect(400, 100, 375, 225)
        
        brush.setStyle(QtCore.Qt.Dense1Pattern) #Das Gravaões Recentes
        qp.setBrush(brush)
        qp.drawRect(25, 275, 325, 150)
        
def main():
    app = QtGui.QApplication(sys.argv) # Esse " sys.argv" corresponde aos argumentos que podemos usar
    ex = GUI()
    GUI.show()
    sys.exit(app.exec_()) #Para de rodar a aplicação quando a janela é fechada.


if __name__ == '__main__':
    main() 
