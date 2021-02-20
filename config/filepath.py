import os

baseurl=os.path.dirname(os.path.dirname(__file__))

def FilePath(dir,filename):
	return os.path.join(baseurl,dir,filename)


# if __name__ == '__main__':
#     print(FilePath('config','filepath.py'))