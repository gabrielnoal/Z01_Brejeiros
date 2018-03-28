# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_Rom = QtWidgets.QVBoxLayout()
        self.verticalLayout_Rom.setObjectName("verticalLayout_Rom")
        self.romView = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.romView.sizePolicy().hasHeightForWidth())
        self.romView.setSizePolicy(sizePolicy)
        self.romView.setObjectName("romView")
        self.verticalLayout_Rom.addWidget(self.romView)
        self.horizontalLayout.addLayout(self.verticalLayout_Rom)
        self.verticalLayout_Ram = QtWidgets.QVBoxLayout()
        self.verticalLayout_Ram.setObjectName("verticalLayout_Ram")
        self.ramView = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ramView.sizePolicy().hasHeightForWidth())
        self.ramView.setSizePolicy(sizePolicy)
        self.ramView.setObjectName("ramView")
        self.verticalLayout_Ram.addWidget(self.ramView)
        self.horizontalLayout.addLayout(self.verticalLayout_Ram)
        self.verticalLayout_Reg = QtWidgets.QVBoxLayout()
        self.verticalLayout_Reg.setObjectName("verticalLayout_Reg")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_Reg = QtWidgets.QLabel(self.centralwidget)
        self.label_Reg.setObjectName("label_Reg")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_Reg)
        self.label_A = QtWidgets.QLabel(self.centralwidget)
        self.label_A.setObjectName("label_A")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_A)
        self.lineEdit_A = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_A.setEnabled(False)
        self.lineEdit_A.setObjectName("lineEdit_A")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_A)
        self.label_D = QtWidgets.QLabel(self.centralwidget)
        self.label_D.setObjectName("label_D")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_D)
        self.lineEdit_D = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_D.setEnabled(False)
        self.lineEdit_D.setObjectName("lineEdit_D")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_D)
        self.label_S = QtWidgets.QLabel(self.centralwidget)
        self.label_S.setObjectName("label_S")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_S)
        self.lineEdit_S = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_S.setEnabled(False)
        self.lineEdit_S.setObjectName("lineEdit_S")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_S)
        self.label_inM = QtWidgets.QLabel(self.centralwidget)
        self.label_inM.setObjectName("label_inM")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_inM)
        self.lineEdit_inM = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_inM.setEnabled(False)
        self.lineEdit_inM.setObjectName("lineEdit_inM")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_inM)
        self.label_outM = QtWidgets.QLabel(self.centralwidget)
        self.label_outM.setObjectName("label_outM")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_outM)
        self.lineEdit_outM = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_outM.setEnabled(False)
        self.lineEdit_outM.setObjectName("lineEdit_outM")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_outM)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.verticalLayout_Reg.addLayout(self.formLayout)
        self.label_ALU = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ALU.sizePolicy().hasHeightForWidth())
        self.label_ALU.setSizePolicy(sizePolicy)
        self.label_ALU.setAutoFillBackground(False)
        self.label_ALU.setText("")
        self.label_ALU.setPixmap(QtGui.QPixmap("theme/icon-alu.png"))
        self.label_ALU.setScaledContents(False)
        self.label_ALU.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ALU.setObjectName("label_ALU")
        self.verticalLayout_Reg.addWidget(self.label_ALU)
        self.horizontalLayout.addLayout(self.verticalLayout_Reg)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        self.menuVisualizar = QtWidgets.QMenu(self.menubar)
        self.menuVisualizar.setObjectName("menuVisualizar")
        self.menuRAM = QtWidgets.QMenu(self.menuVisualizar)
        self.menuRAM.setObjectName("menuRAM")
        self.menuROM = QtWidgets.QMenu(self.menuVisualizar)
        self.menuROM.setObjectName("menuROM")
        self.menuRegistradores = QtWidgets.QMenu(self.menuVisualizar)
        self.menuRegistradores.setObjectName("menuRegistradores")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setToolTipsVisible(True)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuAcao = QtWidgets.QMenu(self.menubar)
        self.menuAcao.setObjectName("menuAcao")
        self.menuOpcoes = QtWidgets.QMenu(self.menubar)
        self.menuOpcoes.setObjectName("menuOpcoes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.actionRAMBinario = QtWidgets.QAction(MainWindow)
        self.actionRAMBinario.setCheckable(True)
        self.actionRAMBinario.setObjectName("actionRAMBinario")
        self.actionAssembly = QtWidgets.QAction(MainWindow)
        self.actionAssembly.setObjectName("actionAssembly")
        self.actionRAMHexadecimal = QtWidgets.QAction(MainWindow)
        self.actionRAMHexadecimal.setCheckable(True)
        self.actionRAMHexadecimal.setObjectName("actionRAMHexadecimal")
        self.actionROMBinario = QtWidgets.QAction(MainWindow)
        self.actionROMBinario.setCheckable(True)
        self.actionROMBinario.setObjectName("actionROMBinario")
        self.actionROMHexadecimal = QtWidgets.QAction(MainWindow)
        self.actionROMHexadecimal.setCheckable(True)
        self.actionROMHexadecimal.setObjectName("actionROMHexadecimal")
        self.actionROMAssembly = QtWidgets.QAction(MainWindow)
        self.actionROMAssembly.setCheckable(True)
        self.actionROMAssembly.setObjectName("actionROMAssembly")
        self.actionREGBinario = QtWidgets.QAction(MainWindow)
        self.actionREGBinario.setCheckable(True)
        self.actionREGBinario.setObjectName("actionREGBinario")
        self.actionREGHexadecimal = QtWidgets.QAction(MainWindow)
        self.actionREGHexadecimal.setCheckable(True)
        self.actionREGHexadecimal.setObjectName("actionREGHexadecimal")
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("theme/document-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbrir.setIcon(icon)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionNovo = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("theme/document-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNovo.setIcon(icon1)
        self.actionNovo.setObjectName("actionNovo")
        self.actionProximo = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("theme/go-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProximo.setIcon(icon2)
        self.actionProximo.setObjectName("actionProximo")
        self.actionExecutarFim = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("theme/go-jump.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("theme/go-jump.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionExecutarFim.setIcon(icon3)
        self.actionExecutarFim.setObjectName("actionExecutarFim")
        self.actionParar = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("theme/process-stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionParar.setIcon(icon4)
        self.actionParar.setObjectName("actionParar")
        self.actionVoltarInicio = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("theme/go-first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVoltarInicio.setIcon(icon5)
        self.actionVoltarInicio.setObjectName("actionVoltarInicio")
        self.actionSalvar_ROM = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("theme/document-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionSalvar_ROM.setIcon(icon6)
        self.actionSalvar_ROM.setObjectName("actionSalvar_ROM")
        self.actionConfiguracoes = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("theme/preferences-system.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfiguracoes.setIcon(icon7)
        self.actionConfiguracoes.setObjectName("actionConfiguracoes")
        self.actionEraseRAM = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("theme/eraser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEraseRAM.setIcon(icon8)
        self.actionEraseRAM.setObjectName("actionEraseRAM")
        self.menuAjuda.addAction(self.actionSobre)
        self.menuRAM.addAction(self.actionRAMBinario)
        self.menuRAM.addAction(self.actionRAMHexadecimal)
        self.menuROM.addSeparator()
        self.menuROM.addSeparator()
        self.menuROM.addAction(self.actionROMBinario)
        self.menuROM.addAction(self.actionROMHexadecimal)
        self.menuROM.addAction(self.actionROMAssembly)
        self.menuRegistradores.addSeparator()
        self.menuRegistradores.addSeparator()
        self.menuRegistradores.addAction(self.actionREGBinario)
        self.menuRegistradores.addAction(self.actionREGHexadecimal)
        self.menuVisualizar.addAction(self.menuROM.menuAction())
        self.menuVisualizar.addAction(self.menuRAM.menuAction())
        self.menuVisualizar.addAction(self.menuRegistradores.menuAction())
        self.menuArquivo.addAction(self.actionNovo)
        self.menuArquivo.addAction(self.actionAbrir)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionSalvar_ROM)
        self.menuArquivo.addAction(self.actionSair)
        self.menuAcao.addAction(self.actionProximo)
        self.menuAcao.addAction(self.actionExecutarFim)
        self.menuAcao.addAction(self.actionParar)
        self.menuAcao.addAction(self.actionVoltarInicio)
        self.menuOpcoes.addAction(self.actionConfiguracoes)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuAcao.menuAction())
        self.menubar.addAction(self.menuVisualizar.menuAction())
        self.menubar.addAction(self.menuOpcoes.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.toolBar.addAction(self.actionNovo)
        self.toolBar.addAction(self.actionAbrir)
        self.toolBar.addAction(self.actionSalvar_ROM)
        self.toolBar.addAction(self.actionEraseRAM)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionProximo)
        self.toolBar.addAction(self.actionExecutarFim)
        self.toolBar.addAction(self.actionParar)
        self.toolBar.addAction(self.actionVoltarInicio)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConfiguracoes)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RESimulatorGUI"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Instruções</p></body></html>"))
        self.label_Reg.setText(_translate("MainWindow", "Registradores"))
        self.label_A.setText(_translate("MainWindow", "A"))
        self.label_D.setText(_translate("MainWindow", "D"))
        self.label_S.setText(_translate("MainWindow", "S"))
        self.label_inM.setText(_translate("MainWindow", "inM"))
        self.label_outM.setText(_translate("MainWindow", "outM"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.menuVisualizar.setTitle(_translate("MainWindow", "Visualizar"))
        self.menuRAM.setTitle(_translate("MainWindow", "RAM"))
        self.menuROM.setTitle(_translate("MainWindow", "ROM"))
        self.menuRegistradores.setTitle(_translate("MainWindow", "Registradores"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuAcao.setTitle(_translate("MainWindow", "Ação"))
        self.menuOpcoes.setTitle(_translate("MainWindow", "Opções"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))
        self.actionRAMBinario.setText(_translate("MainWindow", "Binario"))
        self.actionAssembly.setText(_translate("MainWindow", "Assembly"))
        self.actionRAMHexadecimal.setText(_translate("MainWindow", "Hexadecimal"))
        self.actionROMBinario.setText(_translate("MainWindow", "Binário"))
        self.actionROMHexadecimal.setText(_translate("MainWindow", "Hexadecimal"))
        self.actionROMAssembly.setText(_translate("MainWindow", "Assembly"))
        self.actionREGBinario.setText(_translate("MainWindow", "Binário"))
        self.actionREGHexadecimal.setText(_translate("MainWindow", "Hexadecimal"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionNovo.setText(_translate("MainWindow", "Novo"))
        self.actionNovo.setToolTip(_translate("MainWindow", "Novo Arquivo"))
        self.actionProximo.setText(_translate("MainWindow", "Proximo"))
        self.actionProximo.setToolTip(_translate("MainWindow", "Próxima Instrução"))
        self.actionExecutarFim.setText(_translate("MainWindow", "Executar até o Fim"))
        self.actionExecutarFim.setToolTip(_translate("MainWindow", "Executar até o final"))
        self.actionParar.setText(_translate("MainWindow", "Parar"))
        self.actionParar.setToolTip(_translate("MainWindow", "Parar execução"))
        self.actionVoltarInicio.setText(_translate("MainWindow", "Voltar ao Início"))
        self.actionVoltarInicio.setToolTip(_translate("MainWindow", "Voltar ao Início"))
        self.actionSalvar_ROM.setText(_translate("MainWindow", "Salvar ROM"))
        self.actionSalvar_ROM.setToolTip(_translate("MainWindow", "Salvar ROM"))
        self.actionConfiguracoes.setText(_translate("MainWindow", "Configurações"))
        self.actionConfiguracoes.setToolTip(_translate("MainWindow", "Configurações"))
        self.actionEraseRAM.setText(_translate("MainWindow", "EraseRAM"))
        self.actionEraseRAM.setToolTip(_translate("MainWindow", "Erase RAM"))

