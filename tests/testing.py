import sys
import platform

platform_current = platform.platform()

if "Linux-6.14.0" in platform_current:
    print("Linux version is 6.14.0")
    assert True

version_current = platform.uname()
if "24.04.1-Ubuntu" in version_current.version:
    print("Ubuntu version is 24.04.01")
    assert True
