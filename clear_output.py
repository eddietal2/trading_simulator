#!/usr/bin/env python3
"""
Script to clear the contents of the output directory.
"""

import os

# Path to the output directory
output_dir = "output"

def clear_output_dir():
    """
    Clears all contents of the output directory.
    """
    if os.path.exists(output_dir):
        for root, dirs, files in os.walk(output_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        print(f"Cleared all contents of {output_dir}")
    else:
        print(f"Output directory not found: {output_dir}")

if __name__ == "__main__":
    clear_output_dir()