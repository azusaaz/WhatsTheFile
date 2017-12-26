import os
import unittest

from Lib import whatsTheFile


class Test(unittest.TestCase):
    a = whatsTheFile
    filepath = "./mydata.txt"
    def testName(self):
        self.assertEqual(a.wtf.getFileName(filepath),mydata.txt)
                         

    def testSize(self):
        self.assertEqual(a.wtf.getFileSize(filepath),"44")

if __name__ == '__main__':
    unittest.main()