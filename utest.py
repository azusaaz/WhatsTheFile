import os
import unittest

from Lib import whatsTheFile


class Test(unittest.TestCase):
<<<<<<< HEAD
    def testName():
        assert(getFileName("./mmydata.txt")== mydata.txt)
                         

    def testSize():
        assert(getFileSize("./mydata.txt")== 44)
=======
  
    def testName(self):
        a = whatsTheFile
        filepath = "./mydata.txt"
        self.assertEqual(a.wtf.getFileName(filepath),"mydata.txt")
                         
    def testSize(self):
        a = whatsTheFile
        filepath = "./mydata.txt"
        self.assertEqual(a.wtf.getFileSize(filepath), 43)
        print (a.wtf.getFileSize(filepath))

    def testSize(self):
        a = whatsTheFile
        filepath = "./mydata.txt"
        self.assertEqual(a.wtf.to_md5(filepath),"9e107d9d372bb6826bd81d3542a419d6")

    def testSize(self):
        a = whatsTheFile
        filepath = "./mydata.txt"
        self.assertEqual(a.wtf.to_sha1(filepath),"2fd4e1c67a2d28fced849ee1bb76e7391b93eb12")
>>>>>>> test3

if __name__ == '__main__':
    unittest.main()