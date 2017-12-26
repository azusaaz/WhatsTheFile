import os
import sys

from Lib import whatsTheFile

print ('please input a file path')
filePath = input();

a = whatsTheFile
print ("")
print (a.wtf.getFileName(filePath))
print (a.wtf.getFileSize(filePath))
print (a.wtf.to_md5(filePath))
print (a.wtf.to_sha1(filePath))


