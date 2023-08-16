import pytest
from . import pytestmark
from library.math_ops import sub
class TestCase02:
    
    @pytest.mark.sub
    @pytest.mark.sanity
    def test_sub1(self):
        assert sub(3, 2) == 1, "Failed"
        
    
    @pytest.mark.sub
    @pytest.mark.xfail
    def test_sub2(self):
        assert sub(8, 5, 3) == 5, "Failed"
        
    
    @pytest.mark.sanity
    def test_sub3(self):
        assert sub(2, 0) == 2, "Failed"