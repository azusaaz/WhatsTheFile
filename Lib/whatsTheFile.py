import os
import sys
import hashlib

class wtf:

    #get filename from the given path
    def getFileName(filePath):
        if not os.path.isfile(filePath):
            return ('file does not exist')
        return (os.path.basename(filePath))

    #get filesize from the given path
    def getFileSize(filePath):
        if not os.path.isfile(filePath):
             return ('file does not exist')
        return (os.path.getsize(filePath))

    #apply md5 hush for texts in a file which is on the given path
    def to_md5(filePath):
        if not os.path.isfile(filePath):
            return ('file does not exist')
        f = open(filePath, 'r')
        str = f.read()
<<<<<<< HEAD
        str = str.strip( )
=======
        str = str.strip()  #trim the string
>>>>>>> 634cc6829edc51b558d932d85b1455b078b4b604
        str = str.encode('utf-8')
        f.close()
        return (hashlib.md5(str).hexdigest())

    #apply sha1 hush for texts in a file which is on the given path
    def to_sha1(filePath):
        if not os.path.isfile(filePath):
            return ('file does not exist')
        f = open(filePath, 'r')
        str = f.read()
<<<<<<< HEAD
        str = str.strip( )
=======
        str = str.strip()  #trim the string
>>>>>>> 634cc6829edc51b558d932d85b1455b078b4b604
        str = str.encode('utf-8')
        f.close()
        return (hashlib.sha1(str).hexdigest())

    if __name__ == '__main__':

        print ('please input a file path')
        filePath = input();

        print ('file name: %s' % getFileName(filePath))
        print ('file size: %s' % getFileSize(filePath))
        print ('md5      : %s' % to_md5(filePath))
        print ('sha1     : %s' % to_sha1(filePath))


