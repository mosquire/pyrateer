import pytest
from pyrateer.factors import CompoundFactor


class TestCategoricalFactor():
    def test_cat_factor_lookup(self, cat_factor):
        assert cat_factor.calculate("a") == 1.0
        assert cat_factor.calculate("b") == 1.25
        assert cat_factor.calculate("c") == 1.5

class TestNumericFactor():
    def test_num_factor_lookup_values(self, num_factor):
        assert num_factor.calculate(50_000) == 1.0
        assert num_factor.calculate(200_000) == pytest.approx(1.1666667)
        assert num_factor.calculate(250_000) == 1.25
        assert num_factor.calculate(700_000) == 1.5

class TestConstantFactor():
    def test_const_factor_return_value(self, const_factor):
        assert const_factor.calculate() == 10

class TestCompoundFactor():
    def test_compound_constructor(self, cat_factor, num_factor):
        sum_factor = cat_factor + num_factor
        assert isinstance(sum_factor, CompoundFactor)
        assert sum_factor.operator == "+"
        assert sum_factor.lhs == cat_factor
        assert sum_factor.rhs == num_factor

    def test_sum_numeric_cat(self, cat_factor, num_factor):
        sum_factor = cat_factor + num_factor
        rate_params = {"cat": "c", "num": 130_000}
        assert sum_factor.calculate(**rate_params) == 2.55
    
    def test_sum_numeric_const(self, num_factor, const_factor):
        sum_factor = num_factor + const_factor
        rate_params = {"num": 130_000}
        assert sum_factor.calculate(**rate_params) == 11.05
        
    def test_product_numeric_cat(self, cat_factor, num_factor):
        product_factor = cat_factor * num_factor
        rate_params = {"cat": "c", "num": 250_000}
        assert product_factor.calculate(**rate_params) == 1.875
        
    def test_product_numeric_const(self, num_factor, const_factor):
        sum_factor = num_factor * const_factor
        rate_params = {"num": 130_000}
        assert sum_factor.calculate(**rate_params) == 10.5

    def test_product_numeric_cat(self, cat_factor, num_factor):
        difference_factor = cat_factor - num_factor
        rate_params = {"cat": "c", "num": 250_000}
        assert difference_factor.calculate(**rate_params) == 0.25
        
    def test_product_numeric_const(self, num_factor, const_factor):
        difference_factor = num_factor - const_factor
        rate_params = {"num": 130_000}
        assert difference_factor.calculate(**rate_params) == -8.95