"""
Simple test script for array_profile function.
"""

import numpy as np
import sys
import os

# Add the numpy directory to the path
sys.path.insert(0, os.path.abspath('numpy'))

# Import our array_profile function
from numpy.lib._array_profile_impl import array_profile

# Test with a simple array
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Testing with array:")
print(a)
print("\nArray profile:")
array_profile(a)

# Test with a float array
b = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
print("\nTesting with float array:")
print(b)
print("\nArray profile:")
array_profile(b)

# Test with an array containing NaN
c = np.array([1, 2, np.nan, 4, 5])
print("\nTesting with array containing NaN:")
print(c)
print("\nArray profile:")
array_profile(c)

print("\nAll tests completed successfully!")