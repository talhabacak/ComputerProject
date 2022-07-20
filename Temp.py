#
#	Created by : Talha Bacak
#

import torch
import cv2
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QFileDialog, QTableWidgetItem,QHBoxLayout, QVBoxLayout, QScrollArea
from PyQt5.QtGui import QPixmap , QPainter, QPen
from PyQt5.QtCore import Qt

import sys


from lxml.etree import Element, SubElement
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree
import xml.etree.ElementTree as ET

class Ui_Form(object):
    def setupUi(self, Form):
        self.row = 0
        self.count=-1
        self.startIndex = 0 #karenin başlangıç noktası
        self.status = False #eğer tıklanma yapılırsa true olacak, bırakılınca false olcak
        self.finishIndex = 0
        self.text = []
        self.out_str = " "
        self.control = 0
        self.openMode = 0
        self.imagePath = ""
        self.labels = []
        self.labelL = []        
        self.labelText = []
        self.pushButton_Ex = []
        self.fark = 0,0
        self.beforeSize = 640,860
        self.labelNames = []
        self.cfgControl = 0
        self.weightsControl = 0
        self.namesControl = 0
        self.ptControl = 0
        self.nameSelect = 0

        self.vBox_main = QtWidgets.QVBoxLayout(Form)
        self.vBox_main.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.vBox_main.setContentsMargins(10, 5, 10, 5)
        self.vBox_main.setSpacing(10) 
        
        self.hBox_menu = QtWidgets.QHBoxLayout()
        self.hBox_menu.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.hBox_menu.setContentsMargins(5, 5, 5, 5)
        self.hBox_menu.setSpacing(5)

        self.vBox_Browse = QtWidgets.QVBoxLayout()
        self.vBox_Browse.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.vBox_Browse.setContentsMargins(5, 5, 5, 5)
        self.vBox_Browse.setSpacing(5) 

        self.hBox_Size = QtWidgets.QHBoxLayout()
        self.hBox_Size.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.hBox_Size.setContentsMargins(0, 0, 0, 0)
        self.hBox_Size.setSpacing(5)
        
        self.vBox_Manuel = QtWidgets.QVBoxLayout()
        self.vBox_Manuel.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.vBox_Manuel.setContentsMargins(5, 5, 5, 5)
        self.vBox_Manuel.setSpacing(5) 
        
        self.vBox_AutonomousCOCO = QtWidgets.QVBoxLayout()
        self.vBox_AutonomousCOCO.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.vBox_AutonomousCOCO.setContentsMargins(5, 5, 5, 5)
        self.vBox_AutonomousCOCO.setSpacing(5) 
        
        self.vBox_AutonomousCustom = QtWidgets.QVBoxLayout()
        self.vBox_AutonomousCustom.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.vBox_AutonomousCustom.setContentsMargins(5, 5, 5, 5)
        self.vBox_AutonomousCustom.setSpacing(5) 
        
        self.vBox_Load = QtWidgets.QVBoxLayout()
        self.vBox_Load.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.vBox_Load.setContentsMargins(5, 5, 5, 5)
        self.vBox_Load.setSpacing(5) 

        self.hBox_LoadYOLO = QtWidgets.QHBoxLayout()
        self.hBox_LoadYOLO.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.hBox_LoadYOLO.setContentsMargins(0, 0, 0, 0)
        self.hBox_LoadYOLO.setSpacing(5)
        
        self.vBox_Save = QtWidgets.QVBoxLayout()
        self.vBox_Save.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.vBox_Save.setContentsMargins(5, 5, 5, 5)
        self.vBox_Save.setSpacing(10) 
        
        self.hBox = QtWidgets.QHBoxLayout()
        self.hBox.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.hBox.setContentsMargins(0, 5, 0, 5)
        self.hBox.setSpacing(10)
                
        self.vBox = QtWidgets.QVBoxLayout()
        self.vBox.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.vBox.setContentsMargins(5, 5, 5, 5)
        self.vBox.setSpacing(5) 

        self.vBox_LM = QtWidgets.QVBoxLayout()
        self.vBox_LM.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.vBox_LM.setContentsMargins(0, 0, 0, 0)
        self.vBox_LM.setSpacing(5)     
        
        self.hBox_mode = QtWidgets.QHBoxLayout()
        self.hBox_mode.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.hBox_mode.setContentsMargins(5, 5, 5, 5)
        self.hBox_mode.setSpacing(5)  
        
        self.vBox_label = QtWidgets.QVBoxLayout()
        self.vBox_label.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.vBox_label.setContentsMargins(5, 5, 5, 5)
        self.vBox_label.setSpacing(5)     
        
        self.hBox_labelAdd = QtWidgets.QHBoxLayout()
        self.hBox_labelAdd.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.hBox_labelAdd.setContentsMargins(0, 0, 0, 0)
        self.hBox_labelAdd.setSpacing(5) 
        
        self.hBox_labelDel = QtWidgets.QHBoxLayout()
        self.hBox_labelDel.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.hBox_labelDel.setContentsMargins(0, 0, 0, 0)
        self.hBox_labelDel.setSpacing(5) 

        self.hBox_table = QtWidgets.QHBoxLayout()
        self.hBox_table.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.hBox_table.setContentsMargins(0, 5, 0, 0)
        self.hBox_table.setSpacing(5)  
        
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1024, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(30, 30))
        Form.setSizeIncrement(QtCore.QSize(1, 1))
        Form.setBaseSize(QtCore.QSize(1024, 720))
        Form.setMouseTracking(True)
        Form.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 85, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
           
        self.label_Foto = QtWidgets.QLabel(Form)
        self.label_Foto.setMouseTracking(True)
        self.label_Foto.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Foto.setAutoFillBackground(False)
        self.label_Foto.setStyleSheet("font: 11pt; background-color: rgb(12, 12, 12);")
        self.label_Foto.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.label_Foto.setAlignment(QtCore.Qt.AlignLeft)
        self.label_Foto.setWordWrap(False)
        self.label_Foto.setObjectName("label_Foto")
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        self.groupBox_Menu = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Menu.setFont(font)
        self.groupBox_Menu.setStyleSheet("font: 15pt; background-color: rgb(0, 0, 0); color: rgb(255,255,255);")
        self.groupBox_Menu.setObjectName("groupBox_Menu")
        
        self.groupBox_Browse = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Browse.setFont(font)
        self.groupBox_Browse.setStyleSheet("font: 13pt; background-color: rgb(0, 0, 0); color: rgb(255,127,36);")
        self.groupBox_Browse.setObjectName("groupBox_Menu")
      
        self.pushButton_fotoAdress = QtWidgets.QPushButton(self.groupBox_Browse)
        self.pushButton_fotoAdress.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(255,127,36);")
        self.pushButton_fotoAdress.setObjectName("pushButton_fotoAdress")
        
        self.label_Width = QtWidgets.QLabel(self.groupBox_Browse)

        self.spinBox_width = QtWidgets.QSpinBox(self.groupBox_Browse)
        self.spinBox_width.setGeometry(QtCore.QRect(240, 50, 71, 22))
        self.spinBox_width.setMinimum(1)
        self.spinBox_width.setMaximum(5000)
        self.spinBox_width.setProperty("value", 640)
        self.spinBox_width.setObjectName("spinBox_width")
        
        self.label_height = QtWidgets.QLabel(self.groupBox_Browse)
        
        self.spinBox_height = QtWidgets.QSpinBox(self.groupBox_Browse)
        self.spinBox_height.setMinimum(1)
        self.spinBox_height.setMaximum(5000)
        self.spinBox_height.setProperty("value", 860)
        self.spinBox_height.setObjectName("spinBox_height")
        
        self.pushButton_PhotoResize = QtWidgets.QPushButton(self.groupBox_Browse)
        self.pushButton_PhotoResize.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(255,127,36);")
        self.pushButton_PhotoResize.setObjectName("pushButton_PhotoResize")
        
        self.groupBox_Manuel = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Manuel.setFont(font)
        self.groupBox_Manuel.setStyleSheet("font: 13pt; background-color: rgb(0, 0, 0); color: rgb(191, 66, 143);")
        self.groupBox_Manuel.setObjectName("groupBox_Manuel")
        
        self.pushButton_Manuel = QtWidgets.QPushButton(self.groupBox_Manuel)
        self.pushButton_Manuel.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(191, 66, 143);")
        self.pushButton_Manuel.setObjectName("pushButton_Manuel")
      
        self.label_temp = QtWidgets.QLabel(self.groupBox_Manuel)
                
        self.groupBox_AutonomousCOCO = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_AutonomousCOCO.setFont(font)
        self.groupBox_AutonomousCOCO.setStyleSheet("font: 13pt; background-color: rgb(0, 0, 0); color: rgb(84, 183,180);")
        self.groupBox_AutonomousCOCO.setObjectName("groupBox_AutonomousCOCO")
                
        self.comboBox_Model = QtWidgets.QComboBox(self.groupBox_AutonomousCOCO)
        self.comboBox_Model.setStyleSheet("font: 11pt; background-color: rgb(238, 255, 221);\n"
"selection-color: rgb(180, 180, 180);\n"
"selection-background-color: rgb(0, 0, 0); color: rgb(0,0,0)")
        self.comboBox_Model.setObjectName("comboBox_Model")
        self.comboBox_Model.addItem("YOLOv5s-COCO")
        self.comboBox_Model.addItem("YOLOv4_tiny-COCO")
        self.comboBox_Model.addItem("YOLOv5-Custom")
        self.comboBox_Model.addItem("YOLOv4-Custom")
     
        self.pushButton_Run = QtWidgets.QPushButton(self.groupBox_AutonomousCOCO)
        self.pushButton_Run.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(84, 183, 180);")
        self.pushButton_Run.setObjectName("pushButton_Run")
        
        self.groupBox_AutonomousCustom = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_AutonomousCustom.setFont(font)
        self.groupBox_AutonomousCustom.setStyleSheet("font: 13pt; background-color: rgb(0, 0, 0); color: rgb(99, 183, 60);")
        self.groupBox_AutonomousCustom.setObjectName("groupBox_AutonomousCustom")
        
        self.comboBox_Import = QtWidgets.QComboBox(self.groupBox_AutonomousCustom)
        self.comboBox_Import.setStyleSheet("font: 11pt; background-color: rgb(238, 255, 221);\n"
"selection-color: rgb(180, 180, 180);\n"
"selection-background-color: rgb(0, 0, 0); color: rgb(0,0,0)")
        self.comboBox_Import.setObjectName("comboBox_Import")
        self.comboBox_Import.addItem("YOLOv5 (.pt)")
        self.comboBox_Import.addItem("YOLOv4 (.cfg)")
        self.comboBox_Import.addItem("YOLOv4 (.weights)")
        self.comboBox_Import.addItem("YOLOv4 (.names)")
        
        self.pushButton_Import = QtWidgets.QPushButton(self.groupBox_AutonomousCustom)
        self.pushButton_Import.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(99, 183, 60);")
        self.pushButton_Import.setObjectName("pushButton_Import")
        
        self.groupBox_AutonomousCustom.setVisible(False)
        
        self.groupBox_Load = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Load.setFont(font)
        self.groupBox_Load.setStyleSheet("font: 13pt; background-color: rgb(0, 0, 0); color: rgb(126, 60, 201);")
        self.groupBox_Load.setObjectName("groupBox_Load")
        
        self.pushButton_Loadtxt = QtWidgets.QPushButton(self.groupBox_Load)
        self.pushButton_Loadtxt.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(126, 60, 201);")
        self.pushButton_Loadtxt.setObjectName("pushButton_Loadtxt")
        
        self.pushButton_LoadtxtNames = QtWidgets.QPushButton(self.groupBox_Load)
        self.pushButton_LoadtxtNames.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(126, 60, 201);")
        self.pushButton_LoadtxtNames.setObjectName("pushButton_LoadtxtNames")
        
        self.pushButton_LoadXml = QtWidgets.QPushButton(self.groupBox_Load)
        self.pushButton_LoadXml.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(126, 60, 201);")
        self.pushButton_LoadXml.setObjectName("pushButton_LoadXml")
        
        self.groupBox_Save = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Save.setFont(font)
        self.groupBox_Save.setStyleSheet("font: 13pt; background-color: rgb(0, 0, 0); color: rgb(252, 121, 121);")
        self.groupBox_Save.setObjectName("groupBox_Save")
        
        self.pushButton_txt = QtWidgets.QPushButton(self.groupBox_Save)
        self.pushButton_txt.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(252, 121, 121);")
        self.pushButton_txt.setObjectName("pushButton_txt")
        
        self.pushButton_xml = QtWidgets.QPushButton(self.groupBox_Save)
        self.pushButton_xml.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(252, 121, 121);")
        self.pushButton_xml.setObjectName("pushButton_xml")
        
        self.groupBox_Label = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Label.setFont(font)
        self.groupBox_Label.setStyleSheet("font: 15pt; background-color: rgb(0, 0, 0); color: rgb(255,255,255);")
        
        self.groupBox_Label.setObjectName("groupBox_Label")

        self.pushButton_LabellingDel = QtWidgets.QPushButton(Form)
        self.pushButton_LabellingDel.setStyleSheet("font: 11pt; background-color: rgb(204, 234, 9);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_LabellingDel.setObjectName("pushButton_LabellingDel")
               
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setStyleSheet("font: 11pt; gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"color: rgb(180, 180, 180);\n"
"background-color: rgb(20,20,20);")
        self.tableWidget.setRowCount(self.row)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(280)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
         
        self.groupBox_LabelName = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_LabelName.setFont(font)
        self.groupBox_LabelName.setStyleSheet("font: 13pt; background-color: rgb(0, 0, 0); color: rgb(204, 234, 9);")
        self.groupBox_LabelName.setObjectName("groupBox_LabelName")
     
        self.pushButton_nameAdd = QtWidgets.QPushButton(self.groupBox_LabelName)
        self.pushButton_nameAdd.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(204, 234, 9);")
        self.pushButton_nameAdd.setObjectName("pushButton_nameAdd")
       
        self.pushButton_NameDel = QtWidgets.QPushButton(self.groupBox_LabelName)
        self.pushButton_NameDel.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(204, 234, 9);")
        self.pushButton_NameDel.setObjectName("pushButton_NameDel")
       
        self.lineEdit_name = QtWidgets.QLineEdit(self.groupBox_LabelName)
        self.lineEdit_name.setStyleSheet("font: 11pt; color: rgb(0,0,0);\n"
"background-color: rgb(238, 255, 221);")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
       
        self.comboBox_name = QtWidgets.QComboBox(self.groupBox_LabelName)
        self.comboBox_name.setStyleSheet("font: 11pt; background-color: rgb(238, 255, 221);\n"
"selection-color: rgb(180, 180, 180);\n"
"selection-background-color: rgb(0, 0, 0); color: rgb(0,0,0)")
        self.comboBox_name.setObjectName("comboBox_name")
        
        self.comboBox_select = QtWidgets.QComboBox(Form)
        self.comboBox_select.setStyleSheet("font: 11pt; background-color: rgb(238, 255, 221);\n"
"selection-color: rgb(180, 180, 180);\n"
"selection-background-color: rgb(0, 0, 0); color: rgb(0,0,0)")
        self.comboBox_select.setObjectName("comboBox_select")
       
        self.pushButton_select = QtWidgets.QPushButton(Form)
        self.pushButton_select.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(204, 234, 9);")
        self.pushButton_select.setObjectName("pushButton_select")
    
        self.hBox_labelAdd.addWidget(self.lineEdit_name)
        self.hBox_labelAdd.addWidget(self.pushButton_nameAdd)
        self.hBox_labelDel.addWidget(self.comboBox_name)
        self.hBox_labelDel.addWidget(self.pushButton_NameDel)
        self.vBox_label.addLayout(self.hBox_labelAdd)
        self.vBox_label.addLayout(self.hBox_labelDel)
        self.groupBox_LabelName.setLayout(self.vBox_label)
      
        self.hBox_table.addWidget(self.comboBox_select)
        self.hBox_table.addWidget(self.pushButton_select)

        self.vBox.addWidget(self.groupBox_LabelName)
        self.vBox.addLayout(self.hBox_table)
        self.vBox.addWidget(self.pushButton_LabellingDel)
        self.vBox.addWidget(self.tableWidget)
        self.vBox.setStretch(0, 2)
        self.vBox.setStretch(1, 1)
        self.vBox.setStretch(2, 1)
        self.vBox.setStretch(3, 5)
        self.groupBox_Label.setLayout(self.vBox)
        
        self.vBox_LM.addWidget(self.plainTextEdit,1)
        self.vBox_LM.addWidget(self.groupBox_Label,7)

        self.hBox.addLayout(self.vBox_LM,1)
        self.hBox.addWidget(self.label_Foto,5)
            
        self.hBox_Size.addWidget(self.label_Width,1)        
        self.hBox_Size.addWidget(self.spinBox_width,5)        
        self.hBox_Size.addWidget(self.label_height,1)        
        self.hBox_Size.addWidget(self.spinBox_height,5)
        self.hBox_Size.addWidget(self.pushButton_PhotoResize,15)
        
        self.vBox_Browse.addWidget(self.pushButton_fotoAdress)
        self.vBox_Browse.addLayout(self.hBox_Size)
        self.groupBox_Browse.setLayout(self.vBox_Browse)
        
        self.vBox_Manuel.addWidget(self.pushButton_Manuel)
        self.vBox_Manuel.addWidget(self.label_temp)
        self.groupBox_Manuel.setLayout(self.vBox_Manuel)
        
        self.vBox_AutonomousCOCO.addWidget(self.comboBox_Model,1)
        self.vBox_AutonomousCOCO.addWidget(self.pushButton_Run,1)
        self.groupBox_AutonomousCOCO.setLayout(self.vBox_AutonomousCOCO)       
        
        self.vBox_AutonomousCustom.addWidget(self.comboBox_Import,1)
        self.vBox_AutonomousCustom.addWidget(self.pushButton_Import,1)
        self.groupBox_AutonomousCustom.setLayout(self.vBox_AutonomousCustom) 
        
        self.hBox_LoadYOLO.addWidget(self.pushButton_Loadtxt)
        self.hBox_LoadYOLO.addWidget(self.pushButton_LoadtxtNames)
        self.vBox_Load.addLayout(self.hBox_LoadYOLO)
        self.vBox_Load.addWidget(self.pushButton_LoadXml)
        self.groupBox_Load.setLayout(self.vBox_Load)        
        
        self.vBox_Save.addWidget(self.pushButton_txt,1)
        self.vBox_Save.addWidget(self.pushButton_xml,1)
        self.groupBox_Save.setLayout(self.vBox_Save)        
        
        self.hBox_menu.addWidget(self.groupBox_Browse,1)
        self.hBox_menu.addWidget(self.groupBox_Manuel,1)
        self.hBox_menu.addWidget(self.groupBox_AutonomousCOCO,1)
        self.hBox_menu.addWidget(self.groupBox_AutonomousCustom,1)
        self.hBox_menu.addWidget(self.groupBox_Load,1)
        self.hBox_menu.addWidget(self.groupBox_Save,1)
        self.groupBox_Menu.setLayout(self.hBox_menu)        
        
        self.vBox_main.addWidget(self.groupBox_Menu)
        self.vBox_main.addLayout(self.hBox)
        self.vBox.setStretch(0, 1)
        self.vBox.setStretch(1, 1)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.pushButton_fotoAdress.clicked.connect(self.openImage)
        self.pushButton_PhotoResize.clicked.connect(self.photoSize)
        self.pushButton_nameAdd.clicked.connect(self.labelAdd)
        self.pushButton_NameDel.clicked.connect(self.labelDel)
        self.pushButton_select.clicked.connect(self.changeName)
        self.pushButton_Manuel.clicked.connect(self.rect)
        self.pushButton_LabellingDel.clicked.connect(self.remove)    
        self.pushButton_Run.clicked.connect(self.RunChoosedModel)
        self.pushButton_Import.clicked.connect(self.importChoosedModel)
        self.pushButton_Loadtxt.clicked.connect(self.LoadTxt)
        self.pushButton_LoadtxtNames.clicked.connect(self.LoadTxtNames)
        self.pushButton_LoadXml.clicked.connect(self.LoadXml)
        self.pushButton_txt.clicked.connect(self.writeTxt)
        self.pushButton_xml.clicked.connect(self.writeXml)
        
        self.comboBox_Model.currentIndexChanged.connect(self.on_combobox_changed)
        self.tableWidget.itemSelectionChanged.connect(self.selectItem)
        
        self.labelxy = self.label_Foto.x(),self.label_Foto.y()
        
        Form.mousePressEvent = self.pressed
        Form.mouseReleaseEvent = self.released
        Form.mouseMoveEvent = self.track
        
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Semi-Supervised Data Annotation Tool"))
        self.groupBox_Menu.setTitle(_translate("Form", "MAIN MENU"))
        self.groupBox_Browse.setTitle(_translate("Form", "Photo"))
        self.label_Width.setText(_translate("Form", "X:"))
        self.label_height.setText(_translate("Form", "Y:"))
        self.pushButton_PhotoResize.setText(_translate("Form", "Resize"))
        self.groupBox_Manuel.setTitle(_translate("Form", "Manuel"))
        self.pushButton_Manuel.setText(_translate("Form", "Rectangle"))
        self.groupBox_AutonomousCOCO.setTitle(_translate("Form", "Autonomous-Run"))
        self.pushButton_Run.setText(_translate("Form", "Run"))
        self.groupBox_AutonomousCustom.setTitle(_translate("Form", "Custom Model-Import"))
        self.pushButton_Import.setText(_translate("Form", "Import"))
        self.groupBox_Load.setTitle(_translate("Form", "Load"))
        self.pushButton_Loadtxt.setText(_translate("Form", "YOLO(txt)"))
        self.pushButton_LoadtxtNames.setText(_translate("Form", "import .names"))
        self.pushButton_LoadXml.setText(_translate("Form", "Pascal(xml)"))
        self.groupBox_Save.setTitle(_translate("Form", "Save"))
        self.pushButton_txt.setText(_translate("Form", "YOLO(txt)"))
        self.pushButton_xml.setText(_translate("Form", "Pascal(xml)"))
        self.groupBox_Label.setTitle(_translate("Form", "LABEL"))
        self.label_Foto.setText(_translate("Form", "Photo"))
        self.pushButton_fotoAdress.setText(_translate("Form", "Browse"))
        self.pushButton_LabellingDel.setText(_translate("Form", "Delete"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Label Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Xstart"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Ystart"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Xfinish"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Yfinish"))
        self.groupBox_LabelName.setTitle(_translate("Form", "Label Name"))
        self.pushButton_nameAdd.setText(_translate("Form", "Add"))
        self.pushButton_NameDel.setText(_translate("Form", "Delete"))
        self.pushButton_select.setText(_translate("Form", "Change Name"))
        self.plainTextEdit.setPlainText(_translate("Form", "Message"))
        
    
    def photoSize(self):
        self.pixmap = self.pixmap.scaled(self.spinBox_width.value(), self.spinBox_height.value(), aspectRatioMode = QtCore.Qt.IgnoreAspectRatio)
        self.label_Foto.setPixmap(self.pixmap)
        self.label_Foto.resize(self.pixmap.width(), self.pixmap.height())
        self.resizePhoto()


    def resizePhoto(self):
        ratio = float(self.spinBox_width.value())/self.beforeSize[0], float(self.spinBox_height.value())/self.beforeSize[1]
        i = 0
        while i <= self.count:
            self.labelL[i].setGeometry(QtCore.QRect(int(self.label_Foto.x()+(self.labelL[i].x()-self.label_Foto.x())*ratio[0]), int(self.label_Foto.y()+(self.labelL[i].y()-self.label_Foto.y())*ratio[1]), int(self.labelL[i].width()*ratio[0]), int(self.labelL[i].height()*ratio[1])))
            self.labelL[i].update()
            self.pushButton_Ex[i].setGeometry(QtCore.QRect(self.labelL[i].x()+self.labelL[i].width()-20, self.labelL[i].y()-20+self.labelL[i].height(),15, 15))
            self.labelText[i].setGeometry(QtCore.QRect(self.labelL[i].x()+5, self.labelL[i].y()+4, self.labelL[i].width()-10, 20))

            self.tableWidget.setItem(i,1, QTableWidgetItem(" "+str(self.labelL[i].x()-self.label_Foto.x())))
            self.tableWidget.setItem(i,2, QTableWidgetItem(" "+str(self.labelL[i].y()-self.label_Foto.y())))
            self.tableWidget.setItem(i,3, QTableWidgetItem(" "+str(self.labelL[i].x()-self.label_Foto.x()+self.labelL[i].width())))
            self.tableWidget.setItem(i,4, QTableWidgetItem(" "+str(self.labelL[i].y()-self.label_Foto.y()+self.labelL[i].height())))
            self.text[i*5+1] = str(self.labelL[i].x()-self.label_Foto.x()) + ","
            self.text[i*5+2] = str(self.labelL[i].y()-self.label_Foto.y()) + ","
            self.text[i*5+3] = str(self.labelL[i].x()-self.label_Foto.x()+self.labelL[i].width()) + ","
            self.text[i*5+4] = str(self.labelL[i].y()-self.label_Foto.y()+self.labelL[i].height()) + "\n"
            i += 1

        self.beforeSize = self.spinBox_width.value(), self.spinBox_height.value()

    #uygulama boyutu değişince optimize etme
    def resizeForm(self):
        i = 0
        while i <= self.count:
            self.pushButton_Ex[i].setGeometry(QtCore.QRect(self.pushButton_Ex[i].x()+self.fark[0], self.pushButton_Ex[i].y()+self.fark[1], 15, 15))
            self.labelL[i].setGeometry(QtCore.QRect(self.labelL[i].x()+self.fark[0], self.labelL[i].y()+self.fark[1], self.labelL[i].width(), self.labelL[i].height()))
            self.labelL[i].update()
            self.labelText[i].setGeometry(QtCore.QRect(self.labelText[i].x()+self.fark[0], self.labelText[i].y()+self.fark[1], self.labelText[i].width(), self.labelText[i].height()))
                
            i += 1

    #yeni fotoğraf eklenince çalışacak
    def clean(self):    
        i=self.count
        while i >= 0:
            self.tableWidget.removeRow(i)
            self.labelL[i].setVisible(False)
            self.pushButton_Ex[i].setVisible(False)
            self.labelText[i].setVisible(False)
            i -= 1

        del self.labelL[:]
        del self.pushButton_Ex[:]
        del self.labelText[:]
        del self.text[:]
        del self.labels[:]
        self.comboBox_name.clear()
        self.comboBox_select.clear()
        
        self.tableWidget.update
        self.row = 0
        self.tableWidget.setRowCount(self.row)
        self.count=-1
        self.status = False #eğer tıklanma yapılırsa true olacak, bırakılınca false olcak
        self.out_str = " "
            
        
    def openImage(self):
        if not self.control == 0:
            self.clean()

        filename = QFileDialog.getOpenFileName()
        if filename[0] == '':
            self.plainTextEdit.setPlainText("File wasn't opened") 
            return
        self.imagePath = filename[0]
        self.pixmap = QPixmap(self.imagePath)
        self.label_Foto.setPixmap(self.pixmap)
        self.label_Foto.resize(self.pixmap.width(),self.pixmap.height())
        self.firstPixmap = self.pixmap.copy()
        self.control = 1
        self.plainTextEdit.setPlainText("File was opened")   
        
        self.spinBox_width.setValue(self.pixmap.width())
        self.spinBox_height.setValue(self.pixmap.height())
        self.beforeSize = self.pixmap.width(), self.pixmap.height()
         
        
    def LoadXml(self):
        if self.control==0:
            self.plainTextEdit.setPlainText("Please add a photo") 
            return
        filename = QFileDialog.getOpenFileName()
        if filename[0] == '':
            self.plainTextEdit.setPlainText("File wasn't opened") 
            return
        LoadFile = filename[0]
        
        tree = ET.parse(LoadFile)
        root = tree.getroot()
        
        ratio = self.pixmap.width()/self.firstPixmap.width(), self.pixmap.height()/self.firstPixmap.height()
        
        i = 0
        for r in root:
            if i > 5:
                self.row += 1
                self.count += 1
                self.createLabel() 
                self.text.append(str(r[0].text))
                self.text.append(str(int(int(r[4][0].text)*ratio[0])))
                self.text.append(str(int(int(r[4][1].text)*ratio[1])))
                self.text.append(str(int(int(r[4][2].text)*ratio[0])))
                self.text.append(str(int(int(r[4][3].text)*ratio[1])))
            i += 1
        
        self.plainTextEdit.setPlainText(".xml was read\n Reading format: Pascal")    
        self.setupLoad()
        
        
    def LoadTxtNames(self):
        filename = QFileDialog.getOpenFileName()
        if filename[0] == '':
            self.plainTextEdit.setPlainText(".names wasn't opened") 
            return
        self.plainTextEdit.setPlainText(".names was opened") 
        self.loadName = filename[0]
        self.nameSelect = 2
        self.getNameClass()
        

        
    def LoadTxt(self):
        if self.control==0:
            self.plainTextEdit.setPlainText("Please add a photo") 
            return
        if not self.nameSelect == 2: 
            self.plainTextEdit.setPlainText("Please, import .names") 
            return
            
        filename = QFileDialog.getOpenFileName()
        if filename[0] == '':
            self.plainTextEdit.setPlainText("File wasn't opened") 
            return
        LoadFile = filename[0]
        
        load = open(LoadFile,'r')
        for line in load:
            self.row += 1
            self.count += 1
            self.createLabel()
            temp = ""
            i=0
            for l in line:
                if not l=='\n':
                    temp += l
                if l==' ':
                    if i==0:
                        tempI = int(temp)
                        self.text.append(self.labels[tempI])
                    elif i==1:
                        tempI = float(temp)*self.spinBox_width.value()
                        self.text.append(str(int(tempI)))                        
                    elif i==2:  
                        tempI = float(temp)*self.spinBox_height.value()
                        self.text.append(str(int(tempI)))                        
                    elif i==3:                      
                        tempI = float(temp)*self.spinBox_width.value()
                        self.text[-2] = str(int(self.text[-2])-int(tempI/2))
                        self.text.append(str(int(tempI+int(self.text[-2]))))                        
                    i += 1
                    temp = ""            
            tempI = float(temp)*self.spinBox_height.value()
            self.text[-2] = str(int(self.text[-2])-int(tempI/2))
            self.text.append(str(int(tempI+int(self.text[-2]))))      

        self.plainTextEdit.setPlainText(".txt was read\n Reading format: YOLO")
        self.setupLoad()

        #etiket bilgilerini import etme
    def setupLoad(self):
        self.tableWidget.setRowCount(self.row)
        i=0
        while i<=self.count:
            flag = 0
            for j in range(self.comboBox_name.count()):
                if self.text[i*5] == self.comboBox_name.itemText(j):
                    flag = 1
            if flag == 0:
                self.comboBox_name.addItem(self.text[i*5])
                self.comboBox_select.addItem(self.text[i*5])
                    
            self.labelL[i].setStyleSheet("background: transparent; border: 5px solid red; color: rgb(255, 85, 0);")
            self.labelL[i].setObjectName("labelL")
    
            self.labelText[i].setStyleSheet("background: rgba(0, 0, 0, 0.5); color: rgb(255, 255, 255); font: 75 8pt 'Bahnschrift';")
            self.labelText[i].setObjectName("labelText")
    
            self.pushButton_Ex[i].setStyleSheet("background-color: rgb(20, 20, 20); color: rgb(255, 85, 0)")
            self.pushButton_Ex[i].setText(" X")
            self.pushButton_Ex[i].setObjectName("pushButton_Ex")

            self.pushButton_Ex[i].setGeometry(QtCore.QRect(self.label_Foto.x()+int(self.text[i*5+3])-17,self.label_Foto.y()+int(self.text[i*5+4])-17,15,15))
            self.labelL[i].setGeometry(QtCore.QRect(self.label_Foto.x()+int(self.text[i*5+1]),self.label_Foto.y()+int(self.text[i*5+2]),int(self.text[i*5+3])-int(self.text[i*5+1]),int(self.text[i*5+4])-int(self.text[i*5+2])))
            self.labelText[i].setGeometry(QtCore.QRect(self.label_Foto.x()+5+int(self.text[i*5+1]),self.label_Foto.y()+int(self.text[i*5+2])+5,int(self.text[i*5+3])-int(self.text[i*5+1])-10,20))
            
            self.labelText[i].setText(" " + self.text[i*5])
            
            self.labelL[i].setVisible(True)
            self.pushButton_Ex[i].setVisible(True)
            self.labelText[i].setVisible(True)
            
            self.tableWidget.setItem(i,0, QTableWidgetItem(str(self.text[i*5])))
            self.tableWidget.setItem(i,1, QTableWidgetItem(str(self.text[i*5+1])))
            self.tableWidget.setItem(i,2, QTableWidgetItem(str(self.text[i*5+2])))
            self.tableWidget.setItem(i,3, QTableWidgetItem(str(self.text[i*5+3])))
            self.tableWidget.setItem(i,4, QTableWidgetItem(str(self.text[i*5+4])))
            
            i += 1
        
    def write(self):
        if self.imagePath == "":
            self.plainTextEdit.setPlainText("Please select a file")
            return False
        if self.control == 0:
            self.plainTextEdit.setPlainText("Please add a photo")
            return False
        
        if len(self.out_str.join(self.text)) < 2 :
            self.plainTextEdit.setPlainText("Please add a label, there is no label")
            return False
        return True

    
    def writeXml(self):
        if not self.write():
            return
        
        output = ""
        fiName = ""        
        foName = ""
        for i in self.imagePath:
            if i=='/':
                foName = fiName
                output += foName
                fiName = ""
            fiName += i

        root = Element("annotation")
        
        folder = SubElement(root, "folder")
        folder.text = foName
        
        filename = SubElement(root, "filename")
        filename.text = fiName
        
        path = SubElement(root, "path")
        path.text = self.imagePath
        
        source = SubElement(root, "source")
        database = SubElement(source, "database")  
        database.text = "Unknown"    
        
        size = SubElement(root, "size")
        width = SubElement(size, "width")
        width.text = str(self.firstPixmap.width())    
        height = SubElement(size, "height")
        height.text = str(self.firstPixmap.height())  
        depth = SubElement(size, "depth")
        depth.text = "3"
        
        segmented = SubElement(root, "segmented")
        segmented.text = "0"
      
        ratio = self.firstPixmap.width()/self.pixmap.width(), self.firstPixmap.height()/self.pixmap.height()
   
        i=0
        while i<=self.count:
            object1 = SubElement(root, "object")
            
            name = SubElement(object1,"name")
            name.text = self.text[i*5]
            print(self.text[i*5])
            pose = SubElement(object1,"pose")
            pose.text = "Unspecified"
            truncated = SubElement(object1,"truncated")
            truncated.text = "0"
            difficult = SubElement(object1,"difficult")
            difficult.text = "0"
            
            bndbox = SubElement(object1, "bndbox")
            tempI = int(''.join(self.text[i*5+1]))
            xmin = SubElement(bndbox,"xmin")
            xmin.text = str(int(tempI*ratio[0]))
            tempI = int(''.join(self.text[i*5+2]))
            ymin = SubElement(bndbox,"ymin")
            ymin.text = str(int(tempI*ratio[1]))
            tempI = int(''.join(self.text[i*5+3]))
            xmax = SubElement(bndbox,"xmax")
            xmax.text = str(int(tempI*ratio[0]))
            tempI = int(''.join(self.text[i*5+4]))
            ymax = SubElement(bndbox,"ymax")
            ymax.text = str(int(tempI*ratio[1]))
            i += 1
            
        fileNew = ""
        for i in self.imagePath:
            if i=='.':
                break
            fileNew += i                   
        
        tree = ElementTree(root)
      
        with open (fileNew+".xml", "wb") as files :
            tree.write(files)
            
        self.plainTextEdit.setPlainText(".xml was writed\nWriting format: Pascal")    

        
    def writeTxt(self):
        self.write()
        if not self.write():
            return      
        file = ""
        for i in self.imagePath:
            if i=='.':
                break
            file += i                   
        self.filetxt = open(file+".txt", "w")
        
        print(self.labels)
        
        i = 0
        while i <= self.count:
            class_name = self.text[i*5]
            class_name = class_name.replace('\n','')
            class_name = class_name.replace(' ','')
            class_name = self.labels.index(class_name)
            
            start_x = self.text[i*5+1]
            start_x_f = float(start_x)
            
            start_y = self.text[i*5+2]
            start_y_f = float(start_y)
            
            end_x = self.text[i*5+3]
            end_x_f = float(end_x)
            
            end_y = self.text[i*5+4]
            end_y_f = float(end_y)
            
            width_f = end_x_f - start_x_f
            height_f = end_y_f - start_y_f
            
            center_x_f = start_x_f + width_f / 2.0
            center_y_f = start_y_f + height_f / 2.0
            
            center_x_f /= self.spinBox_width.value()
            width_f /= self.spinBox_width.value()
            center_y_f /= self.spinBox_height.value()
            height_f /= self.spinBox_height.value()
            
            line = ""
            line += str(class_name)+ " "
            line += str(center_x_f) + " "
            line += str(center_y_f) + " "
            line += str(width_f) + " "
            line += str(height_f) + "\n"
            self.filetxt.write(line)
            
            i += 1
            
        self.plainTextEdit.setPlainText(".txt was writed\nWriting format: YOLO")        
        self.filetxt.close()
 
 
    def rect(self):
        if not self.openMode == 2 and not self.openMode == 3:    
            if self.openMode == 0:
                self.pushButton_Manuel.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(231, 100, 203);")
                self.plainTextEdit.setPlainText("Rectangle is enabled")        
                self.openMode = 1
            else:
                self.pushButton_Manuel.setStyleSheet("font: 11pt; color: rgb(0, 0, 0);\n"
"background-color: rgb(191, 66, 143);")
                self.plainTextEdit.setPlainText("Rectangle is disabled")        
                self.openMode = 0
        
        
    def RunChoosedModel(self):
        if self.control == 0:
            self.plainTextEdit.setPlainText("Please add a photo")
            return
        
        indeks = self.comboBox_Model.currentIndex()
        if indeks == 0:
            self.plainTextEdit.setPlainText("Please wait, Yolov5s is loading")   
            self.model = torch.hub.load('ultralytics/yolov5','yolov5s')
            self.plainTextEdit.setPlainText("Yolov5s was loaded")   
            self.yolov5()
        elif indeks == 1:
            self.yolov4COCO()
        elif indeks == 2:
            if self.ptControl == 1:
                self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=self.customYolov5)
                self.yolov5()   
            else:
                self.plainTextEdit.setPlainText("Please import .pt")   
        elif indeks == 3:
            if self.cfgControl == 1 and self.weightsControl == 1 and self.namesControl == 1:
                self.yolov4Custom()
            else:
                self.plainTextEdit.setPlainText("Please import files")   

    def yolov5(self):
        if self.control == 0:
            self.plainTextEdit.setPlainText("Please add a photo")
            return
        """    
        if not self.openMode == 1 and not self.openMode == 2:
            if not self.openMode == 0:
                self.plainTextEdit.setPlainText("Oto-guided is disabled")        
                self.openMode = 0
            else:
                self.plainTextEdit.setPlainText("Oto-guided is enabled")        
                self.openMode = 3
        """           
        ratio = self.pixmap.width()/self.firstPixmap.width(),self.pixmap.height()/self.firstPixmap.height()
        
        results = self.model(self.imagePath)
        self.labels.extend(results.names)
        box_list = results.xyxy
        box_str = ""
        box_str = ''.join(str(l) for l in box_list)
        box_str = box_str.replace('tensor','')
        box_str = box_str.replace(')','')
        box_str = box_str.replace('(','')
        box_str = box_str.replace(']','')
        box_str = box_str.replace('[','')

        box_int = []
        
        temp = ""
        sum_oto_label = 0
        j = 0
        for i in box_str:
            if i == ',':
                tempf = float(temp)
                format(tempf, 'f')
                if j == 4:
                    box_int.append(tempf)
                else:    
                    box_int.append(int(tempf))
                temp = ""
                j += 1
                j %= 6
                sum_oto_label += 1
            else :
                temp += i
        tempf = float(temp)                        
        box_int.append(int(tempf))
        sum_oto_label /= 6
        
        count_oto_label = 0
        while count_oto_label < sum_oto_label:         
            scores = box_int[count_oto_label*6+4]*100
            if scores > 40:
            
                start_x = box_int[count_oto_label*6+0]
                start_y = box_int[count_oto_label*6+1]
        
                end_x = box_int[count_oto_label*6+2]
                end_y = box_int[count_oto_label*6+3]
            
                label = self.labels[box_int[count_oto_label*6+5]]
                
                flag = 0
                for i in range(self.comboBox_name.count()):
                    if label == self.comboBox_name.itemText(i):
                        flag = 1
                if flag == 0:
                    self.comboBox_name.addItem(label)
                    self.comboBox_select.addItem(label)
                
                self.count += 1
                self.createLabel()
            
                self.labelL[self.count].setStyleSheet("background: transparent; border: 5px solid red; color: rgb(255, 85, 0);")
                self.labelL[self.count].setObjectName("labelL")
    
                self.labelText[self.count].setStyleSheet("background: rgba(0, 0, 0, 0.5); color: rgb(255, 255, 255); font: 75 8pt 'Bahnschrift';")
                self.labelText[self.count].setObjectName("labelText")
    
                self.pushButton_Ex[self.count].setStyleSheet("background-color: rgb(20, 20, 20); color: rgb(255, 85, 0)")
                self.pushButton_Ex[self.count].setText(" X")
                self.pushButton_Ex[self.count].setObjectName("pushButton_Ex")

                self.row += 1
                self.tableWidget.setRowCount(self.row)
                self.tableWidget.setItem(self.row-1,0, QTableWidgetItem(label))
                self.text.append(label)
            
                label = "{}: {:.2f}%".format(label, scores)
                self.labelText[self.count].setText(" "+label)
            
                self.tableWidget.setItem(self.row-1,1, QTableWidgetItem(str(int(start_x*ratio[0]))))
                self.tableWidget.setItem(self.row-1,2, QTableWidgetItem(str(int(start_y*ratio[1]))))
                self.tableWidget.setItem(self.row-1,3, QTableWidgetItem(str(int(end_x*ratio[0]))))
                self.tableWidget.setItem(self.row-1,4, QTableWidgetItem(str(int(end_y*ratio[1]))))
                self.text.append(str(int(start_x*ratio[0])))
                self.text.append(str(int(start_y*ratio[1])))
                self.text.append(str(int(end_x*ratio[0])))
                self.text.append(str(int(end_y*ratio[1]))+"\n")
                
                self.pushButton_Ex[self.count].setGeometry(QtCore.QRect(self.label_Foto.x()+int(end_x*ratio[0])-17,self.label_Foto.y()+int(end_y*ratio[1])-17,15,15))
                self.labelL[self.count].setGeometry(QtCore.QRect(self.label_Foto.x()+int(start_x*ratio[0]),self.label_Foto.y()+int(start_y*ratio[1]),int((end_x-start_x)*ratio[0]),int((end_y-start_y)*ratio[1])))
                self.labelText[self.count].setGeometry(QtCore.QRect(self.label_Foto.x()+5+int(start_x*ratio[0]),self.label_Foto.y()+int(start_y*ratio[1])+5,int((end_x-start_x)*ratio[0])-10,20))
                
                self.labelL[self.count].setVisible(True)
                self.pushButton_Ex[self.count].setVisible(True)
                self.labelText[self.count].setVisible(True)
            count_oto_label += 1

        
    def yolov4(self):
        ratio = self.pixmap.width()/self.firstPixmap.width(),self.pixmap.height()/self.firstPixmap.height()
        
        img = cv2.imread(self.imagePath)
        
        img_width = img.shape[1]
        img_height = img.shape[0]
        
        img_blob = cv2.dnn.blobFromImage(img, 1/255, (416,416), swapRB=True, crop=False)

        model = cv2.dnn.readNetFromDarknet(self.cfg, self.weights)
        
        layers = model.getLayerNames()
        output_layer = [layers[layer[0]-1] for layer in model.getUnconnectedOutLayers()]
        
        model.setInput(img_blob)
        
        detection_layers = model.forward(output_layer)
        
        ids_list = []
        boxes_list = []
        confidences_list = []
        
        for detection_layer in detection_layers:
            for object_detection in detection_layer:
        
                scores = object_detection[5:]
                predicted_id = np.argmax(scores)
                confidence = scores[predicted_id]
                
                if confidence > 0.30:
                    
                    label = self.labelNames[predicted_id]
                    bounding_box = object_detection[0:4] * np.array([img_width,img_height,img_width,img_height])
                    (box_center_x, box_center_y, box_width, box_height) = bounding_box.astype("int")
                    
                    start_x = int(box_center_x - (box_width/2))
                    start_y = int(box_center_y - (box_height/2))
                    
                    ids_list.append(predicted_id)
                    confidences_list.append(float(confidence))
                    boxes_list.append([start_x, start_y, int(box_width), int(box_height)])
        
        max_ids = cv2.dnn.NMSBoxes(boxes_list, confidences_list, 0.5, 0.4)
     
        for max_id in max_ids:         
            max_class_id = max_id[0]
            box = boxes_list[max_class_id]
            
            start_x = box[0] 
            start_y = box[1] 
            box_width = box[2] 
            box_height = box[3] 
             
            predicted_id = ids_list[max_class_id]
            label = self.labelNames[predicted_id]
            confidence = confidences_list[max_class_id]
            
            end_x = start_x + box_width
            end_y = start_y + box_height
                                          
            confidence = confidence*100                  
            
            flag = 0
            for i in range(self.comboBox_name.count()):
                if label == self.comboBox_name.itemText(i):
                    flag = 1
            
            if flag == 0:
                self.comboBox_name.addItem(label)
                self.comboBox_select.addItem(label)
            
            self.count += 1
            self.createLabel()
        
            self.labelL[self.count].setStyleSheet("background: transparent; border: 5px solid red; color: rgb(255, 85, 0);")
            self.labelL[self.count].setObjectName("labelL")

            self.labelText[self.count].setStyleSheet("background: rgba(0, 0, 0, 0.5); color: rgb(255, 255, 255); font: 75 8pt 'Bahnschrift';")
            self.labelText[self.count].setObjectName("labelText")

            self.pushButton_Ex[self.count].setStyleSheet("background-color: rgb(20, 20, 20); color: rgb(255, 85, 0)")
            self.pushButton_Ex[self.count].setText(" X")
            self.pushButton_Ex[self.count].setObjectName("pushButton_Ex")

            self.row += 1
            self.tableWidget.setRowCount(self.row)
            self.tableWidget.setItem(self.row-1,0, QTableWidgetItem(label))
            self.text.append(label)
        
            label = "{}: {:.2f}%".format(label, confidence)
            self.labelText[self.count].setText(" "+label)
    
            self.tableWidget.setItem(self.row-1,1, QTableWidgetItem(str(int(start_x*ratio[0]))))
            self.tableWidget.setItem(self.row-1,2, QTableWidgetItem(str(int(start_y*ratio[1]))))
            self.tableWidget.setItem(self.row-1,3, QTableWidgetItem(str(int(end_x*ratio[0]))))
            self.tableWidget.setItem(self.row-1,4, QTableWidgetItem(str(int(end_y*ratio[1]))))
            self.text.append(str(int(start_x*ratio[0])))
            self.text.append(str(int(start_y*ratio[1])))
            self.text.append(str(int(end_x*ratio[0])))
            self.text.append(str(int(end_y*ratio[1]))+"\n")
            
            self.pushButton_Ex[self.count].setGeometry(QtCore.QRect(self.label_Foto.x()+int(end_x*ratio[0])-17,self.label_Foto.y()+int(end_y*ratio[1])-17,15,15))
            self.labelL[self.count].setGeometry(QtCore.QRect(self.label_Foto.x()+int(start_x*ratio[0]),self.label_Foto.y()+int(start_y*ratio[1]),int((end_x-start_x)*ratio[0]),int((end_y-start_y)*ratio[1])))
            self.labelText[self.count].setGeometry(QtCore.QRect(self.label_Foto.x()+5+int(start_x*ratio[0]),self.label_Foto.y()+int(start_y*ratio[1])+5,int((end_x-start_x)*ratio[0])-10,20))
                       
            self.labelL[self.count].setVisible(True)
            self.pushButton_Ex[self.count].setVisible(True)
            self.labelText[self.count].setVisible(True)
    

    def yolov4COCO(self):
        self.weights = "yolov4-tiny/yolov4-tiny.weights"
        self.cfg = "yolov4-tiny/yolov4-tiny.cfg"
        self.labelNames = ["person","bicycle","car","motorcycle","airplane","bus","train","truck","boat",
             "trafficlight","firehydrant","stopsign","parkingmeter","bench","bird","cat",
             "dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack",
             "umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sportsball",
             "kite","baseballbat","baseballglove","skateboard","surfboard","tennisracket",
             "bottle","wineglass","cup","fork","knife","spoon","bowl","banana","apple",
             "sandwich","orange","broccoli","carrot","hotdog","pizza","donut","cake","chair",
             "sofa","pottedplant","bed","diningtable","toilet","tvmonitor","laptop","mouse",
             "remote","keyboard","cellphone","microwave","oven","toaster","sink","refrigerator",
             "book","clock","vase","scissors","teddybear","hairdrier","toothbrush"]
        self.yolov4()

        
    def yolov4Custom(self):
        self.weights = self.customYolov4weights
        self.cfg = self.customYolov4cfg
        self.nameSelect = 1
        self.getNameClass()
        self.yolov4()

        #sınıf isimlerini ekleme
    def getNameClass(self):
        if self.nameSelect == 1:
            fileName = open(self.customYolov4names,"r")
        elif self.nameSelect == 2:
            fileName = open(self.loadName,"r")
        else:    
            self.plainTextEdit.setPlainText("missing file") 
        for line in fileName:
            l = line.replace("\n", "")
            self.labelNames.append(l)
            self.labels.append(l)
        fileName.close()
        

    def importChoosedModel(self):
        indeks = self.comboBox_Import.currentIndex()
        if indeks == 0:
            self.importYOLOv5Custom()
        elif indeks == 1:
            self.importYOLOv4cfg()
        elif indeks == 2:
            self.importYOLOv4weights()   
        elif indeks == 3:
            self.importYOLOv4names()
        
        
    def importYOLOv5Custom(self):
        filename = QFileDialog.getOpenFileName()
        if filename[0] == '':
            self.plainTextEdit.setPlainText(".pt wasn't opened") 
            return
        self.plainTextEdit.setPlainText(".pt was opened") 
        self.customYolov5 = filename[0]
        self.ptControl = 0
        

    def importYOLOv4cfg(self):
        filename = QFileDialog.getOpenFileName()
        if filename[0] == '':
            self.plainTextEdit.setPlainText(".cfg wasn't opened") 
            return
        self.plainTextEdit.setPlainText(".cfg was opened") 
        self.customYolov4cfg = filename[0]
        self.cfgControl = 1



    def importYOLOv4weights(self):
        filename = QFileDialog.getOpenFileName()
        if filename[0] == '':
            self.plainTextEdit.setPlainText(".weights wasn't opened") 
            return
        self.plainTextEdit.setPlainText(".weights was opened") 
        self.customYolov4weights = filename[0]
        self.weightsControl = 1
        

    def importYOLOv4names(self):
        filename = QFileDialog.getOpenFileName()
        if filename[0] == '':
            self.plainTextEdit.setPlainText(".names wasn't opened") 
            return
        self.plainTextEdit.setPlainText(".names was opened") 
        self.customYolov4names = filename[0]
        self.namesControl = 1

    
    def setLabels(self):
        copy = self.firstPixmap.copy()    
        self.pixmap = QPixmap(self.labelL[self.count].size())
        self.pixmap.fill(Qt.transparent)
        qp = QPainter(self.pixmap)
        pen = QPen(Qt.red, 3)
        qp.setPen(pen)
        x1 = self.labelL[self.count].width()
        y1 = self.labelL[self.count].height()
        qp.drawLine(0, 0, x1, y1)
        self.labelL[self.count].setPixmap(self.pixmap)
        qp.end()
        self.firstPixmap = self.pixmap
        self.pixmap = copy
        self.labelL[self.count].update()
        
        #Seçilen label mavi renk oluyor
    def selectItem(self):
        j = 0
        while j < self.row:
            self.labelL[j].setStyleSheet("background: transparent; border: 5px solid red; color: rgb(255, 85, 0);")            
            j += 1
        i=self.tableWidget.currentRow()
        self.labelL[i].setStyleSheet("background: transparent; border: 5px solid blue; color: rgb(255, 85, 0);")
            
         
    #tablo üstünden silme
    def remove(self, state):
        if self.control == 0:
            self.plainTextEdit.setPlainText("Please add a photo")
            return
        if not self.row > 0:
            self.plainTextEdit.setPlainText("Please add a label on the photo")
            return
        i=self.tableWidget.currentRow()
        if not i > -1:
            self.plainTextEdit.setPlainText("Please select first")            
            return
        
        self.tableWidget.removeRow(i)
        
        self.labelL[i].setVisible(False)
        self.pushButton_Ex[i].setVisible(False)
        self.labelText[i].setVisible(False)
                        
        del self.text[i*5]
        del self.text[i*5]
        del self.text[i*5]
        del self.text[i*5]
        del self.text[i*5]
      
        del self.labelL[i]
        del self.labelText[i]
        del self.pushButton_Ex[i]
             
        self.row -= 1
        self.count -= 1
        self.tableWidget.setRowCount(self.row) 
        self.plainTextEdit.setPlainText("label was deleted")        
        
    #Fotoğraf üstünden silme
    def on_click_del(self):        
        i = 0
        while i <= self.count:
            if self.pushButton_Ex[i].isChecked():
                break
            i+=1

        self.tableWidget.removeRow(i)
        
        self.labelL[i].setVisible(False)
        self.pushButton_Ex[i].setVisible(False)
        self.labelText[i].setVisible(False)
        
        del self.text[i*5]
        del self.text[i*5]
        del self.text[i*5]
        del self.text[i*5]
        del self.text[i*5]
        
        del self.labelL[i]
        del self.labelText[i]
        del self.pushButton_Ex[i]
           
        self.row -= 1
        self.count -= 1
        self.tableWidget.setRowCount(self.row) 
        self.plainTextEdit.setPlainText("Label was deleted")        
        
    #label ismi ekleme
    def labelAdd(self):
        if self.lineEdit_name.text() == "":
            self.plainTextEdit.setPlainText("Please write a new label name")            
            return        

        flag = 0
        for i in range(self.comboBox_name.count()):
            if self.lineEdit_name.text() == self.comboBox_name.itemText(i):
                flag = 1
        if flag == 0:
            self.comboBox_name.addItem(self.lineEdit_name.text())
            self.comboBox_select.addItem(self.lineEdit_name.text())
            self.labels.append(self.lineEdit_name.text())
            
        self.lineEdit_name.clear()
        self.plainTextEdit.setPlainText("New label name was added")
        
        #label ismi silme
    def labelDel(self):
        i = self.comboBox_name.currentIndex()
        if i == -1:
            self.plainTextEdit.setPlainText("Please add a label name")        
            return
        
        self.comboBox_name.removeItem(i)
        self.comboBox_select.removeItem(i)
        self.plainTextEdit.setPlainText("Label name was deleted")        
    
    #isim değiştirme
    def changeName(self):
        if self.control == 0:
            self.plainTextEdit.setPlainText("Please add a photo")
            return
        if self.row < 1:
            self.plainTextEdit.setPlainText("Please add a label on the photo")
            return
        
        i = self.tableWidget.currentRow()
        self.tableWidget.setItem(i,0, QTableWidgetItem(self.comboBox_select.currentText()))
        self.text[i*5] = self.comboBox_select.currentText()
        self.labelText[i].setText(" "+self.comboBox_select.currentText())
        self.plainTextEdit.setPlainText("Label name was changed")        
    
    #label olutururken isim atama
    def selectName(self):
        self.row += 1
        self.tableWidget.setRowCount(self.row)
        self.tableWidget.setItem(self.row-1,0, QTableWidgetItem(self.comboBox_select.currentText()))
        self.text.append(self.comboBox_select.currentText())
        self.labelText[self.count].setText(" "+self.comboBox_select.currentText())

    
    def setTable(self):
        self.tableWidget.setItem(self.row-1,1, QTableWidgetItem(str(self.startIndex[0]-self.label_Foto.x())))
        self.tableWidget.setItem(self.row-1,2, QTableWidgetItem(str(self.startIndex[1]-self.label_Foto.y())))
        self.tableWidget.setItem(self.row-1,3, QTableWidgetItem(str(self.finishIndex[0]-self.label_Foto.x())))
        self.tableWidget.setItem(self.row-1,4, QTableWidgetItem(str(self.finishIndex[1]-self.label_Foto.y())))
        self.text.append(str(self.startIndex[0]-self.label_Foto.x()))
        self.text.append(str(self.startIndex[1]-self.label_Foto.y()))
        self.text.append(str(self.finishIndex[0]-self.label_Foto.x()))
        self.text.append(str(self.finishIndex[1]-self.label_Foto.y())+"\n")
        
     #Mouse tıklama
    def pressed(self, event):
        self.startIndex = (event.pos().x(), event.pos().y())
        if self.control == 0:
            self.plainTextEdit.setPlainText("Please add a photo")
            return
        if self.startIndex[0] >= self.label_Foto.x() and self.startIndex[1] >= self.label_Foto.y() and self.startIndex[0] <= self.label_Foto.x()+self.pixmap.width() and self.startIndex[1] <= self.label_Foto.y()+self.pixmap.height() :
            if self.openMode == 0 or self.openMode == 3:
                self.plainTextEdit.setPlainText("Please change the Label Mod")
                return
            self.count += 1
            self.status = True
            self.createLabel()
            self.labelL[self.count].setGeometry(QtCore.QRect(self.startIndex[0],self.startIndex[1],0,0))
            if self.openMode == 1:
                self.labelL[self.count].setStyleSheet("background: transparent; border: 5px solid red; color: rgb(255, 85, 0);")
            elif self.openMode == 2:
                self.labelL[self.count].setStyleSheet("background: transparent; color: rgb(255, 85, 0);")
            
            self.labelL[self.count].setObjectName("labelL")
            
            self.labelText[self.count].setGeometry(QtCore.QRect(self.startIndex[0],self.startIndex[1],0,0))
            self.labelText[self.count].setStyleSheet("background: rgba(0, 0, 0, 0.5); color: rgb(255, 255, 255); font: 75 8pt 'Bahnschrift';")
            self.labelText[self.count].setObjectName("labelText")
            
            self.pushButton_Ex[self.count].setGeometry(QtCore.QRect(self.startIndex[0],self.startIndex[1],0,0))
            self.pushButton_Ex[self.count].setStyleSheet("background-color: rgb(20, 20, 20); color: rgb(255, 85, 0)")
            self.pushButton_Ex[self.count].setText(" X")
            self.pushButton_Ex[self.count].setObjectName("pushButton_Ex")
           
            self.labelL[self.count].setVisible(True)
            self.pushButton_Ex[self.count].setVisible(True)
            
      #Mouse bırakma
    def released(self, event):
        if self.status == True:    
            if self.control == 0:
                self.plainTextEdit.setPlainText("Please add a photo")
                return
            if self.openMode == 0:
                self.plainTextEdit.setPlainText("Please enable the Manuel Mod")
                return
            elif self.openMode == 1:
                self.firstPixmap = self.pixmap
            self.selectName()
            self.setTable()
            self.plainTextEdit.setPlainText("Label was added") 
            self.labelText[self.count].setVisible(True)
        self.status = False
        
        #Mouse anlık
    def track(self, event):
        if (not self.labelxy[0] == self.label_Foto.x()) or (not  self.labelxy[1] == self.label_Foto.y()): 
            self.fark = self.label_Foto.x() - self.labelxy[0] , self.label_Foto.y() -self.labelxy[1]
            self.labelxy = self.label_Foto.x(), self.label_Foto.y()
            self.resizeForm()
            
        if self.control == 0:
            return
        x = event.pos().x()
        y = event.pos().y()
      
        if(self.status == True):
            if(x <= self.label_Foto.x()+self.pixmap.width() and y <= self.label_Foto.y()+self.pixmap.height()):
                xLen =  x - self.startIndex[0]
                yLen =  y - self.startIndex[1]
                
                self.finishIndex = (self.labelL[self.count].pos().x()+xLen, self.labelL[self.count].pos().y()+yLen)                
                self.pushButton_Ex[self.count].setGeometry(QtCore.QRect(self.finishIndex[0]-20,self.finishIndex[1]-20,15,15))
                self.labelL[self.count].setGeometry(QtCore.QRect(self.startIndex[0],self.startIndex[1],xLen,yLen))
                self.labelL[self.count].update()
                self.labelText[self.count].setGeometry(QtCore.QRect(self.startIndex[0]+5,self.startIndex[1]+5,abs(xLen-10),20))
                if self.openMode == 2:
                    self.setLabels()

    
    def createLabel(self):
        temp1=QtWidgets.QLabel(Form)
        self.labelL.append(temp1)

        temp2=QtWidgets.QLabel(Form)
        self.labelText.append(temp2)

        temp3=QtWidgets.QPushButton(Form)
        self.pushButton_Ex.append(temp3)
        self.pushButton_Ex[self.count].clicked.connect(self.on_click_del)
        self.pushButton_Ex[self.count].setCheckable(True)
    
    
    def on_combobox_changed(self, value):
        if value == 0 or value == 1:
            self.groupBox_AutonomousCustom.setVisible(False)
        else:
            self.groupBox_AutonomousCustom.setVisible(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
