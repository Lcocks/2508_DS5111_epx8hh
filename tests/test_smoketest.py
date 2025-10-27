##  Testing file for my_normalizer.py  ##

import os
import sys
sys.path.append('.') # path gets filled with list of directory in which python will find the package we want installed.

import pytest
import platform
from bin.my_normalizer import normalize_yahoo, normalize_wsj
from bin.gainers.base import GainerBase
from bin.gainers.yahoo import GainerYahoo
from bin.gainers.wsj import GainerWSJ
import pandas as pd
import re

def test_of_pytest():
    assert True

def test_python_version():
    python_current = sys.version_info

    if python_current.major == 3 and (python_current.minor == 12 or python_current.minor ==13):
        print("Python version is 3.12 or 3.13")
        assert True
    else:
        assert False, "Python version is NOT 3.12 or 3.13"

def test_os():
    platform_current = platform.platform()

    if "Linux-6.14.0" in platform_current:
        print("Linux version is 6.14")
        assert True

    version_current = platform.uname()

    if "24.04.1-Ubuntu" in version_current.version:
        print("Ubuntu version is 24.04.01")
        assert True


##Test the yahoo.py and wsj.py work with base.py
#def test_gainer_yahoo_inherits_from_base():
#    """Test that GainerYahoo inherits from GainerBase"""
#    gainer = GainerYahoo()
#    assert hasattr(gainer, 'html')
#    assert hasattr(gainer, 'csv')
#    assert hasattr(gainer, 'normalize')
#def test_gainer_wsj_inherits_from_base():
#    """Test that GainerYahoo inherits from GainerBase"""
#    gainer = GainerWSJ()
#    assert hasattr(gainer, 'html')
#    assert hasattr(gainer, 'csv')
#    assert hasattr(gainer, 'normalize')


# Test normalize_yahoo
def test_normalize_yahoo_columns():
    """Test that normalize_yahoo creates correct columns"""

    if not os.path.isfile("./ygainers.csv"):
        pytest.skip("No ygainers.csv files found")

    gainer = GainerYahoo()
    gainer.normalize_data()
#    df = pd.read_csv("./ygainers.csv", index_col = 0)
#    normalize_yahoo(df)
    result = pd.read_csv('normalized_ygainers.csv')

    assert list(result.columns) == ['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']

def test_normalize_yahoo_perc_change_cleaning():
    """Test that perc_change removes +% symbols"""

    if not os.path.isfile("./ygainers.csv"):
        pytest.skip("No ygainers.csv files found")

    gainer = GainerYahoo()
    gainer.normalize_data()
#    df = pd.read_csv("./ygainers.csv", index_col = 0)
#    normalize_yahoo(df)
    result = pd.read_csv('normalized_ygainers.csv')

    # Verify perc_change has no + or % symbols
    assert 'perc_change' in result.columns
    for val in result['perc_change']:
        assert '+' not in str(val)
        assert '%' not in str(val)

def test_normalize_yahoo_removes_nan_rows():
    """Test NaN values are dropped"""

    if not os.path.isfile("./ygainers.csv"):
        pytest.skip("No ygainers.csv files found")

    gainer = GainerYahoo()
    gainer.normalize_data()
    df = pd.read_csv("./ygainers.csv", index_col = 0)
    original_len = len(df)
#    normalize_yahoo(df)

    result = pd.read_csv('normalized_ygainers.csv')

    # Verify no NaN values in numeric columns
    numeric_cols = ['price', 'change', 'perc_change', 'volume']
    assert result[numeric_cols].notna().all().all()
    # Result should have fewer or equal rows (NaNs dropped)
    assert len(result) <= original_len


#Test normalize_wsj
def test_normalize_wsj_symbol_extraction():
    """Test that symbol is extracted from company_name"""

    if not os.path.isfile("./wsjgainers.csv"):
        pytest.skip("No wsjgainers.csv files found")

    gainer = GainerWSJ()
    gainer.normalize_data()
#    df = pd.read_csv("./wsjgainers.csv", index_col = 0)
#    normalize_wsj(df)
    result = pd.read_csv('normalized_wsjgainers.csv')

    # Verify symbol column exists and contains uppercase letters
    assert 'symbol' in result.columns
    assert result['symbol'].notna().any()
    assert result['symbol'].iloc[0].isupper()
    assert result['symbol'].iloc[0].isalpha()

def test_normalize_wsj_company_name_cleaning():
    """Test that company_name removes ticker symbol"""

    if not os.path.isfile("./wsjgainers.csv"):
        pytest.skip("No wsjgainers.csv files found")

    gainer = GainerWSJ()
    gainer.normalize_data()
#    df = pd.read_csv("./wsjgainers.csv", index_col = 0)
#    normalize_wsj(df)
    result = pd.read_csv('normalized_wsjgainers.csv')

    # Verify company_name has no ticker symbols in parentheses
    assert 'company_name' in result.columns
    for name in result['company_name']:
        assert not re.search(r'\([A-Z]+\)$', str(name))

def test_normalize_wsj_columns():
    """Test that normalize_wsj creates correct columns"""

    if not os.path.isfile("./wsjgainers.csv"):
        pytest.skip("No wsjgainers.csv files found")

    gainer = GainerWSJ()
    gainer.normalize_data()
#    df = pd.read_csv("./wsjgainers.csv", index_col = 0)
#    normalize_wsj(df)
    result = pd.read_csv('normalized_wsjgainers.csv')
    assert list(result.columns) == ['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']

def test_normalize_wsj_removes_nan_rows():
    """Testing NaN values are dropped"""

    if not os.path.isfile("./wsjgainers.csv"):
        pytest.skip("No wsjgainers.csv files found")

    gainer = GainerWSJ()
    gainer.normalize_data()
    df = pd.read_csv("./wsjgainers.csv", index_col = 0)
    original_len = len(df)
#    normalize_wsj(df)
    result = pd.read_csv('normalized_wsjgainers.csv')

    # Verify no NaN values in numeric columns
    numeric_cols = ['price', 'change', 'perc_change', 'volume']
    assert result[numeric_cols].notna().all().all()
    # Result should have fewer or equal rows (NaNs dropped)
    assert len(result) <= original_len


