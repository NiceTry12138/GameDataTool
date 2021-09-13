import xlwt
import xlrd
import json
import xlsxwriter

from PyQt5.QtCore import QStandardPaths, QObject
import Program_Function
import os

class AnalysisExcel(QObject):
    def __init__(self):
        self.__CreateExcelpath = ""

    def CreateNullExcel(self):
        workbook = xlwt.Workbook(encoding="utf-8")
        worksheet = workbook.add_sheet("单一Excel转Json")
        worksheet.write(0,0,"注释")
        worksheet.write(1,0,"保留字段")
        worksheet.write(2,0,"数据类型")
        worksheet.write(3,0,"变量名/键名")
        worksheet.write(4,0,"后面是指值")
        fileWritePath = Program_Function.GetSystemWritablePath(Program_Function.SystemPath.Desktop) + "/单一Excel转Json.xls"
        finalPath = Program_Function.CreateFileNotSame(fileWritePath)
        workbook.save(finalPath)
        __CreateExcelpath = finalPath
        os.system("start " + finalPath)
        return finalPath

        # fileWritePath = Program_Function.GetSystemWritablePath(Program_Function.SystemPath.Desktop) + "/单一Excel转Json.xls"
        # finalPath = Program_Function.CreateFileNotSame(fileWritePath)
        # workbook = xlsxwriter.Workbook(finalPath)
        # worksheet = workbook.add_worksheet()
        # worksheet.write("A1", "注释")
        # worksheet.write("A2", "保留字段")
        # worksheet.write("A3", "数据类型")
        # worksheet.write("A4", "变量名/键名")
        # worksheet.write("A5", "后面是指值")
        # for x in range(ord('B'), ord('Z') + 1):
        #     worksheet.data_validation(str(x) + "3", {
        #         'validate': 'list',
        #         'source': ['open', 'high', 'close']
        #     })
        pass

    def OneExcelToJson(self, excelPath):
        return self.__ExcelToJson(excelPath, "toolStruct")
        pass

    def TargetExcelToJson(self, excelPath, structname):
        return self.__ExcelToJson(excelPath, structname)
        pass

    def ExcelToJson(self, excelPath):
        _nodeList = []
        _typeList = []
        _nameList = []

        workbook = xlrd.open_workbook(excelPath)
        worksheet = workbook.sheet_by_index(0)

        rowNum = worksheet.nrows
        colNum = worksheet.ncols

        # 表示没有数据 只有 注释、保留、类型、变量名
        if rowNum <= 4:
            return "{}"

        allNotes = self.__GetOneRowData(worksheet, 0, range(colNum))
        valuableCol = []
        colIndex = 0
        for _oneNote in allNotes:
            if not str.startswith(_oneNote, "mark_") and colIndex != 0:
                valuableCol.append(colIndex)
                pass
            colIndex += 1

        _nodeList = self.__GetOneRowData(worksheet, 0, valuableCol)
        _typeList = self.__GetOneRowData(worksheet, 2, valuableCol)
        _nameList = self.__GetOneRowData(worksheet, 3, valuableCol)
        rowIndex = 4
        data = {"key" : []}
        for rowIndex in range(rowNum):
            if rowIndex < 4:
                continue
            itemList = {}
            rowData = self.__GetOneRowData(worksheet, rowIndex, valuableCol)
            for _dataIndex in range(len(rowData)):
                itemList[str(_nameList[_dataIndex])] = rowData[_dataIndex]
                pass
            data["key"].append(itemList)

        jsonStr = json.dumps(data)
        print(jsonStr)
        pass

    def ExcelToNormalXML(self, excelPath, baseCreatePath):

        _taglist = []

        workbook = xlrd.open_workbook(excelPath)
        worksheet = workbook.sheet_by_index(0)

        rowNum = worksheet.nrows
        colNum = worksheet.ncols

        _taglist = self.__GetOneColData(worksheet, 0, range(rowNum))

        for _colIndex in range(colNum):
            if _colIndex == 0:
                continue
            colValues = self.__GetOneColData(worksheet, _colIndex, range(rowNum))
            if len(colValues) <= 0 or colValues[0].strip() == "":
                continue
            language_tag = colValues[0]
            # <string name="n8elmjc56k9j4c-n7_6k9j" mz="n7">Loading</string>
            fileStr = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<userContent>"
            for _rowIndex in range(len(colValues)):
                if _rowIndex == 0:
                    continue
                fileStr += "\n\t<" + _taglist[_rowIndex] + ">" + colValues[_rowIndex] + "</" + _taglist[_rowIndex] + ">"
            fileStr += "\n</userContent>"
            # print(fileStr)
            Program_Function.WriteStrToFile(baseCreatePath + "/" + language_tag + "/language_config.xml", fileStr)
            pass

        pass

    # 列依次是 name mz 语言缩写等
    def ExcelToFairyGUIXML(self, excelPath, baseCreatePath):

        _nameList = []
        _mzList = []

        workbook = xlrd.open_workbook(excelPath)
        worksheet = workbook.sheet_by_index(0)

        rowNum = worksheet.nrows
        colNum = worksheet.ncols

        namelist = self.__GetOneColData(worksheet, 0, range(rowNum))
        mzlist = self.__GetOneColData(worksheet, 1, range(rowNum))

        for _colIndex in range(colNum):
            if _colIndex in [0, 1]:
                continue
            colValues = self.__GetOneColData(worksheet, _colIndex, range(rowNum))
            if len(colValues) <= 0 or colValues[0].strip() == "":
                continue
            language_tag = colValues[0]
            # <string name="n8elmjc56k9j4c-n7_6k9j" mz="n7">Loading</string>
            fileStr = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>"
            for _rowIndex in range(len(colValues)):
                if _rowIndex == 0:
                    continue
                fileStr += "\n\t<string> name=\"" + namelist[_rowIndex] + "\" mz=\"" + mzlist[_rowIndex] + "\">" + colValues[_rowIndex] + "</string>"
            fileStr += "\n</resources>"
            # print(fileStr)
            Program_Function.WriteStrToFile(baseCreatePath + "/" + language_tag + "/language_config.xml", fileStr)
            pass

        pass

    # 获得这个sheet中第row行的，指定col列的所有元素，这里的 colNum为一个数组 表示读取数据的列序号
    def __GetOneRowData(self, worksheet, rowIndex, colNum):
        result = []
        for _index in colNum:
            result.append(worksheet.cell_value(rowIndex, _index))
        return  result
        pass

    # 获得这个sheet第col列的，指定row行的所有元素，这里的rowNum为一个数组 表示读取数据的行序号
    def __GetOneColData(self, worksheet, colIndex, rowNum):
        result = []
        for _index in rowNum:
            result.append(worksheet.cell_value(_index, colIndex))
        return result
        pass

    # 返回顺序 结构体字符串 json字符串
    def __ExcelToJson(self, filePath, typename):

        _nameList = []
        _mzList = []

        workbook = xlrd.open_workbook(filePath)
        worksheet = workbook.sheet_by_index(0)

        rowNum = worksheet.nrows
        colNum = worksheet.ncols

        if rowNum < 4:
            return "{}"

        noteAllList = self.__GetOneRowData(worksheet, 0, range(colNum))    # 注释行
        valablelist = []
        colIndex = 0
        for noteval in noteAllList:
            val = str(noteval).strip()
            if str(val) != "" or (not str(val).startswith("mark")):
                valablelist.append(colIndex)
            colIndex += 1
            pass
        del (valablelist[0])                                                # 删除第一个提示列

        # 注释1	注释2	注释3	注释4	注释5	注释6	注释7	注释8
        # C	C	C	C	C	C	C	C
        # int[]	bool[]	string[]	double[]	int	bool	string	double
        # name1	name2	name3	name4	name5	name6	name7	name7

        notelist        = self.__GetOneRowData(worksheet, 0, valablelist)
        placeholderlist = self.__GetOneRowData(worksheet, 1, valablelist)
        datatypelist    = self.__GetOneRowData(worksheet, 2, valablelist)
        datanamelist    = self.__GetOneRowData(worksheet, 3, valablelist)

        if len(notelist) != len(datatypelist) or len(notelist) != len(datanamelist):
            print("error : 注释、数据类型、数据名称的数目不同【4】")
            return  "{}"

        structStr = Program_Function.StrToStruct(notelist, datatypelist, datanamelist, typename)
        rapidjsonReadStr = Program_Function.GetRaidjsonReadCode(datanamelist, datatypelist, typename)

        result = "{\"key\" : [ \n"
        for rowIndex in range(rowNum):
            if rowIndex in [0, 1, 2, 3]:
                continue
            datalist = self.__GetOneRowData(worksheet, rowIndex, valablelist)

            isNullRow = True
            for val in datalist:
                if str(val).strip() != "":
                    isNullRow = False
            if isNullRow:
                break

            result += "{\n"

            for columDataIndex in range(len(datalist)):
                result += "\t" + Program_Function.TypeToJsonStr(datanamelist[columDataIndex], datatypelist[columDataIndex], datalist[columDataIndex]) + ",\n"
                pass

            if result.endswith(",\n"):
                result = result[:-2]

            result += "\n},"
            pass
        if result.endswith(","):
            result = result[:-1]
        result += "\n]}"
        return  structStr, result, rapidjsonReadStr
        pass

analysisExcel = AnalysisExcel()