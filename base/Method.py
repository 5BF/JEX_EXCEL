import os
import sys
import requests
from utils.operationExcel2 import OperationExcel,ExcelValuesitem
from utils.operationJson import OperationJson
head=ExcelValuesitem()

jsondata=OperationJson()
class Requests():

	def request(self,url,method='get',**kwargs):
		if method=='get':
			return requests.get(url,method=method,**kwargs)
		elif method=='post':
			return requests.post(url,method=method,**kwargs)

	def get(self,header,url,**kwargs):
		isheader=head.Header
		if isheader=='yes':
			return requests.request(url=url, method='get',headers=header, **kwargs)
		else:
			return requests.request(url=url, method='get', **kwargs)

	def post(self,url,header=None,**kwargs):
		isheader = head.Header
		if isheader == 'yes':
			return requests.request(url=url, method='post', headers=header, **kwargs)
		else:
			return requests.request(url=url, method='post', **kwargs)


	'''测试'''
	def test(self):
		param=jsondata.readjson()["test_009"]
		r=requests.get(url='http://test.coinfex.com/api/v2/pub/kline',params=param)
		print(r.json())
		print(r.url)
		print(r.status_code)
		print(param)


if __name__ == '__main__':
	ooo=Requests()
	ooo.test()
