import sys
import os
import xlwt
import xlrd
from enum import Enum

from  PyQt5.QtWidgets import *
from PyQt5.QtCore import QStandardPaths

class SystemPath(Enum):
    Desktop = 1,
    Document = 2,
    Music = 3,
    Movie = 4,
    Picture = 5,
    HomeLocation = 6,
    CacheLocation = 7,
    Download = 8
    pass

class DataType(Enum):
    INT = "int",
    DOUBLE = "double",
    STRING = "string",
    TUPLE = "tuple:",
    BOOL = "bool",
    LISTINT = "int[]",
    LISTDOUBLE = "double[]",
    LISTSTRING = "string[]",
    LISTTUPLE = "tuple[]:",
    LISTBOOL = "bool[]"
    pass

DataTypeList = [DataType.INT, DataType.DOUBLE, DataType.STRING, DataType.TUPLE, DataType.BOOL, DataType.LISTINT, DataType.LISTDOUBLE, DataType.LISTSTRING, DataType.LISTTUPLE, DataType.LISTBOOL]

def StrToDataType(typestr):
    if "int" == typestr:
        return DataType.INT
    elif "double" == typestr:
        return DataType.DOUBLE
    elif "string" == typestr:
        return DataType.STRING
    elif str(typestr).startswith("tuple[]:"):
        return DataType.LISTTUPLE
    elif "bool" == typestr:
        return DataType.BOOL
    elif "int[]" == typestr:
        return DataType.LISTINT
    elif "double[]" == typestr:
        return DataType.LISTDOUBLE
    elif "string[]" == typestr:
        return DataType.LISTSTRING
    elif str(typestr).startswith("tuple"):
        return DataType.TUPLE
    elif "bool[]" == typestr:
        return DataType.LISTBOOL
    pass

def GetSystemWritablePath(pathEnum):
    if pathEnum == SystemPath.Desktop:
        return QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
    elif pathEnum == SystemPath.Document:
        return QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
    elif pathEnum == SystemPath.Music:
        return QStandardPaths.writableLocation(QStandardPaths.MusicLocation)
    elif pathEnum == SystemPath.Movie:
        return QStandardPaths.writableLocation(QStandardPaths.MoviesLocation)
    elif pathEnum == SystemPath.Picture:
        return QStandardPaths.writableLocation(QStandardPaths.PicturesLocation)
    elif pathEnum == SystemPath.HomeLocation:
        return QStandardPaths.writableLocation(QStandardPaths.HomeLocation)
    elif pathEnum == SystemPath.CacheLocation:
        return QStandardPaths.writableLocation(QStandardPaths.CacheLocation)
    elif pathEnum == SystemPath.Download:
        return QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
    pass

def GetFileText(filePath):
    result = ""
    with open(filePath, "r") as file:
        result = file.read()
        pass
    return result
    pass

def CreateFileNotSame(filePath):
    BaseString = filePath
    fileIndex = 1
    while os.path.exists(filePath):
        filePath = os.path.splitext(BaseString)[0] + "(" + str(fileIndex) + ")" + os.path.splitext(BaseString)[1]
        fileIndex += 1
        pass
    return filePath
    pass

def CreateDir(filePath):
    if not os.path.exists(filePath):
        os.mkdir(filePath)
    pass

def WriteStrToFile(filePath, data):
    dirPath = os.path.dirname(filePath)     # 获得文件所在文件夹路径
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    with open(filePath, "w", encoding="utf-8") as file:
        file.write(data)
    pass


def TypeToJsonStr(key, type, val):
    oldVal = type
    type = StrToDataType(type)
    if not type in DataTypeList:
        print("error : tuple中数据类型不存在【2】", type)
        return "\"" + key + "\" : []"

    if type == DataType.LISTBOOL or type == DataType.LISTINT or type == DataType.LISTDOUBLE or type == DataType.LISTSTRING:
        return ListToJsonStr(key, type, val)

    result = "\"" + key + "\" : "

    if type == (DataType.INT):
        result += str(int(float(val)))
    elif type == (DataType.BOOL):
        result += str(bool(int(float(val)))).lower()
    elif type == (DataType.DOUBLE):
        result += str(float(val))
    elif type == (DataType.STRING):
        result += "\"" + str(val) + "\""
    elif type == (DataType.TUPLE):
        return TupleToJsonStr(key, oldVal, val)
    return result
    pass

def ListToJsonStr(key, type, val):
    result = "\"" + key + "\" : ["

    valSplit = str(val).split(',')

    for _valNode in valSplit:
        if type == (DataType.LISTINT):
            result += str(int(float(_valNode))) + ","
        elif type == (DataType.LISTBOOL):
            result += str(bool(int(float(_valNode)))).lower() + ","
        elif type == (DataType.LISTDOUBLE):
            result += str(float(_valNode)) + ","
        elif type == (DataType.LISTSTRING):
            result += "\"" + _valNode + "\","
    if result[-1] == ',':
        result = result[:-1]
    result += "]"
    return result
    pass

