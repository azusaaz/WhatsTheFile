import os
import sys
import hashlib


class whatsTheFile:

    def getFileName(filePath):
        if not os.path.isfile(filePath):
            return ('file does not exist')
        return (os.path.basename(filePath))

    def getFileSize(filePath):
        if not os.path.isfile(filePath):
             return ('file does not exist')
        return (os.path.getsize(filePath))

    def to_md5(filePath):
        if not os.path.isfile(filePath):
            return ('file does not exist')
        f = open(filePath, 'r')
        str = f.read()
        f.close()
        return (hashlib.md5(str.encode('utf-8')).digest())

    def to_sha1(filePath):
        if not os.path.isfile(filePath):
            return ('file does not exist')
        f = open(filePath, 'r')
        str = f.read()
        f.close()
        return (hashlib.sha1(str.encode('utf-8')).digest())

    if __name__ == '__main__':

        print ('please input a file path')
        filePath = input();

        print ('file name: %s' % getFileName(filePath))
        print ('file size: %s' % getFileSize(filePath))


