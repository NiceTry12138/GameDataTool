import xlwt
import xlrd
import xml
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET

from PyQt5.QtCore import QStandardPaths
import Program_Function

class AnalysisXML:

    def NormalXMLToExcel(self, xmlPath, createPath):
        language_key = "public_sys_language"
        root_elementName = "userContent"
        rowIndex= 1
        workbook = xlwt.Workbook(encoding="utf-8")
        worksheet = workbook.add_sheet("游戏多语言")


        DomTree = ET.parse(xmlPath).getroot()
        Children_node = DomTree.getchildren()
        for _child in Children_node:
            # print(_child.tag + " " + _child.text)
            worksheet.write(rowIndex, 0, _child.tag)
            worksheet.write(rowIndex, 1, _child.text)
            rowIndex += 1
        worksheet.write(0, 0, "tag")
        worksheet.write(0, 1, "zh")

        fileWritePath = createPath + "/普通的多语言.xls"
        finalWritePath = Program_Function.CreateFileNotSame(fileWritePath)
        workbook.save(finalWritePath)
        return finalWritePath

        pass

    def FairyGUIXMLToExcel(self, xmlPath, createPath):
        xmlAttr = ["name", "mz"]
        xmlRootKey = "resources"
        xmlElementKey = "string"
        DomTree = xml.dom.minidom.parse(xmlPath)
        elements = DomTree.documentElement.getElementsByTagName(xmlElementKey)

        rowIndex= 1
        workbook = xlwt.Workbook(encoding="utf-8")
        worksheet = workbook.add_sheet("FairyGUI多语言")

        worksheet.write(0, 0, "name")
        worksheet.write(0, 1, "mz")
        worksheet.write(0, 2, "zh")

        for _element in elements:
            if _element.hasAttribute(xmlAttr[0]) and _element.hasAttribute(xmlAttr[1]):
                worksheet.write(rowIndex, 0, _element.getAttribute(xmlAttr[0]))
                worksheet.write(rowIndex, 1, _element.getAttribute(xmlAttr[1]))
                worksheet.write(rowIndex, 2, _element.childNodes[0].data)
                rowIndex += 1
                pass
            pass
        pass
        fileWritePath = createPath + "/FairyGUI多语言.xls"
        finalWritePath = Program_Function.CreateFileNotSame(fileWritePath)
        workbook.save(finalWritePath)
        return finalWritePath

analysisXML = AnalysisXML()