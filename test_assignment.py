"""
Automated tests for Problem Set 3.
These tests will be run by GitHub Classroom autograding.
"""

import pytest
import os
import sys
from io import StringIO
import subprocess  # ajouté pour créer git_log.txt automatiquement


def test_problem2_imports():
    """Test that problem2.py can be imported."""
    try:
        import problem2
        assert hasattr(problem2, 'celsius_to_fahrenheit')
        assert hasattr(problem2, 'fahrenheit_to_celsius')
    except ImportError:
        pytest.fail("Could not import problem2.py")


def test_celsius_to_fahrenheit():
    """Test Celsius to Fahrenheit conversion."""
    from problem2 import celsius_to_fahrenheit

    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(37) == 98.6


def test_fahrenheit_to_celsius():
    """Test Fahrenheit to Celsius conversion."""
    from problem2 import fahrenheit_to_celsius

    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40
    assert abs(fahrenheit_to_celsius(98.6) - 37) < 0.1


def test_problem3_imports():
    """Test that problem3.py can be imported."""
    try:
        import problem3
        assert hasattr(problem3, 'analyze_numbers')
    except ImportError:
