import pytest
from . import pytestmark
from library.math_ops import add
class TestCase01:
    
    @pytest.mark.add
    @pytest.mark.sanity
    def test_add1(self):
        assert add(2, 3) == 5, "Failed"
        
    
    @pytest.mark.add
    @pytest.mark.xfail
    def test_add2(self):
        assert add(5, 3, 8) == 5, "Failed"
        
    
    @pytest.mark.sanity
    def test_add3(self):
        assert add(2, 0) == 2, "Failed"
        
        
    def test_add4(self):
        assert add(2, 3) == 0, 'Failed'