# type = tuple:int,double,string,bool
# val  = 1,1.1,int,true
def TupleToJsonStr(key, type, val):
    typelist = str(type).split(":")
    if len(typelist) != 2:
        print("error : tuple填写错误 【1】" + type)
        return "\"" + key + "\" : []"

    typelist = typelist[1]                  # int,double,string,bool
    typelist = typelist.split(",")          # int double string bool

    for typeVal in typelist:
        enumType = StrToDataType(typeVal)
        if not enumType in DataTypeList:
            print("error : tuple中数据类型不存在【2】", type)
            return "\"" + key + "\" : []"

    valuelist = str(val).split(",")         # 1   1.1    int    true

    if len(valuelist) != len(typelist):
        print("error : tuple数据类型数目与值的数目不同 【3】" + val)
        return "\"" + key + "\" : []"

    result = "\"" + key + "\" : ["

    for dataIndex in range(len(valuelist)):
        enumType = StrToDataType(typelist[dataIndex])
        if enumType == (DataType.BOOL):
            result += str(bool(int(float(valuelist[dataIndex])))).lower() + ","
        elif enumType == (DataType.STRING):
            result += "\"" + str(valuelist[dataIndex]) + "\","
        elif enumType == (DataType.INT):
            result += str(int(float(valuelist[dataIndex]))) + ","
        elif enumType == (DataType.DOUBLE):
            result += str(float(valuelist[dataIndex])) + ","
        pass

    if result.endswith(","):
        result = result[:-1]
    result += "]"
    return result
    pass

def StrToStruct(notelist, typelist, namelist, typename):

    result = "struct " + typename + " {\n"

    for index in range(len(notelist)):
        result += "\t" + GetCPPType(typelist[index]) + " " + namelist[index] + ";//" + notelist[index] + "\n"
        pass

    result += "};"
    return result
    pass

def GetCPPType(typeStr):
    enumType = StrToDataType(typeStr)

    if DataType.INT == enumType:
        return "int"
    elif DataType.DOUBLE == enumType:
        return "double"
    elif DataType.STRING == enumType:
        return "std::string"
    elif str(typeStr).startswith("tuple[]:"):   # tuple[]:int,double,string
        splittuple = str(typeStr).split(":")
        return "std::vector<std::tuple<" + splittuple[1] + ">>"
    elif str(typeStr).startswith("tuple:"):     # tuple:int,double,string
        splittuple = str(typeStr).split(":")
        return "std::tuple<" + splittuple[1] + ">"
    elif DataType.BOOL == enumType:
        return "bool"
    elif DataType.LISTINT == enumType:
        return "std::vector<int>"
    elif DataType.LISTDOUBLE == enumType:
        return "std::vector<double>"
    elif DataType.LISTSTRING == enumType:
        return "std::vector<std::string>"
    elif DataType.LISTBOOL == enumType:
        return "std::vector<bool>"
    print("error : 不存在的数据类型 【4】")
    return "auto"
    pass

def GetRaidjsonReadCode(namelist, typelist, typename):
    result = "	rapidjson::Document m_doc;// 配置相关的json\n\
	if (!FileUtils::getInstance()->isFileExist(\"" + typename + ".json\"))\n\
	{\n\
		CCASSERT(0, \"文件不存在\");\n\
	}\n\
	std::string data = FileUtils::getInstance()->getStringFromFile(\"" + typename + ".json\");\n\
	m_doc.Parse<0>(data.c_str());\n\
	if (m_doc.HasParseError())\n\
	{\n\
		CCLOG(\"GetParseError %d \", m_doc.GetParseError());\n\
		CCASSERT(0, \"文件有问题\");\n\
	}\n\
	if (!m_doc.IsObject())\n\
	{\n\
		CCASSERT(0, \"文件有问题\");\n\
	}\n\
	std::vector<" + typename + "> m_" + typename + ";\n\
	rapidjson::Value& _jsonInfo = m_doc[\"key\"];\n\
\n\
    if (_jsonInfo.IsArray())\n\
    {\n\
        for (int i = 0; i < _jsonInfo.Size(); i++)\n\
        {\n"

    result += "\t\t\t" + typename + " temp;\n"

    for index in range(len(namelist)):
        result += "\t\t\t" + GetRapidjsonGetValue(typelist[index], namelist[index]) + "\n"
        pass

    result += "			m_" + typename + ".push_back(temp);\n\
		}\n\
	}"

    return result
    pass

