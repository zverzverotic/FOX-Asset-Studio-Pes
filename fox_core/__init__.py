"""
FOX Asset Studio
Core package

Author:
FOX Asset Studio Project

Target:
PES 2021 FOX Engine

Python:
3.9+

Blender:
2.92+
"""

__version__ = "0.1.0"

from .asset import FoxAsset
from .parser import FoxParser

__all__ = [
    "FoxAsset",
    "FoxParser",
]
