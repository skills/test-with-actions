# System Modules
import sys
import os
import unittest

# Installed Modules
# - None

# Project Modules
# - None

class SupportedVersions(unittest.TestCase):

    def test_python_version(self):
        major, minor = sys.version_info[:2]
        self.assertGreaterEqual(major, 3, "Python major version must be >= 3")
        self.assertGreaterEqual(minor, 10, "Python minor version must be >= 10")

if __name__ == "__main__":
    unittest.main()
