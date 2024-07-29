from utils import divide
import numpy as np

def test_divide():
    numerator = np.array([0,-1,2,-1000.4])
    denominator = np.array([2,-3,1212.1212])
    # make combinations of all numerator and dominator
    # Using numpy meshgrid
    num_grid, denom_grid = np.meshgrid(numerator, denominator)
    num_combinations = num_grid.flatten()
    denom_combinations = denom_grid.flatten()

    assert np.all(divide(num_combinations, denom_combinations) == np.divide(num_combinations, denom_combinations))
