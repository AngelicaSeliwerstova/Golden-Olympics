import pytest
from main import Calculator
from contextlib import nullcontext as does_not_raise
class TestCalculator:


    @pytest.mark.parametrize("x,y,res",
                             [
                                 (1,2,0.5,does_not_raise),
                                     (5,-1,-5,does_not_raise),
                             ]
                             )
    def test_divide(self,x,y,res):
        with pytest.raises(TypeError):
            assert Calculator().divide(x,y)==res
    @pytest.mark.parametrize(
        "x,y,res",
        [
            (1,2,0.5, does_not_raise()),
            (5,-1,-5,does_not_raise),
            (5,"-1",-5,pytest.raises(TypeError))
        ]
    )
    def test_add(self,x,y,res):
        assert Calculator().divide(x,y)==res