import os
import unittest

from Lib import whatsTheFile


class Test(unittest.TestCase):
  
    def testName(self):
        a = whatsTheFile
        filepath = "./mydata.txt"
        self.assertEqual(a.wtf.getFileName(filepath),"mydata.txt")
                         

    def testSize(self):
        a = whatsTheFile
        filepath = "./mydata.txt"
        self.assertEqual(a.wtf.getFileSize(filepath),"43")

if __name__ == '__main__':
    unittest.main()