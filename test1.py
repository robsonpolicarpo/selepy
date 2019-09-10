import unittest
from selenium import webdriver


class TestUbuntuHomepage(unittest.TestCase):

    def setUp(self):
        EXE_PATH = './driver/chromedriver'
        self.browser = webdriver.Chrome(executable_path=EXE_PATH)

    def testTitle(self):
        self.browser.get('http://www.ubuntu.com/')
        self.assertIn('Ubuntu', self.browser.title)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)