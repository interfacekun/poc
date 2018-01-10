#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pandas as pd
import os

def mergeCSV():
	print("Start merge this floder CSVs to mergeCSV.csv!")

	folderPath = './'          
	saveFilePath =  './'
	saveFileName = 'mergeCSV.csv'

	os.chdir(folderPath)
	fileList = os.listdir()

	fileObject = pd.read_csv(folderPath + fileList[0])
	fileObject.to_csv(saveFilePath + saveFileName, encoding="utf_8_sig", index=False, header=False)

	for i in range(1,len(fileList)):
		fileObject = pd.read_csv(folderPath + fileList[i])
		fileObject.to_csv(saveFilePath + saveFileName, encoding="utf_8_sig", index=False, header=False, mode='a+')
	
	print("Merge CSVs done! Total merge" + len(fileList) + "files.")

if __name__ == '__main__':
	mergeCSV()