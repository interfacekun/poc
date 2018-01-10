#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pandas as pd
import os

def mergeCVS:

	folderPath = './'          
	saveFilePath =  './'
	saveFileName = 'all.csv'

	os.chdir(folderPath)
	fileList = os.listdir()

	print("")

	fileObject = pd.read_csv(folderPath + fileList[0])

	fileObject.to_csv(saveFilePath + saveFileName, encoding="utf_8_sig", index=False, header=False)

	for i in range(1,len(fileLlist)):
		fileObject = pd.read_csv(folderPath + fileList[i])
		fileObject.to_csv(saveFilePath + saveFileName, encoding="utf_8_sig", index=False, header=False, mode='a+')
