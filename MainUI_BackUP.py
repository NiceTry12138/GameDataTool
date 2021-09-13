# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, pyqtSignal

from AnalysisJson import analysisJson
from AnalysisExcel import analysisExcel
from AnalysisXML import analysisXML
import Program_Function

class Ui_MainWindow(QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 560)
        MainWindow.setMinimumSize(QtCore.QSize(920, 560))
        MainWindow.setMaximumSize(QtCore.QSize(920, 560))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 920, 500))
        self.tabWidget.setMinimumSize(QtCore.QSize(920, 500))
        self.tabWidget.setMaximumSize(QtCore.QSize(920, 500))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.page1_text = QtWidgets.QTextBrowser(self.tab_1)
        self.page1_text.setGeometry(QtCore.QRect(480, 12, 400, 450))
        self.page1_text.setObjectName("page1_text")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.page1_Init = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.page1_Init.setMinimumSize(QtCore.QSize(0, 50))
        self.page1_Init.setObjectName("page1_Init")
        self.verticalLayout.addWidget(self.page1_Init)
        self.page1_Analysis = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.page1_Analysis.setMinimumSize(QtCore.QSize(0, 50))
        self.page1_Analysis.setObjectName("page1_Analysis")
        self.verticalLayout.addWidget(self.page1_Analysis)
        self.page1_Struct = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.page1_Struct.setMinimumSize(QtCore.QSize(0, 50))
        self.page1_Struct.setObjectName("page1_Struct")
        self.verticalLayout.addWidget(self.page1_Struct)
        self.page1_Rapdjson = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.page1_Rapdjson.setMinimumSize(QtCore.QSize(0, 50))
        self.page1_Rapdjson.setObjectName("page1_Rapdjson")
        self.verticalLayout.addWidget(self.page1_Rapdjson)
        self.page1_Exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.page1_Exit.setMinimumSize(QtCore.QSize(0, 50))
        self.page1_Exit.setObjectName("page1_Exit")
        self.verticalLayout.addWidget(self.page1_Exit)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.page2_text = QtWidgets.QTextBrowser(self.tab_2)
        self.page2_text.setGeometry(QtCore.QRect(480, 12, 400, 450))
        self.page2_text.setPlaceholderText("")
        self.page2_text.setObjectName("page2_text")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 451, 451))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.page2_GetExcel = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.page2_GetExcel.setMinimumSize(QtCore.QSize(0, 50))
        self.page2_GetExcel.setObjectName("page2_GetExcel")
        self.verticalLayout_2.addWidget(self.page2_GetExcel)
        self.page2_Exit = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.page2_Exit.setMinimumSize(QtCore.QSize(0, 50))
        self.page2_Exit.setObjectName("page2_Exit")
        self.verticalLayout_2.addWidget(self.page2_Exit)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(270, 30, 321, 401))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.page3_XMLPath = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.page3_XMLPath.setMinimumSize(QtCore.QSize(0, 50))
        self.page3_XMLPath.setMaximumSize(QtCore.QSize(16777215, 50))
        self.page3_XMLPath.setObjectName("page3_XMLPath")
        self.verticalLayout_5.addWidget(self.page3_XMLPath)
        self.page3_ExcelPath = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.page3_ExcelPath.setMinimumSize(QtCore.QSize(0, 50))
        self.page3_ExcelPath.setMaximumSize(QtCore.QSize(16777215, 50))
        self.page3_ExcelPath.setObjectName("page3_ExcelPath")
        self.verticalLayout_5.addWidget(self.page3_ExcelPath)
        self.page3_XMLCreatePath = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.page3_XMLCreatePath.setMinimumSize(QtCore.QSize(0, 50))
        self.page3_XMLCreatePath.setMaximumSize(QtCore.QSize(16777215, 50))
        self.page3_XMLCreatePath.setObjectName("page3_XMLCreatePath")
        self.verticalLayout_5.addWidget(self.page3_XMLCreatePath)
        self.page3_XmlToExcel = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.page3_XmlToExcel.setMinimumSize(QtCore.QSize(0, 50))
        self.page3_XmlToExcel.setObjectName("page3_XmlToExcel")
        self.verticalLayout_5.addWidget(self.page3_XmlToExcel)
        self.page3_ExcelToXml = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.page3_ExcelToXml.setMinimumSize(QtCore.QSize(0, 50))
        self.page3_ExcelToXml.setObjectName("page3_ExcelToXml")
        self.verticalLayout_5.addWidget(self.page3_ExcelToXml)
        self.page3_Exit = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.page3_Exit.setMinimumSize(QtCore.QSize(0, 50))
        self.page3_Exit.setObjectName("page3_Exit")
        self.verticalLayout_5.addWidget(self.page3_Exit)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(270, 30, 321, 401))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.page4_ExcelPath = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.page4_ExcelPath.setMinimumSize(QtCore.QSize(0, 50))
        self.page4_ExcelPath.setSizeIncrement(QtCore.QSize(0, 50))
        self.page4_ExcelPath.setText("")
        self.page4_ExcelPath.setObjectName("page4_ExcelPath")
        self.verticalLayout_6.addWidget(self.page4_ExcelPath)
        self.page4_CreatePath = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.page4_CreatePath.setMinimumSize(QtCore.QSize(0, 50))
        self.page4_CreatePath.setSizeIncrement(QtCore.QSize(0, 50))
        self.page4_CreatePath.setText("")
        self.page4_CreatePath.setObjectName("page4_CreatePath")
        self.verticalLayout_6.addWidget(self.page4_CreatePath)
        self.Page4_Create = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.Page4_Create.setMinimumSize(QtCore.QSize(0, 50))
        self.Page4_Create.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Page4_Create.setSizeIncrement(QtCore.QSize(0, 0))
        self.Page4_Create.setObjectName("Page4_Create")
        self.verticalLayout_6.addWidget(self.Page4_Create)
        self.Page4_Exit = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.Page4_Exit.setMinimumSize(QtCore.QSize(0, 50))
        self.Page4_Exit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Page4_Exit.setObjectName("Page4_Exit")
        self.verticalLayout_6.addWidget(self.Page4_Exit)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(270, 30, 321, 401))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.page5_XMLPath = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.page5_XMLPath.setMinimumSize(QtCore.QSize(0, 50))
        self.page5_XMLPath.setSizeIncrement(QtCore.QSize(0, 50))
        self.page5_XMLPath.setText("")
        self.page5_XMLPath.setObjectName("page5_XMLPath")
        self.verticalLayout_7.addWidget(self.page5_XMLPath)
        self.page5_ExcelPath = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.page5_ExcelPath.setMinimumSize(QtCore.QSize(0, 50))
        self.page5_ExcelPath.setSizeIncrement(QtCore.QSize(0, 50))
        self.page5_ExcelPath.setText("")
        self.page5_ExcelPath.setObjectName("page5_ExcelPath")
        self.verticalLayout_7.addWidget(self.page5_ExcelPath)
        self.page5_CreateXmlPath = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.page5_CreateXmlPath.setMinimumSize(QtCore.QSize(0, 50))
        self.page5_CreateXmlPath.setSizeIncrement(QtCore.QSize(0, 50))
        self.page5_CreateXmlPath.setText("")
        self.page5_CreateXmlPath.setObjectName("page5_CreateXmlPath")
        self.verticalLayout_7.addWidget(self.page5_CreateXmlPath)
        self.page5_AnalysisXML = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.page5_AnalysisXML.setMinimumSize(QtCore.QSize(0, 50))
        self.page5_AnalysisXML.setMaximumSize(QtCore.QSize(16777215, 50))
        self.page5_AnalysisXML.setSizeIncrement(QtCore.QSize(0, 0))
        self.page5_AnalysisXML.setObjectName("page5_AnalysisXML")
        self.verticalLayout_7.addWidget(self.page5_AnalysisXML)
        self.page5_AnalysisExcel = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.page5_AnalysisExcel.setMinimumSize(QtCore.QSize(0, 50))
        self.page5_AnalysisExcel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.page5_AnalysisExcel.setSizeIncrement(QtCore.QSize(0, 0))
        self.page5_AnalysisExcel.setObjectName("page5_AnalysisExcel")
        self.verticalLayout_7.addWidget(self.page5_AnalysisExcel)
        self.page5_Exit = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.page5_Exit.setMinimumSize(QtCore.QSize(0, 50))
        self.page5_Exit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.page5_Exit.setObjectName("page5_Exit")
        self.verticalLayout_7.addWidget(self.page5_Exit)
        self.tabWidget.addTab(self.tab_5, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(860, 500, 121, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DbtTool"))
        self.page1_Init.setText(_translate("MainWindow", "初始化Excel"))
        self.page1_Analysis.setText(_translate("MainWindow", "分析Excel"))
        self.page1_Struct.setText(_translate("MainWindow", "获得结构体"))
        self.page1_Rapdjson.setText(_translate("MainWindow", "读取解析代码"))
        self.page1_Exit.setText(_translate("MainWindow", "退出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Excel转Json"))
        self.page2_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     {</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">         &quot;a&quot; : 1,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">         &quot;b&quot; : &quot;123&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     },</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     {</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">         &quot;c&quot; : 2,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">         &quot;d&quot; : &quot;356&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     } </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">]</p></body></html>"))
        self.page2_GetExcel.setText(_translate("MainWindow", "生成Excel"))
        self.page2_Exit.setText(_translate("MainWindow", "退出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Json转Excel"))
        self.page3_XMLPath.setPlaceholderText(_translate("MainWindow", "单语言XML输入路径"))
        self.page3_ExcelPath.setPlaceholderText(_translate("MainWindow", "多语言Excel输入路径"))
        self.page3_XMLCreatePath.setPlaceholderText(_translate("MainWindow", "多语言XML生成路径"))
        self.page3_XmlToExcel.setText(_translate("MainWindow", "解析单语言XML"))
        self.page3_ExcelToXml.setText(_translate("MainWindow", "解析多语言Excel"))
        self.page3_Exit.setText(_translate("MainWindow", "退出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "多语言XML"))
        self.page4_ExcelPath.setPlaceholderText(_translate("MainWindow", "多Excel文件夹输入路径"))
        self.page4_CreatePath.setPlaceholderText(_translate("MainWindow", "生成文件夹输出路径"))
        self.Page4_Create.setText(_translate("MainWindow", "开始生成"))
        self.Page4_Exit.setText(_translate("MainWindow", "退出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "多Excel转换"))
        self.page5_XMLPath.setPlaceholderText(_translate("MainWindow", "单语言XML路径"))
        self.page5_ExcelPath.setPlaceholderText(_translate("MainWindow", "多语言Excel生成路径"))
        self.page5_CreateXmlPath.setPlaceholderText(_translate("MainWindow", "多语言XML生成路径"))
        self.page5_AnalysisXML.setText(_translate("MainWindow", "解析单语言XML"))
        self.page5_AnalysisExcel.setText(_translate("MainWindow", "解析多语言Excel"))
        self.page5_Exit.setText(_translate("MainWindow", "退出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "FairyGUI多语言"))
        self.label.setText(_translate("MainWindow", "powerd by liucong"))

        self.initMemeber()

    def initMemeber(self):
        self.__AnalysisFairyGUIExcelPath = ""
        self.__AnalysisNormalLanguageExcelPath = ""

    def connectBUTTON(self):
        self.page1_Exit.clicked.connect(self.ExitProgram)
        self.page2_Exit.clicked.connect(self.ExitProgram)
        self.page3_Exit.clicked.connect(self.ExitProgram)
        self.Page4_Exit.clicked.connect(self.ExitProgram)
        self.page5_Exit.clicked.connect(self.ExitProgram)
        analysisJson.tipBox.connect(self.Tip_Box)

        self.page5_AnalysisExcel.clicked.connect(self.Page5_AnalysisExcel)
        self.page5_AnalysisXML.clicked.connect(self.Page5_AnalysisXML)

        self.page3_XmlToExcel.clicked.connect(self.Page3_AnalyasisXML_Btn)
        self.page3_ExcelToXml.clicked.connect(self.Page3_AnalysisExcel_Btn)
        pass

    def Tip_Box(self, title, text):
        QMessageBox.warning(self, title, text)
        pass

    def ExitProgram(self):
        sys.exit()
        pass

    def Page3_AnalyasisXML_Btn(self):
        xmlPath = self.page3_XMLPath.text().strip()
        excelPath = self.page3_ExcelPath.text().strip()

        if (not os.path.exists(xmlPath)) or (not os.path.exists(excelPath)):
            self.Tip_Box("警告", "输入路径的两个路径有至少一个不存在")
            return

        self.__AnalysisNormalLanguageExcelPath = analysisXML.NormalXMLToExcel(xmlPath, excelPath)
        self.page3_ExcelPath.setText(self.__AnalysisNormalLanguageExcelPath)

        pass

    def Page3_AnalysisExcel_Btn(self):
        createPath = self.page3_XMLCreatePath.text().strip()
        excelPath = self.page3_ExcelPath.text().strip()

        if self.__AnalysisNormalLanguageExcelPath == "":
            self.__AnalysisNormalLanguageExcelPath = excelPath

        if (not os.path.exists(self.__AnalysisNormalLanguageExcelPath)) or (not os.path.exists(createPath)):
            self.Tip_Box("警告", "输入路径不存在或多语言的Excel文件被删除")
            return

        analysisExcel.ExcelToNormalXML(self.__AnalysisNormalLanguageExcelPath, createPath)
        pass


    def Page5_AnalysisXML(self):
        xmlPath = self.page5_XMLPath.text().strip()
        excelPath = self.page5_ExcelPath.text().strip()

        if (not os.path.exists(xmlPath)) or (not os.path.exists(excelPath)):
            self.Tip_Box("警告", "输入路径的两个路径有至少一个不存在")
            return

        self.__AnalysisFairyGUIExcelPath = analysisXML.FairyGUIXMLToExcel(xmlPath, excelPath)
        self.page5_ExcelPath.setText(self.__AnalysisFairyGUIExcelPath)
        pass

    def Page5_AnalysisExcel(self):
        createPath = self.page5_CreateXmlPath.text().strip()
        excelPath = self.page5_ExcelPath.text().strip()

        if self.__AnalysisFairyGUIExcelPath == "":
            self.__AnalysisFairyGUIExcelPath = excelPath

        if (not os.path.exists(self.__AnalysisFairyGUIExcelPath)) or (not os.path.exists(createPath)):
            self.Tip_Box("警告", "输入路径不存在或FairyGUI的Excel文件被删除")
            return

        analysisExcel.ExcelToFairyGUIXML(self.__AnalysisFairyGUIExcelPath, createPath)
        pass

def Test_Func():
    # analysisJson.JsonToExcel(Program_Function.GetFileText("C:/Users/cong/Desktop/pyqt/DbtGame/test.txt"))
    # analysisJson.JsonToExcel("{}")
    # analysisXML.FairyGUIXMLToExcel("C:/Users/cong/Desktop/pyqt/DbtGame/test.xml")
    # analysisExcel.CreateNullExcel()
    # analysisExcel.ExcelToJson("C:/Users/cong/Desktop/pyqt/DbtGame/单一Excel转Json.xls")
    # analysisXML.NormalXMLToExcel("C:/Users/cong/Desktop/pyqt/DbtGame/NormalXML.xml")
    # analysisExcel.ExcelToFairyGUIXML(Program_Function.GetSystemWritablePath(Program_Function.SystemPath.Desktop) + "/FairyGUI多语言.xls", Program_Function.GetSystemWritablePath(Program_Function.SystemPath.Desktop) + "/")
    # Program_Function.WriteStrToFile("C:/Users/cong/Desktop/pyqt/DbtGame/newDir/f.txt", "test")
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.connectBUTTON()
    Test_Func()
    MainWindow.show()
    sys.exit(app.exec_())

