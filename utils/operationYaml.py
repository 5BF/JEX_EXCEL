import yaml

from config.filepath import FilePath


class OperationYaml():

	# def readyaml(self):
	# 	with open(FilePath('data','JEX_Request.yaml'),'r') as f:
	# 		return list(yaml.safe_load_all(f))

	def readyaml(self):
		with open(FilePath('data','JEX_requests'),'r',encoding='utf-8') as  f:
			return yaml.safe_load(f)

if __name__ == '__main__':
	p=OperationYaml()
	print(p.readyaml())
	# for item in p.readyaml():
	# 	print(item)