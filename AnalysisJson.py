import xlwt
import xlrd
import json

from PyQt5.QtCore import pyqtSignal, QObject
import Program_Function

class AnalysisJson(QObject):

    tipBox = pyqtSignal(str, str)

    def RegisterObjSignal(self, Obj):
        Obj.tipBox.RegisterSignal(self)
        pass

    def JsonToExcel(self, jsonStr):
        json_list = json.loads(jsonStr)
        if type(json_list).__name__ != 'list' or len(json_list) == 0:
            self.tipBox.emit("警告", "Json不是数组或者Json数组length为0")
            return
        rowIndex= 1
        workbook = xlwt.Workbook(encoding="utf-8")
        worksheet = workbook.add_sheet("Json转Excel")
        for _item in json_list:
            colIndex = 0
            for k,v in _item.items():
                worksheet.write(rowIndex, colIndex, label = v)
                if rowIndex == 1:
                    worksheet.write(0, colIndex, label = k)
                colIndex += 1
                pass
            rowIndex += 1
            pass
        fileWritePath = Program_Function.GetSystemWritablePath(Program_Function.SystemPath.Desktop) + "/Json转Excel.xls"
        workbook.save(Program_Function.CreateFileNotSame(fileWritePath))
        pass

analysisJson = AnalysisJson()