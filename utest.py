import os
import unittest

from Lib import whatsTheFile


class Test(unittest.TestCase):
    def testName():
        assert(getFileName("./mmydata.txt")== mydata.txt)
                         

    def testSize():
        assert(getFileSize("./mydata.txt")== 44)

if __name__ == '__main__':
    unittest.main()