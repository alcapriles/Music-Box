import sys
from PyQt4 import QtGui


class Example(QtGui.QMainWindow): #Coloca QMainWIndow ou QWidget afeta o restante da programação.
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):        
#        self.setGeometry(250, 100, 800, 450) # Primeiros dois argumentos: posição da janela; depois os outros dois são o tamanho
        
        self.resize(800,450)       
        self.center()   #Coloca no centro a partir da resolução da tela encontrada.    
        self.setWindowTitle('Music Box')
        
#       self.setWindowIcon(QtGui.QIcon('arquivo.png'))        Essa linha serve para quando tivermos um ícone pronto para o app.
        
        btn = QtGui.QPushButton('Gravar', self)
        btn.setToolTip('Aperte <b>Gravar</b> para começar a gravação') # Ao passar o mouse por cima do botão, aparece um texto de explicação.
        btn.resize(75,50)
        btn.move(25, 50)   
        self.show()
              
        salvar= QtGui.QAction(QtGui.QIcon('arquivo.png'), '&Salvar', self)
        salvar.setStatusTip('Salvar o arquivo')
        salvar.setShortcut('Ctrl+S')
#        salvar.triggered.connect(Ação)
        
        imprimir= QtGui.QAction(QtGui.QIcon('arquivo.png'), '&Imprimir', self)
        imprimir.setStatusTip('Imprimir o arquivo')
        imprimir.setShortcut('Ctrl+P')
#        imprimir.triggered.connect(Ação)
    
        compartilhar= QtGui.QAction(QtGui.QIcon('arquivo.png'), '&Compartilhar', self)
        compartilhar.setStatusTip('Compartilhar o arquivo')
        compartilhar.setShortcut('Ctrl+F')
#        compartilhar.triggered.connect(Ação)        
        
        enviar= QtGui.QAction(QtGui.QIcon('arquivo.png'), '&Enviar', self)
        enviar.setStatusTip('Enviar o arquivo')
        enviar.setShortcut('Ctrl+E')
#        enviar.triggered.connect(Ação)        

        menubar = self.menuBar() # Aqui criei um menu com as opções de o que fazer com o arquvo gravado.
        fileMenu = menubar.addMenu('&Opções')
        fileMenu.addAction(salvar) #Adiciona a opção salvar dentro do menu "Opções"
        fileMenu.addAction(imprimir)
        fileMenu.addAction(compartilhar)
        fileMenu.addAction(enviar)
        self.statusBar() #Possibilita que o StatusTip apareça na tela.

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
    
        
def main():
    
    app = QtGui.QApplication(sys.argv) # Esse " sys.argv" corresponde aos argumentos que podemos usar
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 