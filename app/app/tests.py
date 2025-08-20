"""
Sample Test
"""
from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """Test che calc module."""
    def test_add_numbers(self):
        """testing adding numbers together"""
        res = calc.add( 5, 6 )
        self.assertEqual( res, 11 )

    def test_subtracting(self):
        res = calc.subtract( 10, 15 )
        
        self.assertEqual(res, 7 )

