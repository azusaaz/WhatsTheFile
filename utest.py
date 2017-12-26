import os
import unittest

from Lib import whatsTheFile


class Test(unittest.TestCase):
    filepath = "./mydata.txt"
    def testName(self):
        self.assertEqual(getFileName(filepath),mydata.txt)
                         

    def testSize(self):
        self.assertEqual(getFileSize(filepath),"44")

if __name__ == '__main__':
    unittest.main()