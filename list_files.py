"""This module list files from a directory following a specific pattern"""

import os
import fnmatch
from datetime import date, datetime

def list_files(directory: str, pattern: str) -> list:
    """This function lists files from a directory following a specific pattern"""
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.startswith(pattern)]