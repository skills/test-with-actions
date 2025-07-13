# System Modules
import sys
import os

# Installed Modules
# - None

# Project Modules
# - None

def test_python_version():
    major, minor = sys.version_info[:2]
    assert major >= 3, "Python major version must be >= 3"
    assert minor >= 10, "Python minor version must be >= 10"
