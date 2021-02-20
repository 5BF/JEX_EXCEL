from base.Method import Requests
from utils.operationExcel2 import OperationExcel,ExcelValuesitem
from utils.operationJson import OperationJson
import pytest
from base.hearder import Get_hearder
import json
import allure


obj=Requests()
excel=OperationExcel()
jsons=OperationJson()
#获取token
head=Get_hearder()
head.get_hearder()
token={"headerToken":head.readToken()}
base_url='https://www.jexzhs.com'

'''按照列表的形式读取可执行的用例'''
@pytest.mark.parametrize('datas',excel.is_run())
def test_kline(datas):
	'''获取请求数据'''
	data = jsons.readjson()[datas[ExcelValuesitem.Data]]
	# if len(data)==0:
	# 	pass
	# else:
	# 	return data

	'''执行前置用例，并替换json里面相对应的请求数据'''
	case_pre = datas[ExcelValuesitem.Rely]
	if len(case_pre) ==0:
		pass
	else:
		r = obj.get(url=base_url+excel.case_pre()[ExcelValuesitem.Url], params=data, header=token)
		case_rely=datas[ExcelValuesitem.Rely_data]
		if case_rely in data:
			data=str(data).replace(str(case_rely),str(r.json()[case_rely]))
		else:
			pass

	if datas[ExcelValuesitem.Method]=='get':
		r=obj.get(url=base_url+datas[ExcelValuesitem.Url],params=data,header=token)
		'''判断excel的值是否包含在响应数据里面'''
		assertmsg = datas[ExcelValuesitem.Expect]
		assert_rssult=json.dumps(r.json(),ensure_ascii=False)
		assert assertmsg in assert_rssult
		print(r.json()["err_msg"])

	elif datas[ExcelValuesitem.Method]=='post':
		r = obj.post(url=base_url+datas[ExcelValuesitem.Url],header=token,data=data)
		assertmsg = datas[ExcelValuesitem.Expect]
		assert_rssult = json.dumps(r.json(), ensure_ascii=False)
		assert assertmsg in assert_rssult
		print(r.json()["err_msg"])


	# if datas[ExcelValuesitem.Method]=='get':
	#
	# 	if datas[ExcelValuesitem.Header]=='yes':
	# 		r = obj.get(url=datas[ExcelValuesitem.Url], headers=token)
	# 		assertmsg = datas[ExcelValuesitem.Expect]
	# 		assert assertmsg in json.dumps(r.json(),ensure_ascii=False)
	# 	else:
	# 		r = obj.get(url=datas[ExcelValuesitem.Url])
	# 		assertmsg = datas[ExcelValuesitem.Expect]
	# 		assert assertmsg in json.dumps(r.json(),ensure_ascii=False)
	#
	# elif datas[ExcelValuesitem.Method]=='post':
	# 	if datas[ExcelValuesitem.Header]=='yes':
	# 		r = obj.post(url=datas[ExcelValuesitem.Url], headers=token)
	# 		assertmsg = datas[ExcelValuesitem.Expect]
	# 		assert assertmsg in r.json()
	# 	else:
	# 		r= obj.post(url=datas[ExcelValuesitem.Url])
	# 		assertmsg = datas[ExcelValuesitem.Expect]
	# 		assert assertmsg in r.json()

if __name__ == '__main__':
	pytest.main(["-v","-s","test_jex.py","--alluredir=./report/result"])
	import subprocess
	#allure generate D:/PyTest/tests/allure/report/xml -o D:/PyTest/tests/allure/report/html --clean
	subprocess.call('allure generate ./report/result -o ./result/html --clean',shell=True)
	subprocess.call('allure open -h 127.0.0.1 -p 8088 ./result/html',shell=True)
