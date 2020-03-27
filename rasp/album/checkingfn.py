from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob, os
import json

def autentify():
	gauth = GoogleAuth()
	gauth.CommandLineAuth()
	drive = GoogleDrive(gauth)

	return drive

def dict_to_json(dict,filename):
    f = open(filename, 'w')
    json.dump(dict,f,ensure_ascii=False,indent=4)
    f.close()

def read_data(filename):
    with open(filename, encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
    return data

# def getfolderid(num):
# 	albumlist = read_data('album_id.json')

# 	return albumlist[num]

if __name__ == '__main__':
	drive = autentify()
	folder_id = "1XsM-QoDMtOVqm7-sC5hA9KcXgwYptN3W"
	try:
		file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder_id)}).GetList()
	except:
		file_list = []
		file_list.append("CONNECTION OR ID ERROR!")

	fn = []
	for filename in file_list:
		fn.append(filename['title'])

	print(fn)
	dict_to_json(fn,"filename_checklist.json")