"""test_chap9_backup2zip.py """
import pytest
import sys, os
# required to allow to find the file to test in directory above the test directory
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from chap9_backup2zip import create_zip_version, backup2zip

def test_version_correct():
    """check that the entered name is correct"""
    foldername = 'dummy'
    new_foldername = foldername + "_1.zip"
    assert create_zip_version(foldername) == new_foldername

def test_version_incorrect():
    """check that the entered name is invalid. """
    empty_file = ''
    with pytest.raises(Exception) as e_info:
        create_zip_version(empty_file)

def test_backup2zip_incorrect_file():
    """check that the entered name is invalid. """
    empty_file = ''
    with pytest.raises(Exception) as e_info:
        backup2zip(empty_file)