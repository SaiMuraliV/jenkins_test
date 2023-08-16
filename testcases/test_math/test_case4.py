import pytest
from . import pytestmark
from library.math_ops import div
class TestCase04:
    
    @pytest.mark.div
    @pytest.mark.sanity
    def test_div1(self):
        assert div(3, 2) == (1,1), "Failed"
        
    
    @pytest.mark.div
    def test_div2(self):
        assert div(8, 5) == (1, 3), "Failed"
        
    
    @pytest.mark.xfail
    @pytest.mark.sanity
    def test_div3(self):
        assert div(2, 0) == (2, 0), "Failed"