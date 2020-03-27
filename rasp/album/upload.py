from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob, os
import json

def autentify():
	gauth = GoogleAuth()
	gauth.CommandLineAuth()
	drive = GoogleDrive(gauth)

	return drive

def read_data(filename):
    with open(filename, encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
    return data

def dict_to_json(dict,filename):
    f = open(filename, 'w')
    json.dump(dict,f,ensure_ascii=False,indent=4)
    f.close()

# def getfolderid(num):
# 	albumlist = read_data('album_id.json')

# 	return albumlist[num]

if __name__ == '__main__':
	drive = autentify()
	folder_id = "1XsM-QoDMtOVqm7-sC5hA9KcXgwYptN3W"
	namelist = read_data("filename_checklist.json")
	IMGPATH ="/home/pi/rasp/photo/"
	assert os.path.exists(IMGPATH)
	assert os.path.isdir(IMGPATH)
	imageList = os.listdir(IMGPATH)
	for image in imageList:
		if image not in namelist:
			f = drive.CreateFile({'title': image,
		                      'mimeType': 'image/jpg',
		                      'parents': [{'kind': 'drive#fileLink', 'id':folder_id}]})

			f.SetContentFile(IMGPATH+image)
			try:
				f.Upload()
			except:
				dict_to_json(['UPLOAD ERROR'],"ERRORLOG.json")