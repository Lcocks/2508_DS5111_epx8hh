##  Testing file for my_normalizer.py  ##

import sys
sys.path.append('.') # path gets filled with list of directory in which python will find the package we want installed.

import platform
import bin.my_normalizer as nm


def test_of_pytest():
    assert True

def test_python_version():
    python_current = sys.version_info

    if python_current.major == 3 and python_current.minor == 12 and python_current.micro == 3:
        print("Python version is 3.12.3")
        assert True
    else:
        assert False, "Python version is NOT 3.12.3"

def test_os():
    platform_current = platform.platform()

    if "Linux-6.14.0" in platform_current:
        print("Linux version is 6.14.0")
        assert True

    version_current = platform.uname()

    if "24.04.1-Ubuntu" in version_current.version:
        print("Ubuntu version is 24.04.01")
        assert True

#def test_normalizer():
#    nm.normalize_yahoo("test")
#    assert response == "Hello"

