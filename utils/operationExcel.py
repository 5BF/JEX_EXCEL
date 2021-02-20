import xlrd
from config.filepath import FilePath
from utils.operationYaml import OperationYaml
from utils.operationJson import OperationJson
import json
import itertools


class ExcelValues():
	Case_id = 0
	Describe = 1
	Url = 2
	Method = 3
	Data = 4
	Is_run = 5
	Expect = 6
	Rely = 7
	Sql = 8

	def caseid(self):
		return self.Case_id

	def describe(self):
		return self.Describe

	def url(self):
		return self.Url

	def method(self):
		return self.Method

	def data(self):
		return self.Data

	def isrun(self):
		return self.Is_run

	def expect(self):
		return self.Expect

	def rely(self):
		return self.Rely

	def sql(self):
		return self.Sql

class OperationExcel(OperationJson):


	def get_sheet(self):
		data=xlrd.open_workbook(FilePath('data','JEX_Excel.xls'))
		return data.sheet_by_index(0)

	@property
	def get_nows(self):
		return self.get_sheet().nrows

	@property
	def get_cols(self):
		return self.get_sheet().ncols

	def get_values(self,row,col):
		'''获取表的值'''
		return self.get_sheet().cell_value(row,col)

	def get_caseid(self,row):
		''''''
		return self.get_values(row,col=ExcelValues.Case_id)

	def get_describe(self,row):
		return self.get_values(row,col=ExcelValues.Describe)

	def get_url(self,row):
		return self.get_values(row,col=ExcelValues.Url)

	def get_method(self,row):
		return self.get_values(row,col=ExcelValues.Method)

	def get_data(self,row):
		coll=self.get_values(row,col=ExcelValues.Data)
		return self.readjson()[coll]
		# return self.get_values(row,col=ExcelValues.Data)

	def get_isrun(self,row):
		return self.get_values(row,col=ExcelValues.Is_run)

	def get_expect(self,row):
		return self.get_values(row,col=ExcelValues.Expect)

	def get_rely(self,row):
		return self.get_values(row,col=ExcelValues.Rely)

	def get_sql(self,row):
		return self.get_values(row,col=ExcelValues.Sql)

	def get_allData(self,item):
		ExcelData=[]
		return (self.get_sheet().row_values(item))
		# for item in self.get_sheet():
		# 	return type(self.get_sheet().row_values(item))


	# def getdatatest(self):
	# 	datas=list()
	# 	title=self.get_sheet().row_values(0)
	# 	for row in range(1,self.get_nows):
	# 		row_values=self.get_sheet().row_values(row)
	# 		datas.append(dict(zip(title,row_values)))
	# 	return datas


	def is_run(self):
		pass




if __name__ == '__main__':
	oo=OperationExcel()
	Excelrows =oo.get_nows
	for item in range(1, Excelrows):
		print(oo.get_allData(item))

	# for item in oo.getdatatest():
	# 	print(item)