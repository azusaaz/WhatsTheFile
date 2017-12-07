import sys
import os

from Lib import whatsTheFile

print ('please input a file path')
filePath = input();

a = whatsTheFile
print ("")
print (a.whatsTheFile.getFileName(filePath))
print (a.whatsTheFile.getFileSize(filePath))
print (a.whatsTheFile.to_md5(filePath))
print (a.whatsTheFile.to_sha1(filePath))


