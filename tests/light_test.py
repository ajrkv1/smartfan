import unittest
import requests

HOST = 'privatepi'
PORT = 5000

class LightTestCase(unittest.TestCase):

    def test_initial(self):
        res = requests.get(f'http://{HOST}:{PORT}/light')
        self.assertFalse(res.json()['light'])
    
    def test_post(self):
        res = requests.post(f'http://{HOST}:{PORT}/light')
        self.assertTrue(res.json()['light'])
        res = requests.post(f'http://{HOST}:{PORT}/light')
        self.assertFalse(res.json()['light'])


if __name__ == '__main__':
    unittest.main()
