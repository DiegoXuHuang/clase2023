import unittest
from app.multi import multiplicacion
class TestMulti(unittest.testCase):
    def test_multi(self):
        self.assertEqual(multiplicacion(2,3),6)


if __name__ == '__main__':
    unittest.main()