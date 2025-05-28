import os
import sys

# Add the parent directory to the Python path to import models.py

try:
    from lib.db import models
    print("models.py imported successfully.")
except ImportError:
    print("models.py not found in the current directory.")

if __name__ == "__main__":
    # Example: Call a function or class from models.py if it exists
    if hasattr(models, 'main'):
        models.main()
    else:
        print("models.py imported successfully. Add a 'main' function to run.")