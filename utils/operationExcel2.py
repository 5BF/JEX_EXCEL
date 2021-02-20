from config.filepath import FilePath
import itertools
import xlrd
import json



class ExcelValuesitem():

	Case_id ='caseID'
	Describe ='描述'
	Url = '请求地址'
	Method = '请求方法'
	Data = '请求数据'
	Is_run = '是否运行'
	Expect = '期望'
	Rely = '依赖'
	Sql = 'SQL'
	Header='是否需要token'
	Rely_data='所需要的依赖数据'


class OperationExcel():

	def get_sheet(self):
		book=xlrd.open_workbook(FilePath('data','JEX_Excel.xls'))
		return book.sheet_by_index(0)

	@property
	def get_rows(self):
		return self.get_sheet().nrows


	@property
	def ExcelValues(self):
		'''或者表格的所有数据，并且使用键对的方式来输出'''
		datas=list()
		title=self.get_sheet().row_values(0)
		for item in range(1,self.get_rows):
			row_values=self.get_sheet().row_values(item)
			datas.append(dict(zip(title,row_values)))
		return datas



	def is_run(self):
		'''根据表格的yes和no来判断是否要执行，然后将要执行的内容返回'''
		run_list=[]
		for item in self.ExcelValues:
			isRun=item[ExcelValuesitem.Is_run]
			if isRun=='yes':
				run_list.append(item)
			else:pass
		return run_list

	def case_pre(self):
		'''返回需要提前执行的测试用例'''
		for item in self.is_run():
			case_pre =item[ExcelValuesitem.Rely]
			if case_pre !=None:
				if case_pre in item.values():
					return item
			return None

	'''调试'''
	def test(self):
		# r=requests.post(url=self.case_pre()[ExcelValuesitem.Url,])
		url = self.case_pre()[ExcelValuesitem.Url]
		data=self.case_pre()[ExcelValuesitem.Data]
		# data = jsons.readjson()[datas[ExcelValuesitem.Data]]
		print(url)
		print(data)


	# def params(self):
	# 	'''将请求的参数进行序列化（变成字典方式）'''
	# 	for item in self.is_run():
	# 		params=item[ExcelValuesitem.Data]
	# 		if len(str(params).strip())==0:pass
	# 		elif len(str(params).strip())>=0:
	# 			print(json.loads(params))





if __name__ == '__main__':
	gg=OperationExcel()
	gg.test()
	# for item in gg.ExcelValues():
	# 	print(item)