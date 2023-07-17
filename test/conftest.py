import pytest
from pyrateer.factors import CategoricalFactor, NumericFactor, ConstantFactor

@pytest.fixture
def cat_factor():
    cat_factor = CategoricalFactor(
        name = "cat",
        lookup = {"a": 1.0, "b": 1.25, "c": 1.5}
    )
    return cat_factor

@pytest.fixture
def num_factor():
    num_factor = NumericFactor(
        name = "num",
        lookup = {100_000: 1.0, 250_000: 1.25, 500_000: 1.5}
    )
    return num_factor

@pytest.fixture
def const_factor():
    const_factor = ConstantFactor(
        name="const",
        lookup=10
    )
    return const_factor