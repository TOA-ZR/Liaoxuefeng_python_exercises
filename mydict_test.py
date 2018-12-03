import unittest

from mydict import Dict

class TestDist(unittest.TestCase):

    def test_init(self):
        d = Dict(a = 1, b="test")
        self.assertEqual(d.a,1)#断言，d.a应该等于1。不等于就报错
        self.assertEqual(d.b,"test")#可以直接写成属性的形式，一般是写成d["a"]
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d = Dict()
        d["key"] = "value"
        self.assertTrue(d.key,"value")

    def test_attr(self):
        d = Dict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"],"value")

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d["empty"]

    def test_attrerror(self):
        d =Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
            print('setUp...')

    def tearDown(self):
            print('tearDown...')







