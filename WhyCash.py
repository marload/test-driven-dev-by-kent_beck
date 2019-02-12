import unittest

class Dollar:
    def __init__(self, amount):
        self.amount = amount
    
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, other):
        dollar = other
        return self.amount == dollar.amount

class Main(unittest.TestCase):
    def main(self):
        self.testMultiplycation()

    def testMultiplycation(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEquals(10, product.amount)
        product = five.times(3)
        self.assertEquals(15, product.amount)
    
    def testEquality(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        self.assertFalse(Dollar(5).equals(Dollar(6)))

if __name__ == "__main__":
    unittest.main()