import pytest
from . import pytestmark
from library.math_ops import mul
class TestCase03:
    
    @pytest.mark.sub
    @pytest.mark.sanity
    def test_mul1(self):
        assert mul(3, 2) == 6, "Failed"
        
    
    @pytest.mark.mul
    @pytest.mark.xfail
    def test_mul2(self):
        assert mul(8, 5) == 45, "Failed"
        
    
    @pytest.mark.sanity
    def test_mul3(self):
        assert mul(2, 0) == 0, "Failed"