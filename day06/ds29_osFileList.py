# file : ds29_osFileList.py
# desc : 윈도우 파일 리스트

import os


fnameAry = []
folderName = 'c:/sources/ds-and-algorithm/day06'

for dirName, subDirList, fnames in os.walk(folderName):
    for fname in fnames:
        fnameAry.append(fname)

print(fnameAry)