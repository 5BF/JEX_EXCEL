from base.Method import Requests
obj=Requests()
from config.filepath import FilePath


password="Kr3pRcJAQqyGhx%2B0fEmS5uLWNimy3LS5tHfNhXO9cEmn%2BNZe%2FR3IJMAyPadfrYImkPjcTEs%2Bw924wrkhz2b4%2BNxtlqsFFMZlwvQ9EGcOqa%2BO8fgQ98x3WLSrmcRTFEe2PAKAxIGHqYrI6jwzksMu2N3vcgp2%2FshnYbIMWMA1kAS5GgPgTopKJG8vef4yZOqWKVW7NZSwqd%2Bsknm1pGuuDdKb%2BEJodZjtUBw8nVdLpynxcbU5TqrG5ZTbunIkvA8nalwXNVlfBTuwYBvXnOXxkA7P4yKCqiK0ZGqb1TYOD4PdwYCmcjhWLmoFYa5vx9eYXuDz%2FzwpPW6NwhZTU8VORA%3D%3D"

url="http://test.coinfex.com/api/v2/inner/user/weblogin"
data={"loginName":"1750095","password":password,"udesk":"false","source":"3"}

class Get_hearder():
	def get_hearder(self):
		with open(FilePath('base','token.txt'),'w') as f:
			r = obj.post(url=url,header=None, data=data)
			f.write(r.json()["data"]["token"])


	def readToken(self):
		with open(FilePath('base','token.txt'),'r') as f:
			return f.read()


if __name__ == '__main__':
	pp=Get_hearder()
	print(pp.get_hearder())
