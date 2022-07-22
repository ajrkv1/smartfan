import unittest
from unittest import TestCase
import requests


HOST = 'privatepi'
PORT = 5000

class LightTestCase(TestCase):

    def test_get(self):
        res = requests.get(f'http://{HOST}:{PORT}/light')
        self.assertFalse(res.json()['light'])
    
    def test_post(self):
        res = requests.post(f'http://{HOST}:{PORT}/light')
        self.assertTrue(res.json()['light'])
        res = requests.post(f'http://{HOST}:{PORT}/light')
        self.assertFalse(res.json()['light'])

class FanTestCase(TestCase):
    def test_get(self):
        res = requests.get(f'http://{HOST}:{PORT}/fan')
        self.assertEqual(res.json()['fan'],0)
    
    def test_post(self):
        res = requests.post(f'http://{HOST}:{PORT}/fan',json={"power":2},headers={"Content-Type": "application/json"})
        self.assertEqual(res.json()['fan'],2)
        res = requests.post(f'http://{HOST}:{PORT}/fan',json={"power":0},headers={"Content-Type": "application/json"})
        self.assertEqual(res.json()['fan'],0)
        res = requests.post(f'http://{HOST}:{PORT}/fan',json={"power":5},headers={"Content-Type": "application/json"})
        self.assertEqual(res.json()['status'],400)


if __name__ == '__main__':
    unittest.main()
