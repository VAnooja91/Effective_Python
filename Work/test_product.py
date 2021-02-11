import product
import unittest


class TestProduct(unittest.TestCase):
    def test_create(self):
        p = product.Product('MINT', 100, 490.1)
        self.assertEqual(p.name, 'MINT')
        self.assertEqual(p.quant, 100)
        self.assertEqual(p.price, 490.1)

    def test_check_cost(self):
        p = product.Product('MINT', 100, 490.1)
        self.assertEqual(p.cost, 49010.0)

    def test_bad_cost(self):
        p = product.Product('MINT', 100, 490.1)
        with self.assertRaises(TypeError):
            p.quant = "14"


if __name__ == "__main__":
    unittest.main()