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



    if __name__ == '__main__':

        print ('please input a file path')
        filePath = input();

        print ('file name: %s' % getFileName(filePath))
        print ('file size: %s' % getFileSize(filePath))