def GetRapidjsonGetValue(typeStr, name):
    enumType = StrToDataType(typeStr)
    if DataType.INT == enumType:
        return "temp." + name + " = _jsonInfo[i][\"" + name + "\"].GetInt();"
    elif DataType.DOUBLE == enumType:
        return "temp." + name + " = _jsonInfo[i][\"" + name + "\"].GetDouble();"
    elif DataType.STRING == enumType:
        return "temp." + name + " = _jsonInfo[i][\"" + name + "\"].GetString();"
    elif DataType.BOOL == enumType:
        return "temp." + name + " = _jsonInfo[i][\"" + name + "\"].GetBool();"
    elif DataType.LISTINT == enumType:
        return "temp." + name + " = GetValueToIntVec(_jsonInfo[i][\"" + name + "\"]);"
    elif DataType.LISTDOUBLE == enumType:
        return "temp." + name + " = GetValueToDoubleVec(_jsonInfo[i][\"" + name + "\"]);"
    elif DataType.LISTSTRING == enumType:
        return "temp." + name + " = GetValueToStringVec(_jsonInfo[i][\"" + name + "\"]);"
    elif DataType.LISTBOOL == enumType:
        return "temp." + name + " = GetValueToBoolVec(_jsonInfo[i][\"" + name + "\"]);"
    elif str(typeStr).startswith("tuple"):
        result = "temp." + name + " = std::make_tuple("
        splittuple = str(typeStr).split(":")[1].split(",")
        for valTypeIndex in range(len(splittuple)):
            valType = StrToDataType(splittuple[valTypeIndex])
            if DataType.INT == valType:
                result += "_jsonInfo[i][\"" + name + "\"][" + str(valTypeIndex) + "].GetInt(),"
            elif DataType.DOUBLE == valType:
                result += "_jsonInfo[i][\"" + name + "\"][" + str(valTypeIndex) + "].GetDouble(),"
            elif DataType.STRING == valType:
                result += "_jsonInfo[i][\"" + name + "\"][" + str(valTypeIndex) + "].GetString(),"
            elif DataType.BOOL == valType:
                result += "_jsonInfo[i][\"" + name + "\"][" + str(valTypeIndex) + "].GetBool(),"
            pass
        if result.endswith(","):
            result = result[:-1]
        result += ");"
        return result
        pass
    print("error : 不存在的数据类型 【4】")
    return "auto"
    pass

def GetDirFiles(file_dir, targetFileType = ""):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == targetFileType:
                L.append(os.path.join(root, file))
    return L
    pass

def Create_H_File(confList):
    h_file = "#pragma once\n\
#include <iostream>\n\
#include <vector>\n\
#include <tuple>\n\
using namespace std;\n"

    for _item in confList:
        h_file += _item["StructStr"] + "\n"

    h_file += """class GameData
    {
    public:
    	static GameData& getInstance()
    	{
    		static GameData instance;
    		return instance;
    	}
        GameData(){
            initmember();
        }
    private:
        void initmember();
    """

    for _item in confList:
        h_file += "\tvoid init" + _item["StructName"] + "();\n"

    for _item in confList:
        h_file += "\tstd::vector<" + _item["StructName"] + "> m_" + _item["StructName"] + ";\n"

    h_file += "};"
    return h_file
    pass


def Create_CPP_File(confList):
    cpp_file = """#include "GameDataConf.h"
#include "json/prettywriter.h"
#include "json/rapidjson.h"
#include "json/document.h"
#include "json/stringbuffer.h"
#include "json/writer.h"
#include "json/memorystream.h"
#include "cocos2d.h"

USING_NS_CC;

static std::vector<int> GetValueToIntVec(const rapidjson::Value& _val)
{
	std::vector<int> result;
	if (!_val.IsArray())
	{
		CCASSERT(0, "存在错误");
		return result;
	}

	for (int i = 0; i < _val.Size(); i++)
	{
		result.push_back(_val[i].GetInt());
	}
	return result;
}
static std::vector<double> GetValueToDoubleVec(const rapidjson::Value& _val)
{
  std::vector<double> result;
  if (!_val.IsArray())
  {
            CCASSERT(0, "存在错误");
            return result;
  }

  for (int i = 0; i < _val.Size(); i++)
  {
            result.push_back(_val[i].GetDouble());
  }
   return result;
}
static std::vector<bool> GetValueToBoolVec(const rapidjson::Value& _val)
{
   std::vector<bool> result;
   if (!_val.IsArray())
   {
        CCASSERT(0, "存在错误");
        return result;
   }

   for (int i = 0; i < _val.Size(); i++)
   {
        result.push_back(_val[i].GetBool());
   }
   return result;
}
static std::vector<std::string> GetValueToStringVec(const rapidjson::Value& _val)
{
   std::vector<std::string> result;
   if (!_val.IsArray())
   {
        CCASSERT(0, "存在错误");
        return result;
   }

   for (int i = 0; i < _val.Size(); i++)
   {
        result.push_back(_val[i].GetString());
   }
   return result;

}\n"""

    for _item in confList:
        cpp_file += "void GameData::init" + _item["StructName"] + "(){\n"
        cpp_file += _item["RapidJson"]
        cpp_file += "}\n"
        pass

    cpp_file += "void GameData::initmember(){\n"
    for _item in confList:
        cpp_file += "\tinit" + _item["StructName"] + "();\n"
        pass
    cpp_file += "}\n"
    return cpp_file
    pass