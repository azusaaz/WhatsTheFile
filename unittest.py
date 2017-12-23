import os
import unittest

From Lib import whatsTheFile


class MyTest(unittest.TestCase):
    def test_file_name(self):
        self.assertEqual(getFileName("./mydata.txt"),mydata.txt)
                         

    def test_file_size(self):
        self.assertEqual(getFileSize("./mydata.txt"), 44)

if __name__ == '__main__':
    unittest.main()