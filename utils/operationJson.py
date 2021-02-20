from config.filepath import FilePath
import json

class OperationJson():
	def readjson(self):
		with open(FilePath('data','JEX_request.json'),'r')as f:
			return json.loads(f.read())


if __name__ == '__main__':
	G=OperationJson()
	print(G.readjson()['test_002'])