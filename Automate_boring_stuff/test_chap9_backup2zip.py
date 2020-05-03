"""test_chap9_backup2zip.py """
import pytest
from chap9_backup2zip import create_zip_version

def test_create_version_type(int_list_not_sorted):
    """ """
    assert create_zip_version("good_name"), "5 should be part of list"